from flask_smorest import Blueprint
from flask.views import MethodView
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models.item_model import Item
from schemas import ItemSchema

blt = Blueprint('item_res', __name__, description='This blueprint is for operation upon items')


@blt.route('/items/<string:name>')
class Items(MethodView):

    @blt.response(200, ItemSchema)
    def get(self, name):
        my_item = Item.query.filter_by(name=name).first()
        return my_item

    @blt.arguments(ItemSchema)
    @blt.response(201, ItemSchema)
    def post(self, stored_data, name):
        try:
            skus = Item(name=name, description=stored_data['description'])
            db.session.add(skus)
            db.session.commit()
            return {"Message": f"Item {skus.name} succesfully created!"}
        except SQLAlchemyError as se:
            raise se

    @blt.response(201, ItemSchema)
    def delete(self, name):
        try:
            skus = Item.query.filter_by(name=name).first()
            db.session.delete(skus)
            db.session.commit()
            return {"Message": f"item {name} succesfully deleted!"}, 201
        except SQLAlchemyError as se:
            raise se


@blt.route('/items')
class ItemOne(MethodView):

    @blt.response(201, ItemSchema)
    def get(self):
        item_names = []
        all_items = Item.query.all()
        for item in all_items:
            item_names.append(item.name)
        return {'Pets': list(item_names)}
