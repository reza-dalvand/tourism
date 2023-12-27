import sentry_sdk

from config.django.base import BASE_DIR, INSTALLED_APPS, MIDDLEWARE
from config.env import env

# django debug toolbar
################################################################
INTERNAL_IPS = [
    "127.0.0.1",
]

# database settings
################################################################
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# install apps
################################################################
INSTALLED_APPS += [
    "rosetta",
    "debug_toolbar",
]

# middlewares
################################################################
MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]

# sentry config
################################################################
sentry_sdk.init(
    dsn=env("DSN"),
    traces_sample_rate=1.0,
    profiles_sample_rate=1.0,
)
