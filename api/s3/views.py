from django.conf import settings
from django.utils.timezone import now
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST

import boto3
from botocore.exceptions import ClientError


# The following code has been taken from:
# https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-presigned-urls.html#generating-a-presigned-url-to-upload-a-file
def create_presigned_post(
    bucket_name, object_name, fields=None, conditions=None, expiration=3600
):
    """Generate a presigned URL S3 POST request to upload a file

    :param bucket_name: string
    :param object_name: string
    :param fields: Dictionary of prefilled form fields
    :param conditions: List of conditions to include in the policy
    :param expiration: Time in seconds for the presigned URL to remain valid
    :return: Dictionary with the following keys:
        url: URL to post to
        fields: Dictionary of form fields and values to submit with the POST
    :return: None if error.
    """

    # Generate a presigned S3 POST URL
    s3_client = boto3.client("s3")
    response = s3_client.generate_presigned_post(
        bucket_name,
        object_name,
        Fields=fields,
        Conditions=conditions,
        ExpiresIn=expiration,
    )

    # The response contains the presigned URL and required fields
    return response


@api_view()
def get_presigned_url(request):
    try:
        response = create_presigned_post(
            settings.AWS_STORAGE_BUCKET_NAME, f"{now()}-filename"
        )
    except ClientError:
        return Response(status=HTTP_400_BAD_REQUEST)

    return Response(response)
