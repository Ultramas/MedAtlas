from django.db import models
from django.core.validators import RegexValidator, URLValidator, MinValueValidator, MaxValueValidator
from django.utils import timezone

# Reusable validators
phone_validator = RegexValidator(
    regex=r"^\+?[0-9\-\(\) ]{7,}$",
    message="Enter a valid phone number."
)
url_validator = URLValidator()

class Cost(models.TextChoices):
    FREE = "free", "Free"
    LOW = "low_cost", "Low cost"
    SLIDING = "sliding", "Sliding scale"
    VARIES = "varies", "Varies"


class MedAtlasListing(models.Model):
    name = models.CharField(max_length=255, db_index=True)                    # e.g., "Mercy Clinic Midtown"
    organization_name = models.CharField(max_length=200, blank=True)          # e.g., "Dignity Health"
    organization_website = models.URLField(blank=True)                        # optional
    organization_phone = models.CharField(max_length=30, blank=True, validators=[phone_validator])

    # — Address —
    street = models.CharField(max_length=255)
    city_text = models.CharField(max_length=120)
    state = models.CharField(max_length=2)                                    # "CA"
    postal_code = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=2, default="US")

    # — Contact —
    phone = models.CharField(max_length=30, blank=True, validators=[phone_validator])
    website = models.URLField(blank=True)

    # — City scoping (for simple routing/chapters) —
    city_slug = models.SlugField(max_length=80, blank=True, help_text="Short code for city/region, e.g., 'sac'")

    # — Cost & Services —
    cost = models.CharField(max_length=12, choices=Cost.choices, default=Cost.FREE, db_index=True)

    # Simple comma-separated strings for lists to avoid DB-specific array fields
    services_csv = models.TextField(
        blank=True,
        help_text="Comma-separated service codes or labels (e.g., 'MH.COUNSEL,WOMEN.PRENATAL')."
    )
    languages_csv = models.TextField(
        blank=True,
        help_text="Comma-separated language codes (e.g., 'en,es,vi,zh')."
    )
    insurance_csv = models.TextField(
        blank=True,
        help_text="Comma-separated insurance names (e.g., 'Medicaid,Medicare,None')."
    )

    # — Flexible structured fields kept as JSON —
    eligibility = models.JSONField(default=dict, blank=True)       # e.g., {"uninsured": true, "income_max_pct_fpl": 200}
    accessibility = models.JSONField(default=dict, blank=True)     # e.g., {"wheelchair": true, "interpreter": true}
    hours = models.JSONField(default=dict, blank=True)             # e.g., {"mon":[{"open":"09:00","close":"17:00"}], ...}

    # — Geo (no GIS): simple lat/lng for distance calcs client-side or via plain SQL —
    latitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True,
        validators=[MinValueValidator(-90), MaxValueValidator(90)]
    )
    longitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True,
        validators=[MinValueValidator(-180), MaxValueValidator(180)]
    )

    # — Verification (flattened) —
    verified = models.BooleanField(default=False)
    last_verified_at = models.DateTimeField(null=True, blank=True)
    verifier_name = models.CharField(max_length=200, blank=True, help_text="Non-sensitive name/title if desired.")
    verifier_org = models.CharField(max_length=200, blank=True, help_text="e.g., 'County Public Health Dept'")

    # — Evidence (flattened; replaces change/evidence tables) —
    evidence_urls = models.JSONField(default=list, blank=True)     # list of strings (URLs)
    evidence_note = models.TextField(blank=True)

    # — Ops —
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # Reasonable uniqueness to limit dupes while still allowing edits before address is perfect
        constraints = [
            models.UniqueConstraint(
                fields=["name", "street", "city_text", "state"],
                name="uniq_listing_basic_address",
                deferrable=models.Deferrable.DEFERRED,
            ),
        ]
        indexes = [
            models.Index(fields=["name"]),
            models.Index(fields=["city_slug"]),
            models.Index(fields=["state", "verified", "is_active"]),
        ]
        ordering = ["-verified", "name"]

    # — Convenience helpers for CSV fields —
    @staticmethod
    def _split_csv(value: str) -> list[str]:
        if not value:
            return []
        return [x.strip() for x in value.split(",") if x.strip()]

    @staticmethod
    def _join_csv(values: list[str]) -> str:
        return ",".join(sorted({v.strip() for v in values if v and v.strip()}))

    @property
    def services(self) -> list[str]:
        return self._split_csv(self.services_csv)

    @services.setter
    def services(self, values: list[str]):
        self.services_csv = self._join_csv(values)

    @property
    def languages(self) -> list[str]:
        return self._split_csv(self.languages_csv)

    @languages.setter
    def languages(self, values: list[str]):
        self.languages_csv = self._join_csv(values)

    @property
    def insurance(self) -> list[str]:
        return self._split_csv(self.insurance_csv)

    @insurance.setter
    def insurance(self, values: list[str]):
        self.insurance_csv = self._join_csv(values)

    # — Simple helpers —
    def address_line(self) -> str:
        z = f" {self.postal_code}" if self.postal_code else ""
        return f"{self.street}, {self.city_text}, {self.state}{z}"

    def mark_verified(self, name: str = "", org: str = ""):
        self.verified = True
        self.last_verified_at = timezone.now()
        if name:
            self.verifier_name = name
        if org:
            self.verifier_org = org
        self.save(update_fields=["verified", "last_verified_at", "verifier_name", "verifier_org", "updated_at"])

    def __str__(self) -> str:
        return self.name
