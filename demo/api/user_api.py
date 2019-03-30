from __future__ import absolute_import

from flask import jsonify
from demo import app
from demo.service import UserService

_user_service = UserService


@app.route('/users')
def query_users():
    return jsonify({'users': _user_service.get_all_user()})


