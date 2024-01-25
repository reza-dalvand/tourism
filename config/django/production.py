from config.settings import aws  # noqa

# database configuration
################################################################
from .db_config import CONFIG_DATABASES  # noqa

DATABASES = CONFIG_DATABASES
DATABASE_ROUTERS = ["config.db_routers.auth_router.AuthRouter"]
