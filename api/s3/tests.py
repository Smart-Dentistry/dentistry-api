from django.urls import reverse
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK

from botocore.exceptions import ClientError


def test_400_response_is_return_when_client_error_getting_presigned_url(api_client, mocker):
    """Test that 400 response is obtained when getting ClientError while trying to get
    a presigned URL for posting to S3"""
    error_response = {'Error': {}}
    mocker.patch(
        "api.s3.views.create_presigned_post",
        side_effect=ClientError(error_response, 'error')
    )
    url = reverse('get_presigned_url')
    response = api_client.get(url, {'Key': 'key', 'ContentType': 'ct'})

    assert response.status_code == HTTP_400_BAD_REQUEST


def test_200_response_is_return_requesting_presigned_url(api_client, mocker):
    """Test that 200 response is obtained when requesting presigned URL for
    posting to S3"""
    mocker.patch("api.s3.views.create_presigned_post")
    url = reverse('get_presigned_url')
    response = api_client.get(url, {'Key': 'key', 'ContentType': 'ct'})

    assert response.status_code == HTTP_200_OK
