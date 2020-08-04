from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

import pytest


@pytest.fixture
def api_client(admin_user):
    """A fixture for an APIClient with JWT token"""
    client = APIClient()
    refresh = RefreshToken.for_user(admin_user)
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')

    return client
