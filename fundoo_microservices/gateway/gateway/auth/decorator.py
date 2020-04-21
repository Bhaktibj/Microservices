from ..common.utils import *
from ..config.cache_connection import CacheService
cache = CacheService()


def is_authenticated(method):
    def authenticate_user(self, request, **kwargs):
        try:
            print(request.path, type(request.path))
            if request.path not in ['/forgot', '/register', '/login']:
                token = request.headers['token']
                payload = decode_jwt_token(token)
                id_key = payload.get('var')
                token = cache.get_value(id_key)
                cache.set_key("login_id", token)
                if token is None:
                    raise ValueError("You Need To Login First")
                return method(self, request, **kwargs)
            else:
                return method(self, request, **kwargs)
        except jwt.ExpiredSignatureError:
            raise Exception("Signature expired. Please log in again.")
        except jwt.DecodeError:
            raise Exception("Decode error")
    return authenticate_user
