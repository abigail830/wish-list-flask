from __future__ import absolute_import

from demo.models import User


class UserService(object):

    def __init__(self):
        pass

    @staticmethod
    def get_all_user():
        return User.query.all()

    @staticmethod
    def get_user_by_id(id):
        return id

