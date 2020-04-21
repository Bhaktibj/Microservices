import json
from functools import wraps
from werkzeug.wrappers import Response
import jwt
from ...settings import *


def json_response(data, message, status):
    response = json.dumps({"data": data, "message": message, "status": status})
    return Response(response=response, content_type="application/json", status=status)


def preprocess_request(f):
    @wraps(f)
    def wrap(self, *args, **kwargs):
        if args[0].method == 'GET':
            request = kwargs
        else:
            request = json.loads(args[0].data)
        return f(self, request)

    return wrap


def create_jwt_token(var):
    """ This method is used to create jwt token"""
    try:
        payload = {'var': var}
        encoded_token = jwt.encode(payload, JWT_SECRET_KEY, 'HS256').decode('utf-8')
    except:
        return None  # if invalid data return None
    return encoded_token  # return encoded token


def decode_jwt_token(token):
    """ This method is used to decode the jwt token"""
    try:
        decoded_token = jwt.decode(token, JWT_SECRET_KEY, algorithms=['HS256'])
    except:
        return None  # if invalid data return None
    return decoded_token  # return decode token


def json_data(request):
    """ This method is used to convert the dictionary"""
    request_data = json.loads(request.get_data(as_text=True))
    return request_data
