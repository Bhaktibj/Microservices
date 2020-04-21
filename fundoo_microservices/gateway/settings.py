import os
from dotenv import load_dotenv
load_dotenv()
CACHE = {
    "host": os.getenv('FUNDOO_USERS_REDIS_CACHE_HOST'),
    "port": os.getenv('FUNDOO_USERS_REDIS_CACHE_PORT'),
    "password": os.getenv('FUNDOO_GATEWAY_REDIS_CACHE_PASSWORD'),
    "db": 0
}

JWT_SECRET_KEY = os.getenv('FUNDOO_USERS_JWT_SECRET_KEY')