from .common import *  # noqa

# Core
DEBUG = DEBUG_TOOLBAR = True
INSTALLED_APPS += [  # noqa
    "drf_yasg",
]

# Swagger
SWAGGER_SETTINGS = {
    "SECURITY_DEFINITIONS": {
        "Bearer": {"type": "apiKey", "name": "Authorization", "in": "header"}
    },
    "LOGOUT_URL": "/auth/logout",
}

# Setup support for proxy headers
USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")


# Hosting and CORS
CORS_ALLOWED_ORIGINS = ["http://localhost:3000", "https://jhoangv.com"]
