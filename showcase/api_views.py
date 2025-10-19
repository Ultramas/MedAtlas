# showcase/api_views.py
from typing import re

from django.db.models import Q
from rest_framework import generics, permissions

from . import views
from .models import MedAtlasListing
from .serializers import MedAtlasListingSerializer
from .views import _split_city_state, _safe, _osm_area_query


class ExternalOSMListingsAPI(views.APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        q = _safe(request.GET.get("q"))
        city, state = _split_city_state(request.GET.get("city"), request.GET.get("state"))

        # Build Overpass query. If city provided, use area search; else global text filter around q
        if city:
            overpass_query = _osm_area_query(city, state)
        else:
            # Fallback: worldwide (heavy); constrain by 'q' in name if provided
            name_filter = f'["name"~"{re.escape(q)}", i]' if q else ""
            overpass_query = f"""
[out:json][timeout:25];
(
  node[amenity~"^(hospital|clinic|doctors|dentist|pharmacy)$"]{name_filter};
  way[amenity~"^(hospital|clinic|doctors|dentist|pharmacy)$"]{name_filter};
  node["healthcare"]{name_filter};
  way["healthcare"]{name_filter};
);
out center tags 100;
"""

        try:
            r = requests.post(OSM_OVERPASS_URL, data={"data": overpass_query}, timeout=25)
            if not r.ok:
                return response.Response({"detail": "Overpass error", "status": r.status_code}, status=r.status_code)
            payload = r.json()
        except Exception as exc:
            return response.Response({"detail": f"Overpass request failed: {exc}"}, status=status.HTTP_502_BAD_GATEWAY)

        elements = payload.get("elements", [])
        normalized = [_map_osm_element(el) for el in elements]

        # Simple pagination (client-like): we’ll page server-side using ?page=
        page = int(_safe(request.GET.get("page")) or "1")
        page_size = int(_safe(request.GET.get("page_size")) or "25")
        start, end = (page - 1) * page_size, (page - 1) * page_size + page_size
        count = len(normalized)
        results = normalized[start:end]

        base = request.build_absolute_uri(request.path)
        query = request.GET.copy()
        def page_link(n):
            qd = query.copy()
            qd["page"] = str(n)
            return f"{base}?{qd.urlencode()}"

        return response.Response({
            "count": count,
            "next": page_link(page + 1) if end < count else None,
            "previous": page_link(page - 1) if page > 1 else None,
            "results": results,
        })

# ---------- EXTERNAL: HRSA ----------
class ExternalHRSAListingsAPI(views.APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        # HRSA Health Center API (see docs index above). One commonly used dataset is their geojson
        # For example, a typical pattern: /resource/geojson?parameters... — the exact resource path is documented on HRSA.
        # We’ll support filters: state=CA or lat/lon/radius (miles).
        state = _safe(request.GET.get("state"))
        lat = _safe(request.GET.get("lat"))
        lon = _safe(request.GET.get("lon"))
        radius_miles = float(_safe(request.GET.get("radius_miles")) or "25")

        # Prefer lat/lon search if provided; else state filter.
        params = {}
        if state:
            # Many HRSA HDW API queries accept 'state' param; consult the linked docs for the exact resource.
            params["state"] = state

        # Example endpoint path below is indicative; you’ll choose the exact HRSA path matching your need from docs.
        # The HDW API provides a health center dataset in GeoJSON.
        endpoint = f"{HRSA_API_BASE}/resource/health-centers.geojson"  # <-- replace with exact documented path

        try:
            # If lat/lon provided, some HRSA endpoints support distance filters; otherwise, filter client-side.
            r = requests.get(endpoint, params=params, timeout=25)
            if not r.ok:
                return response.Response({"detail": "HRSA error", "status": r.status_code}, status=r.status_code)
            payload = r.json()
        except Exception as exc:
            return response.Response({"detail": f"HRSA request failed: {exc}"}, status=status.HTTP_502_BAD_GATEWAY)

        features = payload.get("features", [])
        rows = []
        for f in features:
            item = _map_hrsa_feature(f)
            rows.append(item)

        # Optional radius filter if lat/lon provided
        if lat and lon:
            import math
            la, lo = float(lat), float(lon)
            R = 3958.8  # Earth radius in miles
            def haversine(lat2, lon2):
                if lat2 is None or lon2 is None:
                    return 9e9
                dlat = math.radians(float(lat2) - la)
                dlon = math.radians(float(lon2) - lo)
                a = math.sin(dlat/2)**2 + math.cos(math.radians(la))*math.cos(math.radians(float(lat2)))*math.sin(dlon/2)**2
                return 2*R*math.asin(math.sqrt(a))
            rows = [x for x in rows if haversine(x["latitude"], x["longitude"]) <= radius_miles]

        # Paginate
        page = int(_safe(request.GET.get("page")) or "1")
        page_size = int(_safe(request.GET.get("page_size")) or "25")
        start, end = (page - 1) * page_size, (page - 1) * page_size + page_size
        count = len(rows)
        results = rows[start:end]

        base = request.build_absolute_uri(request.path)
        query = request.GET.copy()
        def page_link(n):
            qd = query.copy()
            qd["page"] = str(n)
            return f"{base}?{qd.urlencode()}"

        return response.Response({
            "count": count,
            "next": page_link(page + 1) if end < count else None,
            "previous": page_link(page - 1) if page > 1 else None,
            "results": results,
        })


class MedAtlasListingListAPI(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = MedAtlasListingSerializer

    def get_queryset(self):
        qs = MedAtlasListing.objects.filter(is_active=True)

        q = (self.request.GET.get("q") or "").strip()
        if q:
            qs = qs.filter(
                Q(name__icontains=q) |
                Q(organization_name__icontains=q) |
                Q(city_text__icontains=q) |
                Q(state__iexact=q)
            )

        city = (self.request.GET.get("city") or "").strip()
        if city:
            qs = qs.filter(city_slug__iexact=city)

        state = (self.request.GET.get("state") or "").strip()
        if state:
            qs = qs.filter(state__iexact=state)

        cost = (self.request.GET.get("cost") or "").strip()
        if cost:
            qs = qs.filter(cost=cost)

        verified = (self.request.GET.get("verified") or "").lower() in {"1", "true", "yes", "on"}
        if verified:
            qs = qs.filter(verified=True)

        services = self.request.GET.getlist("service") or self.request.GET.getlist("services")
        for s in services:
            if s:
                qs = qs.filter(services_csv__icontains=s)

        return qs.only(
            "id", "name", "organization_name",
            "organization_website", "organization_phone",
            "street", "city_text", "state", "postal_code", "country",
            "phone", "website", "city_slug",
            "cost", "verified", "latitude", "longitude"
        )

class MedAtlasListingDetailAPI(generics.RetrieveAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = MedAtlasListingSerializer
    queryset = MedAtlasListing.objects.filter(is_active=True)


# showcase/api_views.py
import time
import requests
from django.conf import settings
from rest_framework import views, response, status, permissions

GOOGLE_PLACES_TEXTSEARCH_URL = "https://maps.googleapis.com/maps/api/place/textsearch/json"

def _norm_google_place(p):
    # Map Google Place result to your card fields
    name = p.get("name") or "Place"
    website = ""  # Text Search doesn't include website; would require Place Details (optional to add later)
    formatted_address = p.get("formatted_address") or ""
    # Try to split address into city/state if present
    city = ""
    state = ""
    try:
        parts = [x.strip() for x in formatted_address.split(",")]
        # naive US parse: "... City, ST ZIP, USA"
        if len(parts) >= 2:
            last_state = parts[-2].split()
            if last_state:
                state = last_state[0] if len(last_state[0]) <= 3 else ""
            # city often sits before state
            city = parts[-3] if len(parts) >= 3 else ""
    except Exception:
        pass

    loc = (p.get("geometry") or {}).get("location") or {}
    lat = loc.get("lat")
    lng = loc.get("lng")

    # cost: unknown — set "varies"
    return {
        "id": f"google:{p.get('place_id')}",
        "name": name,
        "organization_name": "",
        "organization_website": "",
        "organization_phone": "",
        "street": formatted_address,     # we keep full addr here
        "city_text": city,
        "state": state,
        "postal_code": "",
        "country": "",
        "phone": "",
        "website": website,
        "city_slug": "",
        "cost": "varies",
        "cost_label": "Varies",
        "services": [],
        "languages": [],
        "insurance": [],
        "verified": True,  # trusted external data for UI purposes
        "latitude": lat,
        "longitude": lng,
        "address": formatted_address,
        "source": "google_places",
        "source_url": f"https://www.google.com/maps/place/?q=place_id:{p.get('place_id')}",
    }


class ExternalGooglePlacesAPI(views.APIView):
    """
    Proxy to Google Places Text Search (server-side), normalizing results for your UI.
    Supports:
      - q, city, state → combined into query string
      - page_token passthrough for next pages
    """
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        api_key = settings.GOOGLE_PLACES_API_KEY
        if not api_key:
            return response.Response({"detail": "GOOGLE_PLACES_API_KEY not configured"}, status=500)

        q = (request.GET.get("q") or "").strip()
        city = (request.GET.get("city") or "").strip()
        state = (request.GET.get("state") or "").strip()
        # If front-end sends next page token:
        page_token = (request.GET.get("page_token") or "").strip()

        params = {"key": api_key}
        if page_token:
            params["pagetoken"] = page_token
        else:
            # Build a text query like "clinic Sacramento CA"
            query_bits = [q or "clinic"]  # default to 'clinic' if nothing passed
            if city: query_bits.append(city)
            if state: query_bits.append(state)
            params["query"] = " ".join(query_bits)

            # Optionally bias by type(s):
            # params["type"] = "hospital"  # Google Text Search ignores 'type' unless query matches, but we can include

        # IMPORTANT: next_page_token requires a short delay before it becomes valid
        if page_token:
            time.sleep(1.5)

        try:
            r = requests.get(GOOGLE_PLACES_TEXTSEARCH_URL, params=params, timeout=20)
            data = r.json()
        except Exception as exc:
            return response.Response({"detail": f"Google Places request failed: {exc}"}, status=status.HTTP_502_BAD_GATEWAY)

        status_text = data.get("status", "UNKNOWN")
        if status_text not in ("OK", "ZERO_RESULTS"):
            # Common: OVER_QUERY_LIMIT, REQUEST_DENIED, INVALID_REQUEST
            return response.Response({"detail": f"Google Places error: {status_text}", "raw": data}, status=502)

        results = data.get("results", [])
        normalized = [_norm_google_place(p) for p in results]

        # Build pagination with next_page_token if present
        next_token = data.get("next_page_token")
        base = request.build_absolute_uri(request.path)
        qd = request.GET.copy()
        def next_link(token):
            qd2 = qd.copy()
            qd2["page_token"] = token
            # remove numeric page param if present
            qd2.pop("page", None)
            return f"{base}?{qd2.urlencode()}"

        return response.Response({
            "count": None,  # Google doesn't give total count
            "next": next_link(next_token) if next_token else None,
            "previous": None,  # Text Search doesn't support prev tokens; we’ll fake prev in JS via a stack
            "results": normalized,
            "next_page_token": next_token,
        })
