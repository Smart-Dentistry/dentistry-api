from datetime import datetime

from django.utils.timezone import make_aware

import pytest

from core.factories import MalePatientFactory
from .serializers import PatientSerializer, PatientTableSerializer


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
        "health_insurance_company",
        "email",
        "receive_promos",
        "referral_source",
        "emergency_contact",
        "representative",
        "family_history",
        "personal_history",
        "general_practitioners",
    }


@pytest.mark.django_db
def test_patient_table_serializer_has_expected_fields():
    """Test that PatientTableSerializer has expected fields"""
    patient = MalePatientFactory()
    serializer = PatientTableSerializer(patient)
    data = serializer.data
    assert set(data.keys()) == {
        "key",
        "profile_picture_url",
        "first_name",
        "last_name",
        "id_document_number",
        "phone",
        "whatsapp",
        "email",
        "age",
    }


@pytest.mark.django_db
def test_patient_table_serializer_age(mocker):
    """Test that PatientTableSerializer returns correct value for age"""
    now_mock = mocker.patch("django.utils.timezone.now")
    now_mock.return_value = make_aware(datetime.strptime("2020-02-01", "%Y-%m-%d"))
    patient = MalePatientFactory(
        birthdate=make_aware(datetime.strptime("2010-01-01", "%Y-%m-%d")).date()
    )
    serializer = PatientTableSerializer(patient)
    assert serializer.data["age"] == 10
