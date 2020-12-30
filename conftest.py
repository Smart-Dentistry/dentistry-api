import pytest

from core.factories import MalePatientFactory

@pytest.fixture
def patient():
    return MalePatientFactory()
