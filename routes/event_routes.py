
from flask import Blueprint, jsonify, request
from models.user_model import Event


events_bp = Blueprint('events', __name__)

@events_bp.route('/api/events', methods=['GET'])
def get_events():
    events = Event().get_all()
    return jsonify(events), 200

@events_bp.route('/api/events', methods=['POST'])
def create_event():
    data = request.get_json()
    # Create a new Event instance
    event = Event().create(data)

    return jsonify(event), 201

@events_bp.route('/api/events/<event_id>', methods=['GET'])
def get_event(event_id):
    event = Event().get_by_id(event_id)
    return jsonify(event), 200

@events_bp.route('/api/events/<event_id>', methods=['PUT'])
def update_event(event_id):
    event = Event().get_by_id(event_id)
    data = request.get_json()
    # Update event attributes
    event.update(data)

    return jsonify(event), 200

@events_bp.route('/api/events/<event_id>', methods=['DELETE'])
def delete_event(event_id):
    event = Event().get_by_id(event_id)
    event.delete()
    return jsonify(message='Event deleted'), 200
