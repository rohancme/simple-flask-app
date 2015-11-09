from src.fflag import FeatureFlag
import pytest

class ConfigStub():

	def __init__(self, input_dict):
		self.conf = input_dict
	
	def get(self, sec_name, key_name=None):
		if self.conf is None:
			raise Exception
		if sec_name in self.conf :
			if key_name is None:
				return self.conf[sec_name]
			else:
				if key_name in self.conf[sec_name]:
					return self.conf[sec_name][key_name]
				else:
					return None
		else:
			return None

def test_init_redis_client():
	redis_config = ConfigStub({
		'ConnectionSection':{
			'redis.host':'localhost',
			'redis.port':6379
		}
	})
	redis = FeatureFlag._init_redis_client(redis_config, True)
	if redis is None:
		pytest.fail('Unable to init local redis client')

def test_get_feature_flag():
	ff = FeatureFlag(True)
	ff._redis_client = ConfigStub({
		'foo':'bar'
		})
	assert(ff.get_feature_flag('foo') is not None)
