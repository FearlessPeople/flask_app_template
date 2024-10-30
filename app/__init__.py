# -*- coding: utf-8 -*-
from flasgger import Swagger
from flask import Flask

from app.api import auth, main
from app.config import default_config
from app.extensions import db, migrate, login_manager
from app.logger import logger

def create_app():
    """
    创建app
    :return:
    """
    app = Flask(__name__)

    swagger = Swagger(app)

    app.config.from_object(default_config)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    from .api.main import main as main_blueprint
    from .api.auth import auth as auth_blueprint
    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint, url_prefix='/auth')  # 注册认证蓝图

    # 应用启动日志
    logger.info("Flask 应用已启动")
    return app
