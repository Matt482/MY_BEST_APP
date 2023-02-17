from flask_smorest import Blueprint
from flask.views import MethodView
from db import db
from datetime import datetime

# from models.user_model import UserModel

from flask import request


blt = Blueprint('users', __name__, description="This suits for users")


# @blt.route('/users')
# class User(MethodView):
#     def get(self):
#         return "AHOJ AKO SA MAS?"
#
#     def post(self):
#         return "AHOJ AKO SA MAS TOTO JE POST?"


# @blt.route('/users/create')
# class OneUser(MethodView):
#     def post(self, sranda):
#
#         prvy_user = UserModel(sranda)
#         print(prvy_user.main_id)
#
#         return "IDEME"

############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################


# #TODO: FINISH THIS ONE IS NOT WORKING CANT RETURN JSON SERIALIZABLE!!!!
# @blt.route('/users/all')
# def get_all_users():
#     all_users = UserModel.query.all()
#     return {"All users": all_users}
#
#
# @blt.route('/users/<string:datet>')
# def users_on_spec_reg_date(datet):
#     new_date = datetime(2022, 2, 1)
#
#     result = UserModel.query.filter(UserModel.date_joined > datetime(2020, 1, 1)).all()
#     for x in result:
#         print(x.first_name)
#     return "NONE"
#
#
# @blt.route('/users')
# def get_all_user_names():
#     all_users = UserModel.query.all()
#
#     user_list = []
#     for user in all_users:
#         user_list.append(user.first_name)
#
#     return {"All users": user_list}
#
#
# @blt.route('/users/<string:name>', methods=['POST'])
# def create_user(name):
#     body = request.get_json()
#
#     first_user = UserModel(first_name=name, email=body['email'])
#
#     db.session.add(first_user)
#     db.session.commit()
#
#     return "User Created"
#
#
# @blt.route('/user/delete/<string:name>', methods=['DELETE'])
# def delete_user(name):
#     try:
#         usr = UserModel.query.filter_by(first_name=name).first()
#         db.session.delete(usr)
#         db.session.commit()
#
#         return {"Message": f"User {name} deleted!"}, 201
#     except:
#         return {"Message": f"Cant find the user with name {name}"}
