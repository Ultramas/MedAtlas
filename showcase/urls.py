from django.urls import path
from django.views.generic import TemplateView

from . import views
from .views import MedAtlasListingView, map_view, ExternalOSMListingsAPI, ExternalHRSAListingsAPI

from .api_views import (
    MedAtlasListingListAPI, MedAtlasListingDetailAPI,
    ExternalOSMListingsAPI, ExternalHRSAListingsAPI,
    ExternalGooglePlacesAPI,
)
app_name = 'showcase'

urlpatterns = [
    path("", MedAtlasListingView.as_view(), name="index"),
    path("components/api-listings/", TemplateView.as_view(template_name="components/api_listings.html"), name="api_listings"),
    path("map/", map_view, name="map"),
    path("listings/", MedAtlasListingListAPI.as_view(), name="listings"),
    path("listings/<int:pk>/", MedAtlasListingDetailAPI.as_view(), name="listing-detail"),
    path("external/listings/osm/", ExternalOSMListingsAPI.as_view(), name="external-osm"),
    path("external/listings/hrsa/", ExternalHRSAListingsAPI.as_view(), name="external-hrsa"),
    path("external/listings/google/", ExternalGooglePlacesAPI.as_view(), name="external-google"),
]
