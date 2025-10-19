from rest_framework import generics, response
from rest_framework import permissions
from stripe.http_client import requests

from mysite import views
from django.views.generic import ListView, DetailView, View
from django.db.models import Q
from .models import MedAtlasListing
from .serializers import MedAtlasListingSerializer
from rest_framework.views import APIView

OSM_OVERPASS_URL = "https://overpass-api.de/api/interpreter"  # Public OSM endpoint
HRSA_API_BASE = "https://data.hrsa.gov"

# showcase/api_views.py
import re
import requests
from urllib.parse import urlencode
from django.db.models import Q
from rest_framework import generics, permissions, views, response, status
from .models import MedAtlasListing
from .serializers import MedAtlasListingSerializer

OSM_OVERPASS_URL = "https://overpass-api.de/api/interpreter"  # Public OSM endpoint
HRSA_API_BASE = "https://data.hrsa.gov"                       # HRSA API home (see docs above)

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

class MedAtlasListingView(ListView):
    model = MedAtlasListing
    context_object_name = "listings"
    template_name = "index.html"
    paginate_by = 25  # adjust as needed

    def get_queryset(self):
        qs = MedAtlasListing.objects.filter(is_active=True)

        # Basic text search
        q = self.request.GET.get("q")
        if q:
            qs = qs.filter(
                Q(name__icontains=q) |
                Q(organization_name__icontains=q) |
                Q(city_text__icontains=q) |
                Q(state__iexact=q)
            )

        # Filters
        city = self.request.GET.get("city")
        if city:
            qs = qs.filter(city_slug__iexact=city)

        state = self.request.GET.get("state")
        if state:
            qs = qs.filter(state__iexact=state)

        cost = self.request.GET.get("cost")
        if cost:
            qs = qs.filter(cost=cost)

        verified = self.request.GET.get("verified")
        if verified in {"1", "true", "yes"}:
            qs = qs.filter(verified=True)

        # Naive CSV filtering (simple LIKEs)
        services = self.request.GET.getlist("service") or self.request.GET.getlist("services")
        for s in services:
            if s:
                qs = qs.filter(services_csv__icontains=s)

        # Keep it light in the list page
        return qs.only(
            "id", "name", "organization_name", "city_text", "state",
            "phone", "website", "verified", "cost", "city_slug"
        )

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["filters"] = {
            "q": self.request.GET.get("q", ""),
            "city": self.request.GET.get("city", ""),
            "state": self.request.GET.get("state", ""),
            "cost": self.request.GET.get("cost", ""),
            "verified": self.request.GET.get("verified", ""),
            "services": self.request.GET.getlist("service") or self.request.GET.getlist("services"),
        }
        return ctx


