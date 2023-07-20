

from flask import Blueprint, jsonify, request
from models.user_model import Show

shows_bp = Blueprint('shows', __name__)

# Show routes
@shows_bp.route('/api/shows', methods=['GET'])
def get_shows():
    shows = Show().get_all()
    return jsonify(shows), 200

@shows_bp.route('/api/shows', methods=['POST'])
def create_show():
    data = request.get_json()
    # Create a new Show instance
    show = Show().create(data)

    return jsonify(show), 201

@shows_bp.route('/api/shows/<show_id>', methods=['GET'])
def get_show(show_id):
    show = Show().get_by_id(show_id)
    return jsonify(show), 200

@shows_bp.route('/api/shows/<show_id>', methods=['PUT'])
def update_show(show_id):
    show = Show().get_by_id(show_id)
    data = request.get_json()
    # Update show attributes
    show.update(data)

    return jsonify(show), 200

@shows_bp.route('/api/shows/<show_id>', methods=['DELETE'])
def delete_show(show_id):
    show = Show().get_by_id(show_id)
    show.delete()
    return jsonify(message='Show deleted'), 200
