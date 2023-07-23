from flask import Blueprint, jsonify, request, session, redirect, url_for
from models.user_model import Event, Participant
from middleware.auth import token_required
from datetime import datetime
from dateutil.parser import parse
events_bp = Blueprint('events', __name__)


@events_bp.route('/api/events', methods=['GET'])
def get_events():
    events = Event().get_all()
    events_with_id = []
    for event in events:
        event["_id"] = str(event["_id"])
        events_with_id.append({
            "_id": event["_id"],
            "eventName": event["eventName"],
            "eventDate": event["eventDate"],
            "category": event["category"],
            "venue": event["venue"],
            "ticket_price": event["ticket_price"],
            "location": event["location"],
            "participants" : event["participants"]
        })
    return jsonify({"event": events_with_id}), 200


@events_bp.route('/api/events', methods=['POST'])
# Apply the token_required decorator with role 'admin'
@token_required(role='admin')
def create_event(current_user):
    data = request.get_json()
    # Create a new Event instance
    required_fields = ['eventName', 'eventDate',
                       'category', 'venue', 'ticket_price']

    # Check if all required fields are present in user_data
    for field in required_fields:
        if field not in data:
            return jsonify({"message": f"Required field '{field}' is missing in data"}) ,401

    eventName = data.get('eventName')
    eventDate = data.get('eventDate')
    category = data.get('category')
    venue = data.get("venue")
    ticket_price = data.get('ticket_price')
    location = data.get('location')
    eventDate_str = eventDate[:-1] 
    
    try:
        eventDate = parse(eventDate_str)
    except ValueError:
        return jsonify({"message": "Invalid eventDate format. Please use YYYY-MM-DDTHH:mm"}), 400

    event_data = {
        'eventName': eventName,
        'eventDate': eventDate,
        'category': category,
        'venue': venue,
        'ticket_price': ticket_price,
        'location': location,
        "participants": []
    }

    event = Event.create(event_data)

    return jsonify({"message":"event created Successfully"}), 201

@events_bp.route('/api/events/<event_id>', methods=['GET'])
def get_event(event_id):
    event = Event().get_by_id(event_id)
    if event:
        event["_id"] = str(event["_id"])
        event_with_id = {
            "_id": event["_id"],
            "eventName": event["eventName"],
            "eventDate": event["eventDate"],
            "category": event["category"],
            "venue": event["venue"],
            "ticket_price": event["ticket_price"],
            "location": event["location"],
            "participants": event["participants"]
        }
        return jsonify({"event": event_with_id}), 200
    else:
        return jsonify({"message": "Event not found"}), 404


@events_bp.route('/api/events/<event_id>', methods=['PUT'])
def update_event(event_id):
    event = Event.get_by_id(event_id)
    data = request.get_json()
    # Update event attributes
    event.update(data)

    return jsonify(event), 200


@events_bp.route('/api/events/<event_id>', methods=['DELETE'])
def delete_event(event_id):
    event = Event().get_by_id(event_id)
    event.delete()
    return jsonify(message='Event deleted'), 200


@events_bp.route('/api/events/book', methods=['POST'])
# Require the user to be logged in to book an event
def book_event():
    data = request.get_json()
    event_id = data.get('eventId')
    participant_details = data.get('participantDetails')

    # Check if participant details are provided
    if not participant_details:
        return jsonify({"message": "Participant details are required to book an event"}), 400

    event = Event.get_by_id(event_id)
    if not event:
        return jsonify({"message": "Event not found"}), 404

    # Create a new participant and associate with the event
    participant_data = {
        'name': participant_details['name'],
        'email': participant_details.get('email'),
        'phoneno': participant_details.get('phoneno'),
        'address': participant_details.get('address'),
        "events":[],
    }
    participant = Participant.create(participant_data)
   

    if participant['_id'] not in event["participants"]:
        event["participants"].append(participant['_id'])
        event.update({'participants': event["participants"]})

    # Associate the event with the participant as well
    Participant.add_event(event)

    return jsonify({"message": "Event booked successfully"}), 200


