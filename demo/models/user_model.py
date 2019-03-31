from __future__ import absolute_import

from demo import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    username = db.Column(db.String(64), index=True)
    sex = db.Column(db.String(10), nullable=False)
    birthday = db.Column(db.Date, nullable=False)
    wishes = db.relationship('Wish', backref='user', lazy='dynamic')

    # def __init__(self, username, sex, birthday):
    #     self.username = username
    #     self.sex = sex
    #     self.birthday = birthday
    #     self.wishes = []

    def add_wish(self, wish):
        self.wishes.append(wish)

    def __repr__(self):
        return 'User {0} [{1}] Birthday {2}'\
            .format(self.username, self.sex, self.birthday)

