import os.path, redis
import ConfigParser

class FeatureFlag():
	config = None
	__redis_client = None

	def __init__(self):
		if not self.__read_config_file('./feature-flag.ini'):
			raise IOError('Please check your FF configuration')
		else:
			self.__redis_client = FeatureFlag.__init_redis_client(self.config)

	def __read_config_file(self, path):
		if os.path.isfile(path):
			self.config = ConfigParser.RawConfigParser()
			self.config.read(path)
			print self.config.get('ConnectionSection', 'redis.url');
			return True
		return False

	@staticmethod
	def __init_redis_client(config):
		host = config.get('ConnectionSection', 'redis.host')
		port = config.get('ConnectionSection', 'redis.port')
		r = redis.StrictRedis(host=host, port=port, db=0)
		return r

	def get_feature_flag(self, name):
		value = self.__redis_client.get(name)
		if value is not None:
			return True
		else:
			return False
