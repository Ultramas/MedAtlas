# admin.py
from django.contrib import admin
from django import forms
from django.utils import timezone
from django.utils.html import format_html
from django.db.models import QuerySet

from .models import MedAtlasListing, Cost


# ---------- Forms: nicer JSON handling + light CSV normalization ----------
class MedAtlasListingForm(forms.ModelForm):
    # Use JSONField form widgets for better validation and UX
    eligibility = forms.JSONField(required=False, widget=forms.Textarea(attrs={"rows": 6}))
    accessibility = forms.JSONField(required=False, widget=forms.Textarea(attrs={"rows": 6}))
    hours = forms.JSONField(required=False, widget=forms.Textarea(attrs={"rows": 8}))
    evidence_urls = forms.JSONField(required=False, widget=forms.Textarea(attrs={"rows": 4}))

    class Meta:
        model = MedAtlasListing
        fields = "__all__"
        widgets = {
            "services_csv": forms.Textarea(attrs={"rows": 2, "placeholder": "MH.COUNSEL,WOMEN.PRENATAL"}),
            "languages_csv": forms.Textarea(attrs={"rows": 2, "placeholder": "en,es,vi,zh"}),
            "insurance_csv": forms.Textarea(attrs={"rows": 2, "placeholder": "Medicaid,Medicare,None"}),
            "evidence_note": forms.Textarea(attrs={"rows": 3}),
            "street": forms.TextInput(attrs={"size": 50}),
            "organization_website": forms.URLInput(attrs={"size": 50}),
            "website": forms.URLInput(attrs={"size": 50}),
        }

    # Normalize comma-separated fields (strip spaces, dedupe, keep stable order)
    def clean_services_csv(self):
        raw = self.cleaned_data.get("services_csv", "") or ""
        parts = [p.strip() for p in raw.split(",") if p.strip()]
        return ",".join(sorted(set(parts)))

    def clean_languages_csv(self):
        raw = self.cleaned_data.get("languages_csv", "") or ""
        parts = [p.strip() for p in raw.split(",") if p.strip()]
        return ",".join(sorted(set(parts)))

    def clean_insurance_csv(self):
        raw = self.cleaned_data.get("insurance_csv", "") or ""
        parts = [p.strip() for p in raw.split(",") if p.strip()]
        return ",".join(sorted(set(parts)))


# ---------- Filters ----------
class HasCoordinatesFilter(admin.SimpleListFilter):
    title = "Has coordinates"
    parameter_name = "has_coords"

    def lookups(self, request, model_admin):
        return (
            ("yes", "Yes"),
            ("no", "No"),
        )

    def queryset(self, request, queryset: QuerySet):
        if self.value() == "yes":
            return queryset.filter(latitude__isnull=False, longitude__isnull=False)
        if self.value() == "no":
            return queryset.filter(latitude__isnull=True) | queryset.filter(longitude__isnull=True)
        return queryset


# ---------- Admin ----------
@admin.register(MedAtlasListing)
class MedAtlasListingAdmin(admin.ModelAdmin):
    form = MedAtlasListingForm

    # List page columns
    list_display = (
        "name",
        "city_text",
        "state",
        "cost",
        "verified",
        "last_verified_at",
        "is_active",
        "phone_link",
        "website_link",
    )
    list_filter = (
        "state",
        "verified",
        "is_active",
        "cost",
        "city_slug",
        HasCoordinatesFilter,
    )
    search_fields = (
        "name",
        "organization_name",
        "street",
        "city_text",
        "postal_code",
        "phone",
        "organization_phone",
        "website",
        "organization_website",
    )
    ordering = ("-verified", "name")
    date_hierarchy = "last_verified_at"

    # Layout of the edit page
    fieldsets = (
        ("Identity & Organization", {
            "fields": (
                ("name", "organization_name"),
                ("organization_website", "organization_phone"),
            )
        }),
        ("Address", {
            "fields": (
                ("street", "city_text"),
                ("state", "postal_code", "country"),
                "city_slug",
            )
        }),
        ("Contact", {
            "fields": (("phone", "website"),)
        }),
        ("Attributes", {
            "fields": (
                "cost",
                "services_csv",
                "languages_csv",
                "insurance_csv",
                "eligibility",
                "accessibility",
                "hours",
            )
        }),
        ("Geolocation (optional)", {
            "fields": (("latitude", "longitude"),),
            "description": "Decimal degrees (WGS84). No GIS dependencies required."
        }),
        ("Verification", {
            "fields": (
                "verified",
                "last_verified_at",
                ("verifier_name", "verifier_org"),
            )
        }),
        ("Evidence (flat)", {
            "fields": ("evidence_urls", "evidence_note"),
        }),
        ("Operational", {
            "fields": (("is_active",), ("created_at", "updated_at")),
        }),
    )

    readonly_fields = ("created_at", "updated_at", "last_verified_at")

    # Helpful links in list view
    def phone_link(self, obj: MedAtlasListing):
        if obj.phone:
            return format_html('<a href="tel:{}">{}</a>', obj.phone, obj.phone)
        return "-"
    phone_link.short_description = "Phone"

    def website_link(self, obj: MedAtlasListing):
        if obj.website:
            return format_html('<a href="{}" target="_blank" rel="noopener">Website</a>', obj.website)
        return "-"
    website_link.short_description = "Website"

    # Bulk actions
    actions = ("mark_verified_action", "mark_inactive_action", "mark_active_action")

    def mark_verified_action(self, request, queryset: QuerySet):
        updated = 0
        now = timezone.now()
        for obj in queryset:
            if not obj.verified:
                obj.verified = True
                obj.last_verified_at = now
                obj.save(update_fields=["verified", "last_verified_at", "updated_at"])
                updated += 1
        self.message_user(request, f"Marked {updated} listing(s) as verified.")
    mark_verified_action.short_description = "Mark selected as verified"

    def mark_inactive_action(self, request, queryset: QuerySet):
        updated = queryset.update(is_active=False)
        self.message_user(request, f"Marked {updated} listing(s) inactive.")
    mark_inactive_action.short_description = "Mark selected as inactive"

    def mark_active_action(self, request, queryset: QuerySet):
        updated = queryset.update(is_active=True)
        self.message_user(request, f"Marked {updated} listing(s) active.")
    mark_active_action.short_description = "Mark selected as active"

    # Auto-stamp last_verified_at if user toggles 'verified' in the form
    def save_model(self, request, obj: MedAtlasListing, form, change):
        if change:
            # If the verified flag changed from False→True, set timestamp
            if "verified" in form.changed_data and obj.verified and not obj.last_verified_at:
                obj.last_verified_at = timezone.now()
        super().save_model(request, obj, form, change)

admin.site.site_header = "MedAtlas Administration"
admin.site.site_title = "MedAtlas Admin"
admin.site.index_title = "Data & Listings"
