# -*- coding: utf-8 -*-

import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or '_of12039fmMMFD9fiqn2fasjui203'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'mysql+pymysql://root:123456@localhost/flask_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
