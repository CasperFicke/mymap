# markers/api.py

# plugins
from rest_framework import routers

# local
from markers.viewsets import MarkerViewSet, AreaViewSet, MultiareaViewSet, MultilineViewSet

router = routers.DefaultRouter()
router.register(r"markers/v1", MarkerViewSet)
router.register(r"areas/v1", AreaViewSet)
router.register(r"multiareas/v1", MultiareaViewSet)
router.register(r"multilines/v1", MultilineViewSet)

urlpatterns = router.urls
