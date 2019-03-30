from __future__ import absolute_import

from flask import jsonify, request
from demo import app
from demo.service import UserService

_user_service = UserService


@app.route('/users')
def query_users():
    if 'id' in request.args:
        _user_id = request.args.get('id')
        return UserService.get_user_by_id(_user_id)
    else:
        return jsonify({'users': _user_service.get_all_user()})





