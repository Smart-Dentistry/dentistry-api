from django.contrib.auth import get_user_model

import pytest


User = get_user_model()


@pytest.mark.django_db
def test_user_string_representation():
    """Tests that User's string representation is
    properly returned"""
    user = User.objects.create_user(
        username='john',
        email='john@example.com'
    )

    assert str(user) == 'john - john@example.com'
