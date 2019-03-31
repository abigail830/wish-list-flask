from __future__ import absolute_import

from flask.json import JSONEncoder

from demo.models import User, Wish


class DtoJsonEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, User):
            return {
                   'id': obj.id,
                   'username': obj.username,
                   'sex': obj.sex,
                   'birthday': obj.birthday,
                   'wishes': list(obj.wishes)
            }

        if isinstance(obj, Wish):
            return {
                   'id': obj.id,
                   'description': obj.description,
                   'create': obj.create_date_time,
                   'userid': obj.user_id
            }

        return super(DtoJsonEncoder, self).default(obj)
