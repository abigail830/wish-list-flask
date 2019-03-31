from __future__ import absolute_import

from datetime import datetime,date

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
        return user_id

    @staticmethod
    def add_wish_for_user(self, user, wish_description):
        if user.get('id') is not None:
            return 'Going to check if user exist'
        else:
            if self.__valid_user(user):
                __wish = Wish(wish_description)
                y_m_d__date = datetime.strptime(user.get('birthday'), '%y-%m-%d').date()
                __new_user = User(user.get('username'), user.get('sex'), y_m_d__date)
                __new_user.add_wish(__wish)
                log.info('User data going to insert to DB: \n {0} \n new wish: {1}'.format(__new_user, __wish))

                db.session.add(__new_user)
                db.session.commit()
                return User.query.all()
            else:
                return "This is abnormal user"

    @staticmethod
    def __valid_user(user):

        __username = user.get('username')
        __sex = user.get('sex')
        __birthday = user.get('birthday')

        if __username is not None and __sex is not None and __birthday is not None:
            return True
        else:
            return False



