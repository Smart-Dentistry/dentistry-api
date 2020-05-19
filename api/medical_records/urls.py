from rest_framework import routers

from .views import PatientViewSet

router = routers.SimpleRouter()
router.register(r'patients', PatientViewSet)

urlpatterns = router.urls
