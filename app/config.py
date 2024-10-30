# -*- coding: utf-8 -*-

import os


class Config:
    """
    通用配置
    """
    SECRET_KEY = os.environ.get('SECRET_KEY') or '_of12039fmMMFD9fiqn2fasjui203'


class DevelopmentConfig(Config):
    """
    开发环境配置
    """
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'mysql+pymysql://root:123456@localhost/flask_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    """
    生产环境配置
    """
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'mysql+pymysql://root:123456@localhost/flask_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


# 根据环境变量选择配置
config_by_name = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}

default_config = config_by_name[os.environ.get('FLASK_ENV') or 'development']
