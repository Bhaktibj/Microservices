from dotenv import load_dotenv

load_dotenv()
import os

MYSQL_DB_CONFIG = {
    "user": os.getenv('FUNDOO_USERS_MYSQL_DB_USERNAME'),
    "password": os.getenv('FUNDOO_USERS_MYSQL_DB_PASSWORD'),
    "host": os.getenv('FUNDOO_USERS_MYSQL_DB_HOST'),
    "db_name": os.getenv("FUNDOO_USERS_MYSQL_DB_NAME"),
    "port": int(os.getenv("FUNDOD_USERS_MYSQL_DB_PORT"))
}

USER_PASSWORD_SECURITY_SALT = os.getenv('FUNDOO_USER_PASSWORD_SECURITY_SALT')
JWT_SECRET_KEY = os.getenv('FUNDOO_USERS_JWT_SECRET_KEY')

CACHE = {
    "host": os.getenv('FUNDOO_USERS_REDIS_CACHE_HOST'),
    "port": os.getenv('FUNDOO_USERS_REDIS_CACHE_PORT'),
    "password": os.getenv('FUNDOO_USERS_REDIS_CACHE_PASSWORD'),
    "db": 0
}


#  email setting
EMAIL_HOST = os.getenv('FUNDOO_USERS_EMAIL_HOST')
EMAIL_PORT = os.getenv('FUNDOO_USERS_EMAIL_PORT')
EMAIL_HOST_USERNAME = os.getenv('FUNDOO_USERS_EMAIL_HOST_USERNAME')
EMAIL_HOST_PASSWORD = os.getenv('FUNDOO_USERS_EMAIL_HOST_PASSWORD')

# password reset
HOST_LINK = os.getenv('FUNDOO_USERS_HOST_LINK')