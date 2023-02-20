from db import db


class PersonModel(db.Model):

    __tablename__ = "person"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    klas = db.Column(db.String(20), nullable=False)

    items = db.relationship('ItemModel', backref='person', lazy='dynamic')
