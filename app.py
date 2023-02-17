from flask import Flask
from flask_smorest import Api

import models
from db import db

from resources.user import blt as UserBlueprint
from resources.services import blt as ServiceBlueprint
from resources.pet_res import blt as PetBlueprint
from resources.owner_res import blt as OwnerBlueprint
from resources.item_res import blt as ItemBlueprint


def create_app():

    app = Flask(__name__)

    app.config['PROPAGATE_EXCEPTIONS'] = False
    app.config["API_TITLE"] = "Stores REST API"
    app.config['API_VERSION'] = 'v1'
    app.config['OPENAPI_VERSION'] = '3.0.3'
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data_2.db"

    # if len(os.listdir("./empty")) == 0:
    #     db.create_all()

    db.init_app(app)
    with app.app_context():
        db.create_all()

    api = Api(app)
    api.register_blueprint(UserBlueprint)
    api.register_blueprint(ServiceBlueprint)
    api.register_blueprint(PetBlueprint)
    api.register_blueprint(OwnerBlueprint)
    api.register_blueprint(ItemBlueprint)

    return app
