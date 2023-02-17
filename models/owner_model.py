from db import db


class Owner(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    address = db.Column(db.String(50))

    pets = db.relationship("Pet", backref='kokotko')

