import redis
from ...settings import CACHE
import logging

class CacheService:
    """ This cache service class is to store the data into cache"""

    def __init__(self):
        self.connect = self.connect()  # initialize the connect method & create obj

    def connect(self):
        """ this method is used connect the cache server"""
        try:
            connection = redis.Redis(host=CACHE.get('host'), port=CACHE.get('port'), password=CACHE.get('password'),
                                     db=CACHE.get('db'), decode_responses=True)  # create redis cache connection using extra args
            logging.debug(connection)
            logging.info("====================> cache is connected: {}".format(connection))
            return connection  # return the connection
        except:
            logging.error("something went wrong - in cache connection")
            return False  # it returns false

    def set_key(self, key, value):
        """ this method is used to set the key and value in cache"""
        if key and value is not None:  # if key is valid it set the value
            self.connect.set(key, value)
            return True  # it returns true
        else:
            return False

    def get_value(self, key):
        """ this method is used get the key value from cache"""
        value = self.connect.get(key)  # pass to cache get()
        if value:
            return value  # it returns value
        else:
            return None  # if key is not found

    def delete(self, key):
        """ this method is used to delete the key-value from cache using key"""
        self.connect.delete(key)  # if key is found the it delete using cache get method
        return True  # it returns True

    def set_dict_key(self, dict_key, dict):
        """ this method is used to store the dict value in cache using key"""
        if dict_key and dict is not None:
            self.connect.hmset(dict_key, dict)
            return True
        else:
            return False

    def get_dict_value(self, key):
        """ this method is used get the dict_value from cache using key"""
        data = self.connect.hgetall(key)
        if data:
            return data  # if data is then return else None
        else:
            return None

# cache = CacheService()
# cache.set_key(key=None, value="hiiyg")
# cache.get_value('8')
# cache.delete('9')
