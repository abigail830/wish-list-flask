from __future__ import absolute_import

from flask import jsonify, request
from demo import app, log
from demo.service import UserService

_user_service = UserService


@app.route('/users', methods=['GET'])
def query_users():
    if 'id' in request.args:
        _user_id = request.args.get('id')
        return UserService.get_user_by_id(_user_id)
    else:
        return jsonify({'users': _user_service.get_all_user()})


@app.route('/users', methods=['POST'])
def add_user():
    _data = request.get_json()
    log.info('/users POST request data {}'.format(_data))

    _user = _data.get('user')
    _wish_description = _data.get('wish', '')

    result = UserService.add_wish_for_user(_user, _wish_description)
    return jsonify({'result': result})


