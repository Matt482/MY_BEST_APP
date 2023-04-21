from flask_smorest import Blueprint
from flask.views import MethodView
from sqlalchemy.exc import SQLAlchemyError
from flask_jwt_extended import jwt_required

from db import db
from models.item_model import ItemModel
from schemas import ItemSchema, ItemUpdateSchema

from flask import jsonify

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
            return jsonify({"Message": f"Cant find item {item_id}"}), 400

    @blt.arguments(ItemUpdateSchema)
    @blt.response(201, ItemUpdateSchema)
    def put(self, payload, item_id):
        item = ItemModel.query.filter_by(item_id=item_id).first()
        if item:
            item.description = payload['description']
            item.name = payload['name']
            item.owner_id = payload['owner_id']
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
    @jwt_required()
    @blt.response(200, ItemSchema(many=True))
    def get(self):
        all_items = ItemModel.query.all()
        return all_items

    @jwt_required()
    @blt.arguments(ItemSchema)
    @blt.response(201, ItemSchema)
    def post(self, stored_data):
        try:
            item = ItemModel(**stored_data)
            db.session.add(item)
            db.session.commit()

        except SQLAlchemyError as se:
            raise se

        return {"Message": f"Item {item.name} succesfully created!"}
