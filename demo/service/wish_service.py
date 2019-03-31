from __future__ import absolute_import

from demo.models import Wish
from demo.service import UserService

user_service = UserService


class WishService(object):

    @staticmethod
    def add_wish_to_user(user_id, wish_description):
        exist_user = user_service.get_user_by_id(user_id)
        if exist_user is not None:
            wish = Wish(description=wish_description)
            exist_user.add_wish(wish)
            user_service.save_user(exist_user)
            return user_service.get_all_user()
        else:
            # TODO: should throw exception here
            return 'User not exist.'
