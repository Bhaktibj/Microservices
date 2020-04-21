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

HOST_CONFIG = {'AMQP_URI': "amqp://guest:guest@localhost"}
BASE_URL = os.getenv('FUNDOO_API_BASE_URL')
