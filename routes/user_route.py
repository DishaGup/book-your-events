from flask import Blueprint, jsonify, request, current_app
from models.user_model import User
import jwt
import datetime
from functools import wraps
import os
from werkzeug.security import generate_password_hash, check_password_hash
from passlib.hash import scrypt 
users_bp = Blueprint('user', __name__)
SECRET_KEY = os.getenv("SECRET_KEY")


# Decorator for verifying JWT token and user role
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
                data = jwt.decode(token,current_app.config['SECRET_KEY'] , algorithms=['HS256'])
                current_user = User().get_by_username({'username': data['username']})
                if current_user['role'] != role:
                    return jsonify({'message': 'Unauthorized'}), 401
            except jwt.ExpiredSignatureError:
                return jsonify({'message': 'Token is expired!'}), 401
            except jwt.InvalidTokenError:
                return jsonify({'message': 'Invalid token!'}), 401


            return f(current_user, *args, **kwargs)


        return decorated


    return decorator
# User registration route
@users_bp.route('/api/register', methods=['POST'])
def register():

    data = request.get_json()
    required_fields = ['username', 'password', 'location','email']

    # Check if all required fields are present in user_data
    for field in required_fields:
        if field not in data:
            raise ValueError(f"Required field '{field}' is missing in user_data")

    username = data.get('username')
    password = data.get('password')
    user_status = data.get('user_status')
    email =data.get("email")
    gender = data.get('gender')
    membership_type = data.get('membership_type')
    bio = data.get('bio')
    date_of_birth = data.get('date_of_birth')
    location = data.get('location')
    role = data.get('role')

    existing_user = User().get_by_username(username)
    if existing_user:
        return jsonify({'message': 'Username already exists!'}), 400

    hashed_password = scrypt.hash(password)

    new_user = User().create({
        'username': username,
        'password': hashed_password,
        'user_status': user_status,
        'gender': gender,
        'membership_type': membership_type,
        'bio': bio,
        'date_of_birth': date_of_birth,
        'location': location,
        'email':email,
        'role': role  # Set the role as 'user' for new registrations
    })

    return jsonify({'message': 'User registered successfully!'}), 201

# User login route
@users_bp.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User().get_by_username(username)
    if not user or not check_password_hash(user.password, password):
        return jsonify({'message': 'Invalid username or password!'}), 401

    token = jwt.encode(
        {'username': user.username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)},
        current_app.config['SECRET_KEY'], algorithm='HS256')

    return jsonify({'token': token}), 200

# Admin routes
@users_bp.route('/api/admin/users', methods=['GET'])
@token_required(role='admin')
def get_users(current_user):
    users = User().get_all()
    return jsonify(users), 200

@users_bp.route('/api/admin/users/<username>', methods=['GET'])
@token_required(role='admin')
def get_user(current_user, username):
    user = User().get_by_username(username)
    if not user:
        return jsonify({'message': 'User not found!'}), 404

    return jsonify(user), 200

@users_bp.route('/api/admin/users/<username>', methods=['DELETE'])
@token_required(role='admin')
def delete_user(current_user, username):
    user = User().get_by_username(username)
    if not user:
        return jsonify({'message': 'User not found!'}), 404

    User().delete(username)
    return jsonify({'message': 'User deleted successfully!'}), 200
