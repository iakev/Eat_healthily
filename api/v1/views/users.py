#!/usr/bin/env python
from api.v1.views import app_views
from flask import abort, jsonify, request
from hashlib import md5
from models import storage
from models.users import User

@app_views.route('/users/login', methods=['POST'], strict_slashes=False)
def authenticate_user():
    """Validate and authenticate user login"""
    data = request.get_json()
    login_email = data.get('email')
    login_password = data.get('password')
    user = storage.query_user_login(login_email)
    if not user:
        abort(404)
    login_password_hash = md5(login_password.encode()).hexdigest()
    user_dict = {}
    if user.password == login_password_hash:
        user_dict = user.to_dict()
        user_dict['authenticated'] = True
        return jsonify(user_dict)
    else:
        user_dict['authenticated'] = False
        return jsonify(user_dict)
