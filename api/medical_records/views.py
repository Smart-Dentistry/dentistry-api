from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


from .serializers import PatientTableSerializer, PatientSerializer, ValueLabelSerializer
from medical_records.models import Patient
from medical_records.constants import PROVINCES_OF_ECUADOR, CANTONS_OF_ECUADOR, DISEASES


class PatientTableList(ListAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientTableSerializer


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


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
