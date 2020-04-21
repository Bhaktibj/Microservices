from sqlalchemy.ext.declarative import DeclarativeMeta

from ...settings import JWT_SECRET_KEY
import jwt


def decode_jwt_token(token):
    """ This method is used to decode the jwt token"""
    try:
        decoded_token = jwt.decode(token, JWT_SECRET_KEY, algorithms=['HS256'])
    except:
        return None  # if invalid data return None
    return decoded_token  # return decode token


import json


class AlchemyEncoder(json.JSONEncoder):
    """ This class is used for serialize the object and return the json response"""

    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            # an SQLAlchemy class
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                data = obj.__getattribute__(field)
                try:
                    json.dumps(data)  # this will fail on non-encodable values, like other classes
                    fields[field] = data
                except TypeError:
                    fields[field] = None
            # a json-encodable dict
            return fields

        return json.JSONEncoder.default(self, obj)


def serialize_data(object):
    """ this method is used for convert object data into json format"""
    serializer_data = json.dumps(object, cls=AlchemyEncoder)
    data = json.loads(serializer_data)  # and loads the data
    return data  # return the data
