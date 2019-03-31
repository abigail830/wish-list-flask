from __future__ import absolute_import

from flask import jsonify, request

from demo import app, log
from demo.api.dto_json_encoder import DtoJsonEncoder
from demo.service import UserService

service = UserService()
app.json_encoder = DtoJsonEncoder


@app.route('/users', methods=['GET'])
def query_users():
    if 'id' in request.args:
        _user_id = request.args.get('id')
        return jsonify(service.get_user_by_id(_user_id))
    else:
        return jsonify(service.get_all_user())


@app.route('/users', methods=['POST'])
def add_user():
    _data = request.get_json()
    log.info('/users POST request data {}'.format(_data))

    user = _data.get('user')
    wish_description = _data.get('wish', '')

    result = service.add_wish_for_user(service, user, wish_description)
    log.info('return from user_service: {}'.format(result))
    return jsonify({'result': result})


