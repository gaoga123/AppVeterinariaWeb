from rest_framework import routers

from .viewsets import ReseniaRestApiViewSet

router = routers.SimpleRouter()
router.register("reseniarestapi", ReseniaRestApiViewSet)

urlpatterns = router.urls
