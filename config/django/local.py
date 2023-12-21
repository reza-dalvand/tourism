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
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)
