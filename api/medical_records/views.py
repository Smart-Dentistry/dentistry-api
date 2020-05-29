from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

from .serializers import PatientTableSerializer, PatientSerializer
from medical_records.models import Patient
from medical_records.constants import PROVINCES_OF_ECUADOR


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    @swagger_auto_schema(responses={200: PatientTableSerializer(many=True)})
    def list(self, request):
        queryset = Patient.objects.all()
        serializer = PatientTableSerializer(queryset, many=True)
        return Response(serializer.data)


@api_view()
def provinces_of_ecuador(request):
    return Response(PROVINCES_OF_ECUADOR)
