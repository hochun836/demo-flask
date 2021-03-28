# Demo Flask

## Python Version

`python --version # Python 3.8.2`

`pip --version # pip 21.0.1`

## Install Dependencies

`pip install -r requirements.txt`

## Export Dependencies

`pip freeze > requirements.txt`

## How to Run

step1. set environment variable

Linux

`export FLASK_CFG=./config/[local.py|sit.py|prd.py]`

Windows

`set FLASK_CFG=./config/[local.py|sit.py|prd.py]`

step2. run application

`flask run`

Then

- server will run on http://127.0.0.1:5000

- server creates `logs` directory in project

- server creates `test.db` file in project

## How to Use Flask_Apscheduler

As set `SCHEDULER_API_ENABLED = True` in `./config/local.py`, we can query / delete / add / edit / pause / run jobs by
api (more [doc](https://github.com/viniciuschiele/flask-apscheduler#api))