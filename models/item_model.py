from db import db


class ItemModel(db.Model):

    __tablename__ = 'item'

    item_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    description = db.Column(db.String(75))

    owner_id = db.Column(db.Integer, db.ForeignKey('person.id'), nullable=False, unique=False)
    persona = db.relationship('PersonModel', back_populates='items')
