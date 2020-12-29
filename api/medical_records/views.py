from rest_framework import viewsets
from rest_framework import response
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_201_CREATED
from rest_framework import filters
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


from .serializers import PatientSerializer, ValueLabelSerializer
from medical_records.models import Patient, MedicalBackground, PeriodontalExam, NonPathologicalBackground, ClinicalExam
from medical_records.constants import PROVINCES_OF_ECUADOR, CANTONS_OF_ECUADOR, DISEASES


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['first_name', 'last_name', 'id_document_number']

    @action(detail=True, methods=['post'])
    def create_med_history(self, request, pk=None):
        patient = self.get_object()
        fields = ['medical_background', 'periodontal_exam', 'non_pathological_background', 'clinical_exam']
        if any(hasattr(patient, field) for field in fields):
            return Response(
                {'error': "Patient has already medical history"},
                status=HTTP_400_BAD_REQUEST
            )
        data = request.data
        patient.first_appointment_reason = data['appointment_reason']
        patient.save()
        MedicalBackground.objects.create(
            patient=patient,
            family_history=data['family_history'],
            personal_history=data['personal_history'],
            general_practitioners=data['general_practitioners']
        )
        PeriodontalExam.objects.create(
            patient=patient,
            **data['periodontal_exam']
        )
        NonPathologicalBackground.objects.create(
            patient=patient,
            **data['non_pathological_background']
        )
        ClinicalExam.objects.create(
            patient=patient,
            **data['clinical_exam']
        )

        return Response(status=HTTP_201_CREATED)


@swagger_auto_schema(method="get", responses={200: ValueLabelSerializer(many=True)})
@api_view()
def provinces_of_ecuador(request):
    return Response(PROVINCES_OF_ECUADOR)


province_key = openapi.Parameter(
    "province_key", openapi.IN_PATH, type=openapi.TYPE_INTEGER, required=True
)


@swagger_auto_schema(
    method="get",
    manual_parameters=[province_key],
    responses={200: ValueLabelSerializer(many=True)},
)
@api_view()
def cantons_by_province(request, province_key=None):
    try:
        cantons = CANTONS_OF_ECUADOR[province_key]
    except KeyError:
        return Response(status=HTTP_400_BAD_REQUEST)

    return Response(cantons)


@swagger_auto_schema(method="get", responses={200: ValueLabelSerializer(many=True)})
@api_view()
def diseases(request):
    return Response(DISEASES)
