import secrets
from datetime import timedelta


class Config(object):

    # DB_HOST = 'localhost'  # -> only works on localhost not in docker-container
    DB_HOST = 'mysql_db'  # -> if running on docker container add the same name under db service
    DB_PORT = '3306'
    DB_NAME = "my_db_best"
    DB_USERNAME = "root"
    DB_PASSWORD = "root"
    # DB_CHARSET = "utf8mb4"
    DB_CHARSET = "utf8"

    # SQLALCHEMY_DATABASE_URI = "sqlite:///data_2.db"  # -> soon be deleted!
    SQLALCHEMY_DATABASE_URI = f"mysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:" \
                              f"{DB_PORT}/{DB_NAME}?charset={DB_CHARSET}"
    # # SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:" \
    # #                           f"{DB_PORT}/{DB_NAME}?charset={DB_CHARSET}"

    SQLALCHEMY_TRACK_MODIFICATION = False
    PROPAGATE_EXCEPTIONS = False
    API_TITLE = "Stores REST API"
    API_VERSION = 'v1'
    OPENAPI_VERSION = '3.0.3'
    OPENAPI_URL_PREFIX = "/"
    OPENAPI_SWAGGER_UI_PATH = "/swagger-ui"
    OPENAPI_SWAGGER_UI_URL = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"


    pwd = secrets.SystemRandom().getrandbits(128)
    # JWT_SECRET_KEY = '283115596964503999410326437429980209564'  # -> pwd try os.getenv("env_key")
    JWT_SECRET_KEY = '1235'  # -> pwd try os.getenv("env_key")

    ACCESS_EXPIRES = timedelta(hours=1, minutes=30)
    JWT_ACCESS_TOKEN_EXPIRES = ACCESS_EXPIRES


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True
    SESSION_COOKIE_SECURE = False
    JWT_COOKIE_SECURE = False
    JWT_COOKIE_CSRF_PROTECT = False
    TESTING = True
