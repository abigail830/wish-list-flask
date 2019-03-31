from __future__ import absolute_import

from flask import jsonify, request

from demo import app, log
from demo.api.dto_json_encoder import DtoJsonEncoder
from demo.service import UserService, WishService

user_service = UserService()
wish_service = WishService()
app.json_encoder = DtoJsonEncoder


@app.route('/users', methods=['GET'])
def query_users():
    if 'id' in request.args:
        __user_id = request.args.get('id')
        return jsonify(user_service.get_user_by_id(__user_id))
    else:
        return jsonify(user_service.get_all_user())


@app.route('/users', methods=['POST'])
def add_user():
    __user = request.get_json().get('user')
    result = user_service.add_user(__user)
    return jsonify({'result': result})


@app.route('/users', methods=['PUT'])
def update_user():
    __user = request.get_json().get('user')
    result = user_service.update_user(__user)
    return jsonify({'result': result})


@app.route('/users/<id>/wishes', methods=['POST'])
def add_wish_for_user():
    __user_id = request.args.get('id')
    __wish = request.get_json().get('wish')
    result = wish_service.add_wish_to_user(__user_id, __wish)
    return jsonify({'result': result})
