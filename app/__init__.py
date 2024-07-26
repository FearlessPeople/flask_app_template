# -*- coding: utf-8 -*-
from flasgger import Swagger
from flask import Flask

from app.api import auth, main
from app.config import Config
from app.extensions import db, migrate, login_manager


def create_app():
    """
    创建app
    :return:
    """
    app = Flask(__name__)

    swagger = Swagger(app)

    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    from .api import auth_bp, main_bp
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(main_bp, url_prefix='/api')

    return app
