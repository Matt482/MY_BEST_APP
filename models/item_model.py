from db import db


class Item(db.Model):

    __tablename__ = 'item'

    item_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)
    description = db.Column(db.String(75))

    owner = db.Column(db.String, db.ForeignKey('person.name'), nullable=False, unique=False)
