from flask import Blueprint, jsonify, request, current_app
from models.user_model import User
import jwt
import datetime
from functools import wraps
import os
from middleware.auth import token_required    # Updated import statement
from passlib.hash import scrypt

users_bp = Blueprint('user', __name__)
SECRET_KEY = os.getenv("SECRET_KEY")


# User registration route
@users_bp.route('/api/register', methods=['POST'])
def register():

    data = request.get_json()
    required_fields = ['username', 'password', 'location', 'email']

    # Check if all required fields are present in user_data
    for field in required_fields:
        if field not in data:
            return jsonify({"message": f"Required field '{field}' is missing in user_data"})

    username = data.get('username')
    password = data.get('password')
    user_status = data.get('user_status') or True
    email = data.get("email")
    gender = data.get('gender') or 'Other'
    membership_type = data.get('membership_type') or 'Regular'
    bio = data.get('bio')
    date_of_birth = data.get('date_of_birth')
    location = data.get('location')
    role = data.get('role') or 'user'

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
        'email': email,
        'role': role  # Set the role as 'user' for new registrations
    })

    return jsonify({'message': 'User registered successfully!'}), 201


@users_bp.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user_data = User().get_by_username(username)
    if not user_data or not scrypt.verify(password, user_data.get('password', '')):
        return jsonify({'message': 'Invalid username or password!'}), 401

    # Convert the ObjectId to a string before encoding it in the token
    user_data['_id'] = str(user_data['_id'])

    # Encode the user_data dictionary directly in the token
    token = jwt.encode(
        {'user_data': user_data, 'exp': datetime.datetime.utcnow() +
         datetime.timedelta(hours=1)},
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
