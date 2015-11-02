# simple-flask-app

![Build Status](https://travis-ci.org/rchakra3/simple-flask-app.svg?branch=master)

A simple flask app to use in learning about CI etc

## Setup

```
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```

## Running the app

```
python source/app.py
```

## Setup [Tests]

```
pip install -r test_requirements.txt
```

## Running tests

```
py.test test
```

## Ensure build is successfull

```
tox
```

## Contributing

- The master branch is protected. This means no forced pushes and no merges with branches that are breaking the build.
- Submit a pull request to check the status of your build