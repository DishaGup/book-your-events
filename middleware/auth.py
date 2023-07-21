# middleware/auth.py
from flask import jsonify, request, current_app
from functools import wraps
import jwt
from models.user_model import User

def token_required(role):
    def decorator(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            token = None

            if 'Authorization' in request.headers:
                token = request.headers['Authorization'].split()[1]

            if not token:
                return jsonify({'message': 'Token is missing!'}), 401

            try:
                data = jwt.decode(
                    token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
                current_user = User().get_by_username(
                    {'username': data['username']})
                if current_user['role'] != role:
                    return jsonify({'message': 'Unauthorized'}), 401
            except jwt.ExpiredSignatureError:
                return jsonify({'message': 'Token is expired!'}), 401
            except jwt.InvalidTokenError:
                return jsonify({'message': 'Invalid token!'}), 401

            return f(current_user, *args, **kwargs)

        return decorated

    return decorator
