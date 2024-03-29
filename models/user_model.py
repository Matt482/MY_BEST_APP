from db import db


class UserModel(db.Model):

    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(800), nullable=False)

    items = db.relationship('ItemModel', back_populates='user', lazy='dynamic')
    # tags = db.relationship('TagModel', back_populates='user', lazy='dynamic')
