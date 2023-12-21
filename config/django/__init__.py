import os

from split_settings.tools import include

include("secret.py")
include("base.py")
include("email.py")

if os.environ.get("DEBUG"):
    include("local.py")
include("production.py")
