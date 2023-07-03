from storages.backends.s3boto3 import S3Boto3Storage
from django.conf import settings
from django.core.files.storage import FileSystemStorage


class StaticStorage(S3Boto3Storage):
    """S3 storage backend for serving statics on S3."""

    location = "static"
    default_acl = "public-read"


class PublicMediaStorage(S3Boto3Storage):
    """S3 storage backend for serving media on S3."""

    location = "media"
    # default_acl = 'public-read'
    file_overwrite = False


class PrivateMediaStorage(S3Boto3Storage):
    """S3 storage backend for serving private media on S3."""

    location = "media/private"
    default_acl = "private"
    file_overwrite = False
    custom_domain = False


# This is the store to store private media files
# at the local or environment which is not support remove (S3)
# we can force to use the default = FileStorage instead of hard code to the models.FileField
private_storage = FileSystemStorage()

if settings.USE_S3 is True:
    private_storage = PrivateMediaStorage()
