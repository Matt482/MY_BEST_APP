from db import db


class PersonModel(db.Model):

    __tablename__ = "person"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)
    klas = db.Column(db.String(20))
