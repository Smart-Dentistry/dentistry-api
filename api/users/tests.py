from django.contrib.auth import get_user_model

import pytest

from .serializers import UserSerializer

User = get_user_model()


@pytest.mark.django_db
def test_user_serializer_has_expected_fields():
    '''Test that UserSerializer has expected fields'''
    user = User.objects.create_user(
        username="user", password="password123", email="user@gmail.com"
    )
    serializer = UserSerializer(user)
    data = serializer.data
    assert set(data.keys()) == {'id', 'username', 'email'}
