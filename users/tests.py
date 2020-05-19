import pytest

from core.factories import UserFactory


@pytest.mark.django_db
def test_user_string_representation():
    """Tests that User's string representation is
    properly returned"""
    user = UserFactory(username='john', email='john@example.com')

    assert str(user) == 'john - john@example.com'
