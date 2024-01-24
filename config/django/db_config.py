from config.django.base import BASE_DIR

CONFIG_DATABASES = {
    "default": {},
    "users_db": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "users.db.sqlite3",
    },
}
