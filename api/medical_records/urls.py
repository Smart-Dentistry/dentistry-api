from django.urls import path, include
from rest_framework import routers

from .views import PatientViewSet, provinces_of_ecuador

router = routers.SimpleRouter()
router.register(r'patients', PatientViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('provinces-of-ecuador/', provinces_of_ecuador, name='provinces_of_ecuador')
]
