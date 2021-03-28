import logging
import os
import sys
from logging import Formatter
from logging.handlers import TimedRotatingFileHandler

from flask import Flask
from flask_apscheduler import APScheduler
from flask_httpauth import HTTPTokenAuth
from flask_sqlalchemy import SQLAlchemy

"""
flask app
"""
app = Flask(__name__)
app.config.from_envvar('FLASK_CFG')

"""
logger
"""
log_dir = app.config['LOG_DIR']
log_file = app.config['LOG_FILE']
log_format = app.config['LOG_FORMAT']

if not os.path.exists(log_dir):
    os.makedirs(log_dir)

file_handler = TimedRotatingFileHandler(
    filename=os.path.join(log_dir, log_file),
    when='midnight',
    backupCount=7,
    encoding='utf-8')
file_handler.suffix = '%Y-%m-%d'
file_handler.setFormatter(Formatter(log_format))
app.logger.addHandler(file_handler)
app.logger.setLevel(logging.DEBUG)

"""
auth
"""
auth = HTTPTokenAuth(scheme='Bearer')

"""
scheduler
"""
scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()

"""
database
"""
db = SQLAlchemy()
db.init_app(app)

app.logger.info(f'"app" in sys.modules: {"app" in sys.modules}')
app.logger.info(f'server is running by {app.config["NAME"]} config')

if __name__ == '__main__':
    app.run()
