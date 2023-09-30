# mymap/urls.py

from django.contrib import admin
from django.urls import path, include

from markers.views import MarkersMapView

urlpatterns = [
  # admin
  path('admin/'    , admin.site.urls),
  # apps
  path(''          , include('site_basis.urls', namespace="site-basis")),
  path("markers/"  , include("markers.urls")),
  path("stations/" , include("stations.urls")),
  # api
  path("api/"      , include("markers.api")),
]

# Configure Admin area Titles
admin.site.site_header = "Admin area"      # header op admin pagina (blauwe balk)
admin.site.index_title = "Admin van alles" # koptekst op admin pagina en 1e deel in browsertab title
admin.site.site_title  = "My Map"          # toevoeging (2e deel) in browsertab title