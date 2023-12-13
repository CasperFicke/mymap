# mymap/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  # admin
  path('admin/', admin.site.urls),
  # apps
  path(''      , include('site_basis.urls', namespace="site-basis")),
  path(''      , include("markers.urls")),
  path(''      , include("stations.urls")),
  # api
  path('api/'  , include("markers.api")),
]

if settings.DEBUG:
  urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # url compositie voor externe toegang tot staticfiles
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)   # url compositie voor externe toegang tot mediafiles

# Configure Admin area Titles
admin.site.site_header = "Admin area"      # header op admin pagina (blauwe balk)
admin.site.index_title = "Admin van alles" # koptekst op admin pagina en 1e deel in browsertab title
admin.site.site_title  = "My Map"          # toevoeging (2e deel) in browsertab title