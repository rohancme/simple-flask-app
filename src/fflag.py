import os
import redis
import ConfigParser
from redis.exceptions import ConnectionError


class FeatureFlag():

    def __init__(self, test=False):
        if not test:
            if not self.__read_config_file('./feature-flag.ini'):
                raise IOError('Please check your FF configuration')
            else:
                self._redis_client = FeatureFlag._init_redis_client(self.config)
                try:
                    self._redis_client.ping()
                except ConnectionError:
                    raise ConnectionError('Invalid Redis server')
        else:
            self._redis_client = None

    def __read_config_file(self, path):
        if os.path.isfile(path):
            self.config = ConfigParser.RawConfigParser()
            self.config.read(path)
            return True
        return False

    @staticmethod
    def _init_redis_client(config, test=False):
        if not test:
            host = os.environ.get('REDIS_PORT_6379_TCP_ADDR') 
            #config.get('ConnectionSection', 'redis.host')
            port = config.get('ConnectionSection', 'redis.port')
            r = redis.StrictRedis(host=host, port=port, db=0)
            return r
        return "Stub"

    def get_feature_flag(self, name):
        value = self._redis_client.get(name)
        if value is not None:
            return True
        else:
            return False
