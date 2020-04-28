from flaskapp_env import Config
from config_logger import configure_logging
configure_logging()
config = Config
CACHE = {
    "host": config.FUNDOO_REDIS_CACHE_HOST,
    "port": config.FUNDOO_REDIS_CACHE_PORT,
    "password": config.FUNDOO_REDIS_CACHE_PASSWORD,
    "db": 0
}

JWT_SECRET_KEY = config.FUNDOO_USERS_JWT_SECRET_KEY

HOST_CONFIG = config.AMQP_URI
BASE_URL = config.API_BASE_URL
