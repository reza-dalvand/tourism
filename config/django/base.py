import logging.config
from pathlib import Path

from django.utils.translation import gettext_lazy as _

from config.env import env
from config.settings.logger import LOGGING

BASE_DIR = Path(__file__).resolve().parent.parent.parent

DEBUG = env("DEBUG", cast=bool, default=False)

# which domain/host access to website (security)
################################################################
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=["*"])

# which domains can send request to website
################################################################
CORS_ORIGIN_WHITELIST = env.list("CORS_ORIGIN_WHITELIST", default=[])

# logger configuration
################################################################
logging.config.dictConfig(LOGGING)

# all apps
################################################################
DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

LOCAL_APPS = [
    "apps.users",
]

THIRD_PARTY_APPS = [
    "rest_framework",
    "corsheaders",
]

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS

# middlewares
################################################################
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",  # new
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "apps.core.middlewares.current_user.CurrentUserMiddleware",
]

# root url
################################################################
ROOT_URLCONF = "config.urls"

# templates
################################################################
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

# password validator
################################################################
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# rest configuration
################################################################
REST_FRAMEWORK = {
    "DEFAULT_VERSIONING_CLASS": "rest_framework.versioning.URLPathVersioning",
    "ALLOWED_VERSIONS": ["v1"],
    "DEFAULT_VERSION": "v1",
}

# language settings
################################################################
LANGUAGE_CODE = "en"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGES = (
    ("en", _("English")),
    ("fa", _("فارسی")),
)

LOCALE_PATHS = [
    BASE_DIR / "locale/",
]

# serve static and media files
################################################################
STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "static"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# default auto field
################################################################
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# config default user model
################################################################
AUTH_USER_MODEL = "users.User"
