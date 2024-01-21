import sentry_sdk

from config.django.base import INSTALLED_APPS, MIDDLEWARE

# django debug toolbar
################################################################
INTERNAL_IPS = [
    "127.0.0.1",
]

# database settings
################################################################
from .db_config import CONFIG_DATABASES  # noqa

DATABASES = CONFIG_DATABASES
DATABASE_ROUTER = ["config.db_routers.auth_routers"]

# install apps
################################################################
INSTALLED_APPS += [
    "rosetta",
    "debug_toolbar",
    "rest_framework_swagger",
    "drf_yasg",
]

# middlewares
################################################################
MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]

# sentry config
################################################################
# todo: active sentry
# sentry_sdk.init(
#     dsn=env("DSN"),
#     traces_sample_rate=1.0,
#     profiles_sample_rate=1.0,
# )
