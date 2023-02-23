import os
import secrets
from datetime import timedelta

from flask import Flask, jsonify
from flask_smorest import Api
from flask_jwt_extended import JWTManager

import models
from db import db

from resources.item_res import blt as ItemBlueprint
from resources.person import blt as PersonBlueprint
from resources.tag import blt as TagBlueprint
from resources.user import blt as UserBlueprint

from models.token import TokenBlocklist


def create_app(db_url=None):

    app = Flask(__name__)

    app.config['PROPAGATE_EXCEPTIONS'] = False
    app.config["API_TITLE"] = "Stores REST API"
    app.config['API_VERSION'] = 'v1'
    app.config['OPENAPI_VERSION'] = '3.0.3'
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url or os.getenv("DATABASE_URL", "sqlite:///data_2.db")
    app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

    db.init_app(app)

    pwd = secrets.SystemRandom().getrandbits(128)
    app.config['JWT_SECRET_KEY'] = '283115596964503999410326437429980209564'  # -> pwd

    ACCESS_EXPIRES = timedelta(hours=1, minutes=30)
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = ACCESS_EXPIRES
    jwt = JWTManager(app)

    @jwt.token_in_blocklist_loader
    def check_if_token_revoked(jwt_header, jwt_payload: dict) -> bool:
        jti = jwt_payload['jti']
        token = db.session.query(TokenBlocklist.id).filter_by(jti=jti).scalar()
        return token is not None

    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        return (
            jsonify({"Message": "The token has expired.", 'error': "token_expired"}),
            401,
        )

    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return (
            jsonify({'message': "Signature verification failed.", "error": "invalid_token"}),
            401,
        )

    @jwt.unauthorized_loader
    def missing_token_callback(error):
        return (
            jsonify(
                {
                    "description": "Request does not contain access token",
                    'error': "authorization_required",
                }
            ),
            401
        )

    with app.app_context():
        db.create_all()

    api = Api(app)
    api.register_blueprint(ItemBlueprint)
    api.register_blueprint(PersonBlueprint)
    api.register_blueprint(TagBlueprint)
    api.register_blueprint(UserBlueprint)

    return app
