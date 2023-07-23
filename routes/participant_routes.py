
from flask import Blueprint, jsonify, request
from models.user_model import Movie, Show, Event, Participant
participants_bp = Blueprint('participant', __name__)

# Participant routes
@participants_bp.route('/api/participants', methods=['GET'])
def get_participants():
    participants = Participant().get_all()
    return jsonify(participants), 200

@participants_bp.route('/api/participants', methods=['POST'])
def create_participant():
    data = request.get_json()
    # Create a new Participant instance
    participant = Participant().create(data)

    return jsonify(participant), 201

@participants_bp.route('/api/participants/<participant_id>', methods=['GET'])
def get_participant(participant_id):
    participant = Participant().get_by_id(participant_id)
    return jsonify(participant), 200

@participants_bp.route('/api/participants/<participant_id>', methods=['PUT'])
def update_participant(participant_id):
    participant = Participant().get_by_id(participant_id)
    data = request.get_json()
    # Update participant attributes
    participant.update(data)

    return jsonify(participant), 200

@participants_bp.route('/api/participants/<participant_id>', methods=['DELETE'])
def delete_participant(participant_id):
    participant = Participant().get_by_id(participant_id)
    participant.delete()
    return jsonify(message='Participant deleted'), 200

@participants_bp.route('/api/participants/book/<participant_id>/<show_id>', methods=['POST'])
def book_show(participant_id, show_id):
    show = Show.get_by_id(show_id)
    if not show:
        return jsonify({"message": "Show not found"}), 404

    participant = Participant.get_by_id(participant_id)
    if not participant:
        return jsonify({"message": "Participant not found"}), 404

    participant.book_show(show_id)
    return jsonify({"message": "Show booked successfully"}), 200
