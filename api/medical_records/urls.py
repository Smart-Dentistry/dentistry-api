from django.urls import path, include
from rest_framework import routers

from .views import (
    PatientViewSet,
    provinces_of_ecuador,
    cantons_by_province,
    diseases,
    PatientTableList,
)

router = routers.SimpleRouter()
router.register(r"patients", PatientViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("patients-table/", PatientTableList.as_view(), name="patients-table"),
    path("provinces-of-ecuador/", provinces_of_ecuador, name="provinces_of_ecuador"),
    path(
        "provinces-of-ecuador/<int:province_key>/cantons/",
        cantons_by_province,
        name="cantons_by_province",
    ),
    path("diseases/", diseases, name="diseases"),
]
