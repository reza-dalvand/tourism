from config.django.env_file import BASE_DIR

CONFIG_DATABASES = {
    "default": {},
    "custom_db": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "custom.db.sqlite3",
    },
    # "custom_db": {
    #     "ENGINE": "django.db.backends.postgresql",
    #     "NAME": env("DB_NAME"),
    #     "USER": env("DB_USER"),
    #     "PASSWORD": env("DB_PASSWORD"),
    #     "HOST": env("DB_HOST"),
    #     "PORT": env("DB_PORT"),
    # },
}
