import pytest

from core.factories import UserFactory
from .serializers import UserSerializer


@pytest.mark.django_db
def test_user_serializer_has_expected_fields():
    '''Test that UserSerializer has expected fields'''
    user = UserFactory(username="user", password="password123", email="user@gmail.com")
    serializer = UserSerializer(user)
    data = serializer.data
    assert set(data.keys()) == {'id', 'username', 'email'}
