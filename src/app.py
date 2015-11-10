from flask import Flask
from flask import abort
from flask import make_response
from fflag import FeatureFlag
from redis.exceptions import ConnectionError
import requests
import sys

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


@app.route('/')
def party_gif():
    resp = get_resp_dict(giphy_string + "party")
    if resp is None:
        abort(make_response('Something went wrong:<br>No gif for you', 500))

    if resp['data']['image_url']:
        img_url = resp['data']['image_url']
        return '<img src=' + img_url + '>'


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
    app.run(host='0.0.0.0', port=3000)
