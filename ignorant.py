# import os
#
# if len(os.listdir("./empty")) == 0:
#     print('je tam nula')
# else:
#     print('je tam nieco')


# db.init_app(app)

# with app.app_context():
#     db.create_all()




# def create_app():
#
#     app = Flask(__name__)
#
#     app.config["PROPAGATE_EXCEPTIONS"] = True
#     app.config["API_TITLE"] = "Stores REST API"
#     app.config['API_VERSION'] = 'v1'
#     app.config['OPENAPI_VERSION'] = '3.0.3'
#     app.config["OPENAPI_URL_PREFIX"] = "/"
#     app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
#     app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
#
#     # app.config['SQLALCHEMY_DATABASE_URI'] = db_url or os.getenv("DATABASE_URL", "sqlite:///data.db")
#
#     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#
#     db = SQLAlchemy()
#     db.init_app(app)
#
#     with app.app_context():
#         db.create_all()



    # api = Api(app=app)
    #
    # api.register_blueprint(UserBlueprint)
    #
    # return app
