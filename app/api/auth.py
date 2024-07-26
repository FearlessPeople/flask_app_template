# -*- coding: utf-8 -*-

from flask import jsonify, request
from flask_login import login_user, logout_user, current_user

from app.api import auth_bp
from app.extensions import login_manager
from app.models.user import User


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@auth_bp.route('/login', methods=['GET'])
def login():
    """Example endpoint returning a list of colors by palette
        This is using docstrings for specifications.
        ---
        parameters:
          - name: palette
            in: path
            type: string
            enum: ['all', 'rgb', 'cmyk']
            required: true
            default: all
        definitions:
          Palette:
            type: object
            properties:
              palette_name:
                type: array
                items:
                  $ref: '#/definitions/Color'
          Color:
            type: string
        responses:
          200:
            description: A list of colors (may be filtered by palette)
            schema:
              $ref: '#/definitions/Palette'
            examples:
              rgb: ['red', 'green', 'blue']
        """
    if current_user.is_authenticated:
        return jsonify({'message': 'Already logged in'}), 200

    data = request.json
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    if user is None or not user.check_password(password):
        return jsonify({'message': 'Invalid credentials'}), 401

    login_user(user)
    return jsonify({'message': 'Logged in successfully'}), 200


@auth_bp.route('/logout', methods=['POST'])
def logout():
    logout_user()
    return jsonify({'message': 'Logged out successfully'}), 200
