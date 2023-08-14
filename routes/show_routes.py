

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

@shows_bp.route('/api/shows/movie/<movie_id>', methods=['GET'])
def get_movie_shows(movie_id):
    shows = Show.get_by_movie(movie_id)
    return jsonify(shows), 200


# @shows_bp.route('/api/shows', methods=['POST'])
# def create_show():
#     data = request.get_json()
#     # Create a new Show instance
#     show = Show().create(data)

#     return jsonify(show), 201

# @shows_bp.route('/api/book_show', methods=['POST'])
# def book_show():
#     data = request.get_json()
#     movie_id = data.get("movieId")
#     participant = data.get("participant")

#     # Add the movie name to the participant data
#     participant["movies"] = [movie_id]

#     # Save the participant to the database
#     participant_id = create_participant(participant)

#     # Retrieve the show details for the given movie
#     shows = get_shows_by_movie(movie_id)

#     # Select the first show (you can add more logic here to choose a specific show)
#     show = shows[0] if shows else None

#     if not show:
#         return jsonify({"message": "Show not found for the selected movie"}), 404

#     # Perform the booking logic here...
#     # For example, update the show with the participant details and reduce the available seats
#     # Then save the updated show to the database

#     # Return success response
#     return jsonify({"message": "Show booked successfully"}), 200