import pytest

from medical_records.models import (MedicalBackground,
                                    PeriodontalExam,
                                    NonPathologicalBackground,
                                    ClinicalExam)


@pytest.mark.django_db
def test_has_medical_history_returns_false(patient):
    """Test that property has_medical_history returns False"""
    assert not patient.has_medical_history


@pytest.mark.django_db
def test_has_medical_history_returns_true(patient):
    """Test that property has_medical_history returns True"""
    MedicalBackground.objects.create(patient=patient)
    PeriodontalExam.objects.create(patient=patient)
    NonPathologicalBackground.objects.create(patient=patient)
    ClinicalExam.objects.create(patient=patient)
    patient.refresh_from_db()

    assert patient.has_medical_history
