from __future__ import absolute_import

from datetime import datetime
from demo import db


class Wish(db.Model):
    __tablename__ = 'wish'
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    description = db.Column(db.String(100))
    create_date_time = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return 'Wish-{0} created at {1}: {2}.'.format(self.id, self.create_date_time, self.description)

