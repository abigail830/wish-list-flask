from __future__ import absolute_import

from flask import jsonify
from flask_restplus import Resource

from demo import app
from demo.api.dto_json_encoder import DtoJsonEncoder
from demo.service import UserService, WishService

user_service = UserService()
wish_service = WishService()
app.json_encoder = DtoJsonEncoder


@app.route('/wishes')
class WishController(Resource):
    def get(self):
        result = WishService.query_all_wishes()
        return jsonify(result)


