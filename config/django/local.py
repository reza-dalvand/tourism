import sentry_sdk

from config.django.base import BASE_DIR, INSTALLED_APPS
from config.env import env

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
INSTALLED_APPS += ["rosetta"]


# sentry config
################################################################
sentry_sdk.init(
    dsn=env("DSN"),
    traces_sample_rate=1.0,
    profiles_sample_rate=1.0,
)
