from rest_framework import viewsets
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_201_CREATED
from rest_framework import filters
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


from .serializers import PatientSerializer, ValueLabelSerializer
from medical_records.models import Patient
from medical_records.constants import PROVINCES_OF_ECUADOR, CANTONS_OF_ECUADOR, DISEASES


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['first_name', 'last_name', 'id_document_number']

    @action(detail=True, methods=['post'])
    def create_med_history(self, request, pk=None):
        patient = self.get_object()
        if hasattr(patient, 'medical_background'):
            return Response(status=HTTP_400_BAD_REQUEST)
        # if patient already has med history, return 400 response
        # create MedicalBackground
        # create PeriodontalExam
        # create NonPathologicalBackground
        # create ClinicalExam

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
