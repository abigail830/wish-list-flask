from __future__ import absolute_import

import logging.config

from flask import Flask
from flask_migrate import Migrate
from flask_restplus import Api
from flask_sqlalchemy import SQLAlchemy

from demo.config import config

# define app
app = Flask(__name__)
app.config.from_object(config['development'])

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

# api = Api(app)
api = Api(app, title="Flask Demo", description="Users and Wishes CURD api.")


# define db
db = SQLAlchemy(app)
migrate = Migrate(app, db)


from demo.api import index_api, user_api, wish_api, health_api

from demo.models import user_model, wish_model
