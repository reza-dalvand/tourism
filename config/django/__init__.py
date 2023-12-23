from split_settings.tools import include

from config.django.base import DEBUG

include("secret.py")
include("base.py")
include("email.py")

if DEBUG:
    include("local.py")
else:
    include("production.py")
