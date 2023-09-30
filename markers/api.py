# markers/api.py

# plugins
from rest_framework import routers

# local
from markers.viewsets import MarkerViewSet, AreaViewSet, MultiareaViewSet, MultilineViewSet

router = routers.DefaultRouter()
router.register(r"markers", MarkerViewSet)
router.register(r"areas", AreaViewSet)
router.register(r"multiareas", MultiareaViewSet)
router.register(r"multilines", MultilineViewSet)

urlpatterns = router.urls
