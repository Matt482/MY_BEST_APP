from datetime import datetime, timezone, timedelta

from flask_smorest import Blueprint, abort
from flask.views import MethodView
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
from flask import jsonify

from passlib.hash import pbkdf2_sha256

from db import db
from models.user_model import UserModel
from models.token import TokenBlocklist

from schemas import UserSchema

blt = Blueprint('User', __name__, description='This blueprint is for operation with users')


@blt.route('/register')
class UserRegister(MethodView):

    @blt.arguments(UserSchema)
    def post(self, user_data):
        if UserModel.query.filter(UserModel.username == user_data['username']).first():
            abort(409,
                  message='A user with that username already exists in db!')
        user = UserModel(username=user_data['username'],
                         password=pbkdf2_sha256.hash(user_data['password'])
                         )

        db.session.add(user)
        db.session.commit()

        return {"Message": "user successfully created!"}, 201


@blt.route('/login')
class UserLogin(MethodView):

    @blt.arguments(UserSchema)
    def post(self, user_data):
        user = UserModel.query.filter(UserModel.username == user_data['username']).first()
        if user and pbkdf2_sha256.verify(user_data['password'], user.password):
            access_token = create_access_token(identity=user.id)
            return {"access_token": access_token}

        abort(401, message='Invalid credentials.')


@blt.route('/logout')
class UserLogout(MethodView):
    @jwt_required()
    def post(self):
        jti = get_jwt()['jti']
        now = datetime.now(timezone.utc)

        db.session.add(TokenBlocklist(jti=jti, created_at=now))
        db.session.commit()
        return jsonify(msg='JWT revoked')


@blt.route('/user/<int:user_id>')
class User(MethodView):

    @blt.response(201, UserSchema)
    def get(self, user_id):
        user = UserModel.query.get_or_404(user_id)
        return user

    def delete(self, user_id):
        user = UserModel.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return {"Message": "User successfully deleted!"}
