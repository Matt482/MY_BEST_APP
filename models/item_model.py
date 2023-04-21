from db import db


class ItemModel(db.Model):

    __tablename__ = 'items'

    item_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=False)
    description = db.Column(db.String(75), unique=False, nullable=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True, unique=False)

    user = db.relationship('UserModel', back_populates='items')
    # tags = db.relationship('TagModel', back_populates='items', secondary='items_tags')
