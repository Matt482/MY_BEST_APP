from flask_smorest import Blueprint
from flask.views import MethodView
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models.item_model import ItemModel
from schemas import PlainItemSchema, ItemSchema, ItemUpdateSchema

blt = Blueprint('item_res', __name__, description='This blueprint is for operation upon items')


@blt.route('/items/<string:item_id>')
class Items(MethodView):

    # dOdO: fix the validation
    @blt.response(200, ItemSchema)
    def get(self, item_id):
        my_item = ItemModel.query.filter_by(item_id=item_id).first()
        if my_item:
            return my_item
        else:
            return f"Cant find item {item_id}", 400

    @blt.arguments(ItemUpdateSchema)
    @blt.response(201, ItemUpdateSchema)
    def put(self, payload, item_id):
        item = ItemModel.query.filter_by(item_id=item_id).first()
        if item:
            item.description = payload['description']
            item.owner = payload['owner']
        else:
            item = ItemModel(item_id=item_id, **payload)

        db.session.add(item)
        db.session.commit()
        return item

    def delete(self, item_id):

        # DODO: fix the validation of wrong input for query
        try:
            item = ItemModel.query.filter_by(item_id=item_id).first()
            db.session.delete(item)
            db.session.commit()
            return {"Message": f"item {item_id} succesfully deleted!"}, 201
        except SQLAlchemyError as se:
            raise se


@blt.route('/items')
class ItemOne(MethodView):

    @blt.response(201, ItemSchema(many=True))
    def get(self):
        all_items = ItemModel.query.all()
        return all_items

    @blt.arguments(ItemSchema)
    @blt.response(201, ItemSchema)
    def post(self, stored_data):
        try:
            skus = ItemModel(**stored_data)
            db.session.add(skus)
            db.session.commit()
            return {"Message": f"Item {skus.name} succesfully created!"}
        except SQLAlchemyError as se:
            raise se
