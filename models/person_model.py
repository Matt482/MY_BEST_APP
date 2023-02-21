from db import db


class PersonModel(db.Model):

    __tablename__ = "person"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    klas = db.Column(db.String(20), nullable=False)

    # cascade='all, delete' --> deleted from items!
    items = db.relationship('ItemModel', back_populates='person', lazy='dynamic')
    tags = db.relationship('TagModel', back_populates='person', lazy='dynamic')
