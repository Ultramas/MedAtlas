# showcase/api_urls.py
from django.urls import path
from .api_views import (
    MedAtlasListingListAPI, MedAtlasListingDetailAPI,   # your existing internal APIs
    ExternalOSMListingsAPI, ExternalHRSAListingsAPI,     # if you keep them
    ExternalGooglePlacesAPI,                             # NEW
)


urlpatterns = [
    path("listings/", MedAtlasListingListAPI.as_view(), name="listings"),
    path("listings/<int:pk>/", MedAtlasListingDetailAPI.as_view(), name="listing-detail"),
    path("external/listings/osm/", ExternalOSMListingsAPI.as_view(), name="external-osm"),
    path("external/listings/hrsa/", ExternalHRSAListingsAPI.as_view(), name="external-hrsa"),

    # NEW: Google Places Text Search
    path("external/listings/google/", ExternalGooglePlacesAPI.as_view(), name="external-google"),
]
