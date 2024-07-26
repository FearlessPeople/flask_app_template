# -*- coding: utf-8 -*-

from flask import jsonify
from flask_login import login_required, current_user
from . import main_bp

@main_bp.route('/dashboard', methods=['GET'])
@login_required
def dashboard():
    return jsonify({
        'message': 'Welcome to the dashboard',
        'user': current_user.username
    }), 200
