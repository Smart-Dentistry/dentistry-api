from rest_framework import viewsets

from .serializers import PatientSerializer
from medical_records.models import Patient


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
