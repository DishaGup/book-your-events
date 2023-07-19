# routes/user.route.py

from flask import Blueprint, jsonify, request
from models.user_model import User
from app import db

users_bp = Blueprint('/', __name__)

@users_bp.route('/api/users', methods=['GET'])
def get_users():
    users = User.objects()
    return jsonify(users), 200

@users_bp.route('/api/users', methods=['POST'])
def create_user():
    data = request.get_json()
    username = data.get('username')
    user_status = data.get('user_status')
    gender = data.get('gender')
    membership_type = data.get('membership_type')
    bio = data.get('bio')
    date_of_birth = data.get('date_of_birth')
    location = data.get('location')

    user = User(username=username, user_status=user_status, gender=gender,
                membership_type=membership_type, bio=bio, date_of_birth=date_of_birth,
                location=location)
    user.save()

    return jsonify(user), 201

@users_bp.route('/api/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = User.objects.get_or_404(id=user_id)
    return jsonify(user), 200

@users_bp.route('/api/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.objects.get_or_404(id=user_id)
    data = request.get_json()
    user.username = data.get('username', user.username)
    user.user_status = data.get('user_status', user.user_status)
    user.gender = data.get('gender', user.gender)
    user.membership_type = data.get('membership_type', user.membership_type)
    user.bio = data.get('bio', user.bio)
    user.date_of_birth = data.get('date_of_birth', user.date_of_birth)
    user.location = data.get('location', user.location)
    user.save()

    return jsonify(user), 200

@users_bp.route('/api/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.objects.get_or_404(id=user_id)
    user.delete()
    return jsonify(message='User deleted'), 200
