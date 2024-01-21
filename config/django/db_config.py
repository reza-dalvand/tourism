from config.django.base import BASE_DIR

CONFIG_DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    },
    "users": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "users_db.sqlite3",
    },
}
