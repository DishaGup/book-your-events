from flask import Blueprint, jsonify, request, session, redirect, url_for
from models.user_model import Event


events_bp = Blueprint('events', __name__)

@events_bp.route('/api/events', methods=['GET'])
def get_events():
    events = Event().get_all()
    return jsonify(events), 200

@events_bp.route('/api/events', methods=['POST'])
def create_event():
    data = request.get_json()
    eventName =data.get("eventName")
    eventDate =data.get("eventDate")
    
    # Create a new Event instance
    event = Event().create(data)

    return jsonify(event), 201

@events_bp.route('/api/events', methods=['POST'])
def create_event():
    # Check if the user is logged in
    if 'username' not in session:
        return jsonify({'message': 'Unauthorized'}), 401

    # Check if the user is an admin
    if session['role'] != 'admin':
        return jsonify({'message': 'Unauthorized - Admin access required'}), 403

    data = request.get_json()
    # Create a new Event instance
    event = Event(**data)
    event.save()

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
