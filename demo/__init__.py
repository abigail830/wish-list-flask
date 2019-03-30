from __future__ import absolute_import

from flask import Flask
from demo.config import config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import logging.config


# define app
app = Flask(__name__)
app.config.from_object(config['development'])
log = logging.getLogger(__name__)

# define db
db = SQLAlchemy(app)
migrate = Migrate(app, db)


from demo.api import index_api, user_api, health_api

from demo.models import user_model, wish_model
