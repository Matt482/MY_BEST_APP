from flask_smorest import Blueprint
from flask.views import MethodView
from sqlalchemy.exc import SQLAlchemyError

from db import db
# from models.owner_model import OwnerModel
# from schemas import PlainOwnerSchema, OwnerSchema

from flask import request


blt = Blueprint('owners', __name__, description="This suits for owners")


# @blt.route('/owner/<string:name>')
# class Owner(MethodView):
#
#     @blt.response(200, OwnerSchema)
#     def get(self, name):
#         try:
#             one_owner = OwnerModel.query.filter_by(name=name).first()
#             return {'Owners name': one_owner.name, "owner id": one_owner.id}
#         except SQLAlchemyError as se:
#             raise se
#
#     @blt.arguments(PlainOwnerSchema)
#     @blt.response(200, PlainOwnerSchema)
#     def post(self, stored_data, name):
#         try:
#             own = OwnerModel(name=name, address=stored_data['address'])
#             db.session.add(own)
#             db.session.commit()
#             return {"Message": f"owner {own.name} created succesfully"}, 201
#
#         except SQLAlchemyError as se:
#             raise se
#
#     def delete(self):
#         pass
#
#
# @blt.route('/owners')
# class Owners(MethodView):
#
#     @blt.response(200, OwnerSchema)
#     def get(self):
#         all_owners = OwnerModel.query.all()
#         res = []
#         for own in all_owners:
#             res.append(own.name)
#
#         return {'Owners': list(res)}


# @blt.route('/owner/<string:name>/all_pets')
# def get_owner_pets(name):
#     try:
#         own = OwnerModel.query.filter_by(name=name).first()
#         owner_pets = [pet.name for pet in own.pets]
#         return {"Owner_pets": owner_pets}
#
#     except SQLAlchemyError as se:
#         raise se


# @blt.route('/owner_del/<string:name>', methods=['DELETE'])
# def delete_owner(name):
#     try:
#         own = OwnerModel.query.filter_by(name=name).first()
#         db.session.delete(own)
#         db.session.commit()
#         return {"Message": f"user {own.name} succesfully deleted!"}, 201
#
#     except SQLAlchemyError as se:
#         raise se
