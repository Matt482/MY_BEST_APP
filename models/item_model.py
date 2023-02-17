from db import db


class Item(db.Model):
    item_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    description = db.Column(db.String(75))

