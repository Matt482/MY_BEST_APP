from db import db


class ItemTags(db.Model):

    __tablename__ = 'items_tags'

    id = db.Column(db.Integer, primary_key=True)

    #link to items and tags!!!
    item_links = db.Column(db.Integer, db.ForeignKey('items.item_id'))
    tags_links = db.Column(db.Integer, db.ForeignKey('tags.id'))
