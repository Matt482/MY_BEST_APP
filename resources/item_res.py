from flask_smorest import Blueprint
from flask.views import MethodView
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models.item_model import ItemModel
from schemas import PlainItemSchema, ItemSchema, ItemUpdateSchema

blt = Blueprint('item_res', __name__, description='This blueprint is for operation upon items')


@blt.route('/items/<string:name>')
class Items(MethodView):

    # dOdO: fix the validation
    @blt.response(200, ItemSchema)
    def get(self, name):
        my_item = ItemModel.query.filter_by(name=name).first()
        if my_item is None:
            return f"Cant find item {name}"
        else:
            return my_item

    @blt.arguments(ItemSchema)
    @blt.response(201, ItemSchema)
    def post(self, stored_data, name):
        # print(stored_data['owner'])
        try:
            skus = ItemModel(**stored_data)
            db.session.add(skus)
            db.session.commit()
            return {"Message": f"Item {skus.name} succesfully created!"}
        except SQLAlchemyError as se:
            raise se

    @blt.arguments(ItemUpdateSchema)
    @blt.response(201, ItemUpdateSchema)
    def put(self, payload, name):
        item = ItemModel.query.filter_by(name=name).first()
        if item:
            item.description = payload['description']
            item.name = payload['name']
        else:
            item = ItemModel(**payload)

        db.session.add(item)
        db.session.commit()
        return item

    @blt.response(201, PlainItemSchema)
    def delete(self, name):

        # DODO: fix the validation of wrong input for query
        try:
            skus = ItemModel.query.filter_by(name=name).first()
            db.session.delete(skus)
            db.session.commit()
            return {"Message": f"item {name} succesfully deleted!"}, 201
        except SQLAlchemyError as se:
            raise se


@blt.route('/items')
class ItemOne(MethodView):

    @blt.response(201, ItemSchema(many=True))
    def get(self):
        try:
            all_items = ItemModel.query.all()
            return all_items
        except SQLAlchemyError as se:
            raise se
