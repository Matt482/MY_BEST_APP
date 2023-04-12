from flask import Flask, jsonify
from flask_smorest import Api
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate

import models
from db import db

from resources.item_res import blt as ItemBlueprint
from resources.person import blt as PersonBlueprint
from resources.tag import blt as TagBlueprint
from resources.user import blt as UserBlueprint

from models.token import TokenBlocklist


def create_app():

    app = Flask(__name__)

    if app.config["ENV"] == "production":
        app.config.from_object("config.ProductionConfig")
    else:
        app.config.from_object("config.DevelopmentConfig")

    db.init_app(app)
    migrate = Migrate(app, db)

    jwt = JWTManager(app)

    @jwt.token_in_blocklist_loader
    def check_if_token_revoked(jwt_header, jwt_payload: dict) -> bool:
        jti = jwt_payload['jti']
        token = db.session.query(TokenBlocklist.id).filter_by(jti=jti).scalar()
        return token is not None

    @jwt.revoked_token_loader
    def revoke_token_callback(jwt_header, jwt_payload):
        return (
            jsonify({"description": "Token has been revoked!!!!!!!!!!!!!!!!!",
                     "error": "token_revoked"}),
            401,
        )

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

    # with app.app_context():
    #     db.create_all()

    api = Api(app)
    api.register_blueprint(ItemBlueprint)
    api.register_blueprint(PersonBlueprint)
    api.register_blueprint(TagBlueprint)
    api.register_blueprint(UserBlueprint)

    return app
