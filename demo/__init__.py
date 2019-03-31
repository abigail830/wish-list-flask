from __future__ import absolute_import

import logging.config

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from demo.config import config

# define app
app = Flask(__name__)
app.config.from_object(config['development'])
logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

# define db
db = SQLAlchemy(app)
migrate = Migrate(app, db)


from demo.api import index_api, user_api

from demo.models import user_model, wish_model
