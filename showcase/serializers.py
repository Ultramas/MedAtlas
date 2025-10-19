# serializers.py
from rest_framework import serializers
from .models import MedAtlasListing

class MedAtlasListingSerializer(serializers.ModelSerializer):
    cost_label = serializers.SerializerMethodField()
    services = serializers.SerializerMethodField()
    languages = serializers.SerializerMethodField()
    insurance = serializers.SerializerMethodField()
    address = serializers.SerializerMethodField()

    class Meta:
        model = MedAtlasListing
        fields = [
            "id",
            "name",
            "organization_name",
            "organization_website",
            "organization_phone",
            "street",
            "city_text",
            "state",
            "postal_code",
            "country",
            "phone",
            "website",
            "city_slug",
            "cost",
            "cost_label",
            "services",
            "languages",
            "insurance",
            "verified",
            "latitude",
            "longitude",
            "address",
        ]

    def get_cost_label(self, obj):
        return obj.get_cost_display()

    def get_services(self, obj):
        return obj.services

    def get_languages(self, obj):
        return obj.languages

    def get_insurance(self, obj):
        return obj.insurance

    def get_address(self, obj):
        return obj.address_line()
