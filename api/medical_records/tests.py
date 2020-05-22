from medical_records.models import Patient

import pytest

from .serializers import PatientSerializer, PatientTableSerializer


@pytest.mark.django_db
def test_patient_serializer_has_expected_fields():
    """Test that PatientSerializer has expected fields"""
    patient = Patient.objects.create(
        first_name="Mary",
        middle_name="Jane",
        last_name="Jones",
        second_last_name="",
        id_document_number="123456789",
        sex="F",
        job_title="Engineer",
        marital_status="SI",
        birthdate="2010-01-01",
        country_of_residence="A",
        address=None,
        phone="+593987878787",
        whatsapp=False,
        health_insurance_company="",
        email="mary@example.com",
        receive_promos=True,
        referral_source="S",
    )
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
    patient = Patient.objects.create(
        first_name="Mary",
        middle_name="Jane",
        last_name="Jones",
        second_last_name="",
        id_document_number="123456789",
        sex="F",
        job_title="Engineer",
        marital_status="SI",
        birthdate="2010-01-01",
        country_of_residence="A",
        address=None,
        phone="+593987878787",
        whatsapp=False,
        health_insurance_company="",
        email="mary@example.com",
        receive_promos=True,
        referral_source="S",
    )
    serializer = PatientTableSerializer(patient)
    data = serializer.data
    assert set(data.keys()) == {
        "key",
        "profile_picture_url",
        "first_name",
        "last_name",
        "id_document_number",
        "birthdate",
        "phone",
        "whatsapp",
        "email",
    }
