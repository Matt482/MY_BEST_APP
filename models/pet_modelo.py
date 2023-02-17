from db import db


class Pet(db.Model):

    pet_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    age = db.Column(db.Integer)

    owner_id = db.Column(db.Integer, db.ForeignKey('owner.id'))


