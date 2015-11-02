# simple-flask-app
A simple flask app to use in learning about CI etc

![Build Status](https://travis-ci.org/rchakra3/simple-flask-app.svg?branch=master)


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