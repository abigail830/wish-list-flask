from __future__ import absolute_import

from flask import render_template, jsonify, request
from flask_restplus import Resource, reqparse, Namespace

from demo import app, api
from demo.service import WishService

# ns = Namespace("users", description="Users CURD api.")


@app.route('/hello')
def hello():
    user = {'username': 'Sara Qian'}
    return render_template('hello.html', title=app.config['TITLE'], user=user)


@api.route('/health')
class Health(Resource):
    def get(self):
        return "UP"


@api.route('/wishes')
class WishController(Resource):
    def get(self):
        result = WishService.query_all_wishes()
        return jsonify(result)


# parser = reqparse.RequestParser()
# parser.add_argument('wish', type=int, help='User id', location='json')
# args = parser.parse_args()


@api.route('/users/<int:user_id>/wishes')
class UserWishController(Resource):
    def get(self, user_id):
        result = WishService.query_wish_for_user(user_id)
        return jsonify(result)

