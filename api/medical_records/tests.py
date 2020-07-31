import datetime

from django.urls import reverse
from django.utils.timezone import make_aware
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

import pytest

from core.factories import MalePatientFactory
from .serializers import PatientSerializer, ValueLabelSerializer


@pytest.fixture
def api_client(admin_user):
    """A fixture for an APIClient with JWT token"""
    client = APIClient()
    refresh = RefreshToken.for_user(admin_user)
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')

    return client


@pytest.mark.django_db
def test_patient_serializer_has_expected_fields():
    """Test that PatientSerializer has expected fields"""
    patient = MalePatientFactory()
    serializer = PatientSerializer(patient)
    data = serializer.data
    assert set(data.keys()) == {
        "key",
        "profile_picture_url",
        "first_name",
        "middle_name",
        "last_name",
        "second_last_name",
        "id_document_number",
        "sex",
        "job_title",
        "marital_status",
        "birthdate",
        "country_of_residence",
        "address",
        "phone",
        "whatsapp",
        "whatsapp_link",
        "health_insurance_company",
        "email",
        "receive_promos",
        "referral_source",
        "emergency_contact",
        "representative",
        "family_history",
        "personal_history",
        "general_practitioners",
        "age",
    }


@pytest.mark.django_db
def test_patient_table_serializer_age(mocker):
    """Test that PatientSerializer returns correct value for age"""
    now_mock = mocker.patch("django.utils.timezone.now")
    now_mock.return_value = make_aware(
        datetime.datetime.strptime("2020-02-01", "%Y-%m-%d")
    )
    patient = MalePatientFactory(birthdate=datetime.date(2010, 1, 1))
    serializer = PatientSerializer(patient)
    assert serializer.data["age"] == 10


@pytest.mark.django_db
def test_patient_table_serializer_whatsapp_link():
    """Test that PatientSerializer returns correct value for whatsapp_link
    when whatsapp is True"""
    patient = MalePatientFactory(phone="+13053991321", whatsapp=True)
    serializer = PatientSerializer(patient)
    assert serializer.data["whatsapp_link"] == "https://wa.me/13053991321"


@pytest.mark.django_db
def test_patient_table_serializer_whatsapp_link_no_whatsapp():
    """Test that PatientSerializer returns correct value for whatsapp_link
    when whatsapp is False"""
    patient = MalePatientFactory(phone="+13053991321", whatsapp=False)
    serializer = PatientSerializer(patient)
    assert serializer.data["whatsapp_link"] is None


def test_value_label_serializer_has_expected_fields():
    """Test that ValueLabelSerializer has expected fields"""
    serializer = ValueLabelSerializer()
    data = serializer.data
    assert set(data.keys()) == {"value", "label"}


@pytest.mark.skip(reason='Too expensive to test')
def test_province_cantons_returns_400_when_no_province(api_client):
    """Tests that 400 response is returned when no province for province_key"""
    url = reverse("cantons_by_province", kwargs={"province_key": 50})
    response = api_client.get(url)

    assert response.status_code == HTTP_400_BAD_REQUEST


@pytest.mark.skip(reason='Too expensive to test')
def test_provice_cantons_are_returned_successfully(api_client):
    """Test that 200 response and cants are returned when province exists"""
    url = reverse("cantons_by_province", kwargs={"province_key": 9})
    response = api_client.get(url)
    data = response.data

    assert response.status_code == HTTP_200_OK
    assert data == [
        {"value": 74, "label": "Isabela"},
        {"value": 75, "label": "San Cristóbal"},
        {"value": 76, "label": "Santa Cruz"},
    ]
