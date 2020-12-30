import datetime

from django.urls import reverse
from django.utils.timezone import make_aware
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK, HTTP_201_CREATED

import pytest

from medical_records.models import PeriodontalExam
from core.factories import MalePatientFactory
from .serializers import PatientSerializer, ValueLabelSerializer



@pytest.mark.django_db
def test_patient_serializer_has_expected_fields(patient):
    """Test that PatientSerializer has expected fields"""
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
        "age",
        "has_medical_history"
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


def test_province_cantons_returns_400_when_no_province(api_client):
    """Tests that 400 response is returned when no province for province_key"""
    url = reverse("cantons_by_province", kwargs={"province_key": 50})
    response = api_client.get(url)

    assert response.status_code == HTTP_400_BAD_REQUEST


def test_provice_cantons_are_returned_successfully(api_client):
    """Test that 200 response and cantons are returned when province exists"""
    url = reverse("cantons_by_province", kwargs={"province_key": 9})
    response = api_client.get(url)
    data = response.data

    assert response.status_code == HTTP_200_OK
    assert data == [
        {"value": 74, "label": "Isabela"},
        {"value": 75, "label": "San Cristóbal"},
        {"value": 76, "label": "Santa Cruz"},
    ]


def test_provices_are_returned_successfully(api_client):
    """Test that 200 response and provinces are returned"""
    url = reverse("provinces_of_ecuador")
    response = api_client.get(url)
    data = response.data

    assert response.status_code == HTTP_200_OK
    assert {"value": 8, "label": "Esmeraldas"} in data
    assert {"value": 9, "label": "Galápagos"} in data


def test_diseases_are_returned_successfully(api_client):
    """Test that 200 response and diseases are returned"""
    url = reverse("diseases")
    response = api_client.get(url)
    data = response.data

    assert response.status_code == HTTP_200_OK
    assert {"value": 2, "label": "Hypertension"} in data
    assert {"value": 3, "label": "Cardiovascular disease"} in data


@pytest.mark.django_db
def test_patient_med_record_is_created_successfully(patient, api_client):
    """Test that medical history for a patient is created successfully"""
    url = reverse('patient-create-med-history', kwargs={"pk": patient.pk})
    data = {
        "appointmentReason": "This is silly",
        "familyHistory": {
            "diseases": [
                {
                    "id": 12,
                    "label": "Drinker",
                    "relatives": ["M", "F", "S"]
            }
        ],
        "observations": "This is a good guy."
        },
        "personalHistory": {
            "diseases": [1, 5],
            "observations": "This doesn't look good."
        },
        "generalPractitioners": [
            {
                "name": "Luis M Vargas",
                "phone": "+13053991321",
                "specialization": "Scientist",
                "observations": "This is a great guy."
            }
        ],
        "clinicalExam": {
            "extraoralExam": "ABCD",
            "intraoralExam": "XYZ"
        },
        "periodontalExam": {
            "dentalPlaque": True,
            "calculus": False,
            "bleeding": True,
            "toothMobility": False
        },
        "nonPathologicalBackground": {
            "mouthwash": True,
            "floss": True,
            "brushingFrequency": 3
        }
    }
    response = api_client.post(url, data,  format='json')
    patient.refresh_from_db()

    assert response.status_code == HTTP_201_CREATED
    assert hasattr(patient, 'medical_background')
    assert hasattr(patient, 'periodontal_exam')
    assert hasattr(patient, 'non_pathological_background')
    assert hasattr(patient, 'clinical_exam')
    

@pytest.mark.django_db
def test_patient_med_record_is_not_created_when_patient_already_has_it(patient, api_client):
    """Test that medical history for a patient is not created when patient
    already has medical history"""
    PeriodontalExam.objects.create(patient=patient)
    url = reverse('patient-create-med-history', kwargs={"pk": patient.pk})
    response = api_client.post(url, {},  format='json')
    
    assert response.status_code == HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_400_response_when_patient_has_no_medical_history(patient, api_client):
    """Test that 400 status code is returned when patient has no medical history"""
    url = reverse('patient-get-med-history', kwargs={"pk": patient.pk})
    response = api_client.get(url)

    assert response.status_code == HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_200_and_med_history_when_patient_has_medical_history(patient, api_client):
    """Test that 200 status code and medical history JSON is returned when patient
    has medical history"""
    url = reverse('patient-create-med-history', kwargs={"pk": patient.pk})
    data = {
        "appointmentReason": "This is silly",
        "familyHistory": {
            "diseases": [
                {
                    "id": 12,
                    "label": "Drinker",
                    "relatives": ["M", "F", "S"]
            }
        ],
        "observations": "This is a good guy."
        },
        "personalHistory": {
            "diseases": [1, 5],
            "observations": "This doesn't look good."
        },
        "generalPractitioners": [
            {
                "name": "Luis M Vargas",
                "phone": "+13053991321",
                "specialization": "Scientist",
                "observations": "This is a great guy."
            }
        ],
        "clinicalExam": {
            "extraoralExam": "ABCD",
            "intraoralExam": "XYZ"
        },
        "periodontalExam": {
            "dentalPlaque": True,
            "calculus": False,
            "bleeding": True,
            "toothMobility": False
        },
        "nonPathologicalBackground": {
            "mouthwash": True,
            "floss": True,
            "brushingFrequency": 3
        }
    }
    api_client.post(url, data,  format='json')
    url = reverse('patient-get-med-history', kwargs={"pk": patient.pk})
    response = api_client.get(url)
    patient.refresh_from_db()
    data = response.data

    assert response.status_code == HTTP_200_OK
    assert 'appointment_reason' in data
    assert 'family_history' in data
    assert 'personal_history' in data
    assert 'general_practitioners' in data
    assert 'clinical_exam' in data
    assert 'periodontal_exam' in data
    assert 'non_pathological_background' in data
