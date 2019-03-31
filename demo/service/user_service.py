from __future__ import absolute_import

from demo import log
from demo.models import User, Wish


class UserService(object):

    def __init__(self):
        pass

    @staticmethod
    def get_all_user():
        return User.query.all()

    @staticmethod
    def get_user_by_id(user_id):
        return user_id

    @staticmethod
    def add_wish_for_user(user, wish_description):
        if user.get('id') is not None:
            return 'Going to check if user exist'
        else:
            if UserService._valid_user(user):
                _wish = Wish(wish_description)
                _new_user = User(user.get('username'), user.get('sex'), user.get('birthday'))
                _new_user.add_wish(_wish)
                return 'User data going to insert to DB: \n {0} \n new wish: {1}'.format(_new_user, _wish)
            else:
                return "This is abnormal user"

    @staticmethod
    def _valid_user(user):

        _username = user.get('username')
        _sex = user.get('sex')
        _birthday = user.get('birthday')

        if _username is not None and _sex is not None and _birthday is not None:
            return True
        else:
            return False



