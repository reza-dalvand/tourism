import os
from pathlib import Path

# todo: import base dir instead make again path in below line
LOGGING_DIR = Path(__file__).resolve().parent.parent.parent
if not os.path.exists(LOGGING_DIR):
    os.makedirs(LOGGING_DIR)

# config format of handlers
########################################################################
LOGGING_FORMAT = "%(asctime)s [%(levelname)s] [%(name)s] - %(message)s"
LOGGING_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

# config maximum size and backup count
########################################################################
MAXIMUM_FILE_LOGS = 1024 * 1024 * 5  # 5 MB
BACKUP_COUNT = 5

# logger configuration
########################################################################


LOGGING = {
    "version": 1,
    "disable_existing_logger": True,
    "formatters": {
        "verbose": {
            "format": LOGGING_FORMAT,
            "datefmt": LOGGING_DATE_FORMAT,
        },
        "simple": {
            "format": "%(levelname)s %(message)s",
        },
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
        "file": {
            "level": "WARNING",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": os.path.join(LOGGING_DIR, "log_file.log"),
            "formatter": "verbose",
            "maxBytes": MAXIMUM_FILE_LOGS,
            "backupCount": BACKUP_COUNT,
        },
        "mail_admins": {
            "level": "ERROR",
            "class": "django.utils.log.AdminEmailHandler",
            "email_backend": "django.core.mail.backends.smtp.EmailBackend",
        },
    },
    "loggers": {
        "main": {
            "handlers": ["console", "file", "mail_admins"],
            "level": "DEBUG",
            "propagate": True,
        },
    },
}