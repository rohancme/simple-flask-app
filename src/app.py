from flask import Flask
from flask import abort
from flask import make_response
from fflag import FeatureFlag
from redis.exceptions import ConnectionError
import random
import requests
import sys
from timeit import default_timer as timer

app = Flask(__name__)

giphy_string = "http://api.giphy.com/v1/gifs/random?api_key=dc6zaTOxFJmzC&tag="
retries = 5

redis_mode = True

if len(sys.argv) > 1 and sys.argv[1] == 'no-redis':
    redis_mode = False
else:
    try:
        feat_flag = FeatureFlag()
    except IOError:
        print "WARNING: No redis config"
        redis_mode = False
    except ConnectionError:
        print "WARNING: Invalid Redis server"
        redis_mode = False


def timer_wrap(func):
    def func_wrapper():
        start = timer()
        ret_val = func()
        end = timer()
        diff = (end - start)
        if redis_mode:
            feat_flag._redis_client.lpush("latency", diff)
        else:
            print diff
        return ret_val
    return func_wrapper


@app.route('/party')
def party_gif():
    resp = get_resp_dict(giphy_string + "party")
    if resp is None:
        abort(make_response('Something went wrong:<br>No gif for you', 500))

    if resp['data']['image_url']:
        img_url = resp['data']['image_url']
        return '<img src=' + img_url + '>'


@app.route('/')
@timer_wrap
def simple_key_gen():
    prime_number = 5743
    rand_num = random.randint(1, 100000000)
    # print rand_num
    while(rand_num > 1000000 or rand_num % prime_number != 0):
        rand_num = random.randint(1, 100000000)

    return '' + str(rand_num)


@app.route('/new')
def new_feature():
    if redis_mode:
        if feat_flag.get_feature_flag('new_feature'):
            return "This is the new feature"
    abort(404)


@app.errorhandler(404)
def page_not_found(error):
    return '<h1>No such URL exists</h1>', 404


def get_resp_dict(url):
    tries_left = retries

    while(tries_left > 0):
        try:
            resp = requests.get(url)
            resp = resp.json()
            if resp['meta']:
                if resp['meta']['status'] == 200:
                    return resp
        except Exception:
            pass
        tries_left -= 1
    return None


if __name__ == '__main__':
    app.run(host='0.0.0.0')
