# simple-flask-app

![Build Status](https://travis-ci.org/rchakra3/simple-flask-app.svg?branch=master)

A simple flask app to use in learning about CI etc

## Setup

```
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```

### Setting up the Redis instance
Install Redis and run on <REDIS_HOST_URL>:<REDIS_PORT_NUMBER>
In the `feature-flag.ini` file, change the following parameters:
```
redis.host=<REDIS_HOST_URL>
redis.port=<REDIS_PORT_NUMBER>
```

## Running the app

```
python src/app.py
```

## Setup [Tests]

```
pip install -r test_requirements.txt
```

## Running tests

```
py.test test
```

## Ensure build is successful

```
tox
```

## Contributing

- The master branch is protected. This means no forced pushes and no merges with branches that are breaking the build.
- Submit a pull request to check the status of your build