class MedAtlasListingDetailAPI(generics.RetrieveAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = MedAtlasListingSerializer
    queryset = MedAtlasListing.objects.filter(is_active=True)


def _safe(s):
    return (s or "").strip()


def _split_city_state(city, state):
    c, st = _safe(city), _safe(state)
    if (not st) and c and "," in c:
        parts = [p.strip() for p in c.split(",")]
        if len(parts) >= 2 and re.fullmatch(r"[A-Z]{2}", parts[-1]):
            st = parts[-1]
            c = ",".join(parts[:-1]).strip()
    return c, st

def _osm_area_query(city, state):
    """
    Overpass 'area' query to match administrative area by city + optional state,
    then search healthcare amenities within that area.
    """
    # Build admin area search. This prioritizes city name; if state given, narrow by is_in.
    city_clause = f'["name"="{city}"]["boundary"="administrative"]'
    state_clause = f'["name"="{state}"]["boundary"="administrative"]' if state else ""
    # Overpass uses area ids; we derive area via 'area[name=...]["boundary"="administrative"]'
    # We’ll compute a city area; if state provided, inner join by is_in as filter hint.
    q = f"""
[out:json][timeout:25];
area{city_clause}->.cityarea;
(
  node(area.cityarea)[amenity~"^(hospital|clinic|doctors|dentist|pharmacy)$"];
  way(area.cityarea)[amenity~"^(hospital|clinic|doctors|dentist|pharmacy)$"];
  node(area.cityarea)["healthcare"];
  way(area.cityarea)["healthcare"];
);
out center tags;
"""
    # In practice you can further refine with state/region using is_in tags,
    # but the above is a solid general solution for city scope.
    return q

def _map_osm_element(el):
    """Map OSM element to a normalized listing-like dict compatible with your UI."""
    tags = el.get("tags", {})
    lat = el.get("lat") or (el.get("center") or {}).get("lat")
    lon = el.get("lon") or (el.get("center") or {}).get("lon")

    name = tags.get("name") or tags.get("official_name") or "Unnamed facility"
    street = ", ".join(filter(None, [
        tags.get("addr:housenumber"),
        tags.get("addr:street"),
    ])) or tags.get("addr:full") or ""
    city = tags.get("addr:city") or ""
    state = tags.get("addr:state") or ""
    postcode = tags.get("addr:postcode") or ""
    phone = tags.get("phone") or tags.get("contact:phone") or ""
    website = tags.get("website") or tags.get("contact:website") or ""
    org = tags.get("operator") or tags.get("brand")

    # Derive a 'cost' guess (OSM doesn't have cost; default 'varies')
    cost = "varies"

    return {
        "id": f"osm:{el.get('type')}:{el.get('id')}",
        "name": name,
        "organization_name": org or "",
        "organization_website": "",
        "organization_phone": "",
        "street": street,
        "city_text": city,
        "state": state,
        "postal_code": postcode,
        "country": tags.get("addr:country") or "US",
        "phone": phone,
        "website": website,
        "city_slug": "",
        "cost": cost,
        "cost_label": "Varies",
        "services": [],       # Could infer from tags['healthcare'] or 'amenity'
        "languages": [],
        "insurance": [],
        "verified": False,    # not verified by you
        "latitude": lat,
        "longitude": lon,
        "address": ", ".join(filter(None, [street, city, state, postcode])),
        "source": "osm",
        "source_url": f"https://www.openstreetmap.org/{el.get('type')}/{el.get('id')}",
    }

def _map_hrsa_feature(f):
    """Map HRSA response to your normalized schema."""
    # HRSA fields vary by endpoint; common fields include NAME, ADDRESS, CITY, STATE, ZIP, PHONE, LAT, LON, WEBSITE (sometimes)
    props = f.get("properties", {})
    name = props.get("NAME") or props.get("name") or "HRSA Health Center"
    website = props.get("WEBSITE") or props.get("website") or ""
    phone = props.get("PHONE") or props.get("phone") or ""
    lat = props.get("LAT") or props.get("latitude")
    lon = props.get("LON") or props.get("longitude")
    street = props.get("ADDRESS") or ""
    city = props.get("CITY") or ""
    state = props.get("STATE") or ""
    zipc = props.get("ZIP") or ""

    return {
        "id": f"hrsa:{props.get('SITE_ID') or props.get('id') or name}",
        "name": name,
        "organization_name": props.get("ORGANIZATION") or "",
        "organization_website": "",
        "organization_phone": "",
        "street": street,
        "city_text": city,
        "state": state,
        "postal_code": zipc,
        "country": "US",
        "phone": phone,
        "website": website,
        "city_slug": "",
        "cost": "low_cost",          # FQHCs are low/no-cost; use 'low_cost' label
        "cost_label": "Low cost",
        "services": [],
        "languages": [],
        "insurance": [],
        "verified": True,            # Government data; treat as verified for UI purposes
        "latitude": lat,
        "longitude": lon,
        "address": ", ".join(filter(None, [street, city, state, zipc])),
        "source": "hrsa",
        "source_url": "https://findahealthcenter.hrsa.gov/",  # primary portal for these data
    }


# ---------- EXTERNAL: OSM ----------
class ExternalOSMListingsAPI(APIView):
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
class ExternalHRSAListingsAPI(APIView):
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

# showcase/views.py
from django.conf import settings
from django.shortcuts import render
from .models import MedAtlasListing

def map_view(request):
    qs = MedAtlasListing.objects.filter(
        is_active=True,
        latitude__isnull=False,
        longitude__isnull=False,
    ).only("id", "name", "website", "city_text", "state", "latitude", "longitude")[:500]

    points = [
        {
            "id": obj.id,
            "name": obj.name,
            "website": obj.website,
            "city": obj.city_text,
            "state": obj.state,
            "lat": float(obj.latitude),
            "lng": float(obj.longitude),
        }
        for obj in qs
    ]
    return render(request, "map.html", {
        "points": points,
        "GOOGLE_MAPS_API_KEY": settings.GOOGLE_MAPS_API_KEY,
    })
