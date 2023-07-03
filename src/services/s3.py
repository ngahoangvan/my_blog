import os
import boto3

from botocore.config import Config
from botocore.exceptions import ClientError


class S3:
    def __init__(self):
        self.s3_client = boto3.client(
            "s3",
            os.environ.get("AWS_REGION"),
            endpoint_url=os.environ.ge("AWS_S3_ENDPOINT_URL"),
            aws_access_key_id=os.environ.ge("AWS_ACCESS_KEY_ID"),
            aws_secret_access_key=os.environ.ge("AWS_SECRET_ACCESS_KEY"),
            config=Config(signature_version="s3v4"),
        )

    def generate_presigned_url(self, client_method, key):
        try:
            url = self.s3_client.generate_presigned_url(
                client_method,
                Params={
                    "Bucket": os.environ.ge("AWS_STORAGE_BUCKET_NAME"),
                    "Key": key,
                },
                ExpiresIn=36000,
            )
        except ClientError:
            return "Could not get a presigned URL"

        return url
