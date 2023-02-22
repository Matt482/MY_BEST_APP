from db import db


class TagModel(db.Model):

    __tablename__ = 'tags'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('person.id'), nullable=False)

    #Create a relation to itemmodel
    items = db.relationship('ItemModel', back_populates='tags', secondary='items_tags')
    person = db.relationship('PersonModel', back_populates='tags')