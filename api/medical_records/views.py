from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import PatientTableSerializer, PatientSerializer
from medical_records.models import Patient


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    def list(self, request):
        queryset = Patient.objects.all()
        serializer = PatientTableSerializer(queryset, many=True)
        return Response(serializer.data)
