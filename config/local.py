import os

from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore

project_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
db_uri = f'sqlite:///{project_path}/test.db'

"""
config keys must be uppercase
"""

NAME = 'LOCAL'

SCHEDULER_JOBSTORES = {
    'default': SQLAlchemyJobStore(url=db_uri)
}
SCHEDULER_API_ENABLED = True

SQLALCHEMY_DATABASE_URI = db_uri
SQLALCHEMY_TRACK_MODIFICATIONS = False

LOG_DIR = f'{project_path}/logs'
LOG_FILE = 'log'
LOG_FORMAT = '%(asctime)s [%(threadName)s] %(levelname)5s - %(message)s'
