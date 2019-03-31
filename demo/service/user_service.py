from __future__ import absolute_import

from datetime import datetime

from demo import log, db
from demo.models import User, Wish


class UserService(object):

    def __init__(self):
        pass

    @staticmethod
    def get_all_user():
        return User.query.all()

    @staticmethod
    def get_user_by_id(user_id):
        return User.query.get(user_id)

    @staticmethod
    def add_user(user):
        new_user = UserService.construct_new_user(user)
        if new_user is not None:
            db.session.add(user)
            db.session.commit()
            return User.query.all()
        else:
            # TODO: It should throw exception instead
            return "Abnormal user: username|sex|birthday should not be null"

    @staticmethod
    def update_user(user):
        if user.get('id') is not None:
            exist_user = User.query.get(user.get('id'))
            UserService.construct_update_user(exist_user, user)
            db.session.commit()
            return User.query.all()

    @staticmethod
    def construct_update_user(exist_user, user):
        exist_user.username = user.get('username') or exist_user.username
        exist_user.sex = user.get('sex') or exist_user.sex
        new_y_m_d__date = datetime.strptime(user.get('birthday'), '%y-%m-%d').date()
        exist_user.birthday = new_y_m_d__date or exist_user.birthday

    @staticmethod
    def valid_user(user):
        if user.get('username') is not None \
                and user.get('sex') is not None \
                and user.get('birthday') is not None:
            return True
        else:
            return False

    @staticmethod
    def construct_new_user(new_user):
        if UserService.valid_user(new_user):
            __username = new_user.get('username')
            __sex = new_user.get('sex')
            new_y_m_d__date = datetime.strptime(new_user.get('birthday'), '%y-%m-%d').date()
            __birthday = new_y_m_d__date
            return User(username=__username, sex=__sex, birthday=__birthday)







