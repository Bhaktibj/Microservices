from common.utils import decode_jwt_token
from flask import request
from config.cache_connection import CacheService
import jwt
import logging
cache = CacheService()


def is_authenticated(method):
    """This method is provide the security authentication"""
    def authenticate_user(self, **kwargs):
        try:
            print(request.path, type(request.path))
            if request.path not in ['/forgot', '/register', '/login']:  # except login , forgot and register
                try:
                    token = request.headers['token']  # get token from header
                    payload = decode_jwt_token(token)  # decode jwt token and return payload
                    if payload is not None:  # check payload is not None or None
                        id_key = payload.get('var')  # if not None
                        token = cache.get_value(id_key)  # return id and check in cache id_key is in cache
                        if token is None:  # if token None
                            raise ValueError("You Need To Login First")  # return value error
                        return method(self, **kwargs) # else return authenticate user
                    else:
                        return {"message": "token is invalid, please check"} # else token is invalid
                except KeyError:
                    logging.error('You need to login first')
                    return {"message": "You need to login first, please "}
            else:
                return method(self, **kwargs)
        except jwt.DecodeError:
            raise Exception("Decode error")
    return authenticate_user
