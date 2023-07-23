
from flask import Blueprint, jsonify, request
from models.user_model import Movie,Show
from dateutil.parser import parse
movies_bp = Blueprint('movies', __name__)

# Movie routes
@movies_bp.route('/api/movies', methods=['GET'])
def get_movies():
    movies = Movie().get_all()
    movies_with_id = []
    for event in movies:
        event["_id"] = str(event["_id"])
        movies_with_id.append({
            "_id": event["_id"],
            "title": event["title"],
            "rating": event["rating"],
            "description": event["description"],
            "genre": event["genre"],
            "duration": event["duration"],
            "cast": event["cast"],
            "movieDate" : event["movieDate"],
            "image":event["image"]


        })
    return jsonify({"movies": movies_with_id}), 200
   

@movies_bp.route('/api/movies', methods=['POST'])
def create_movie():
    data = request.get_json()
    required_fields = ['title', 'rating', 'description', 'genre','duration','cast','movieDate']

    # Check if all required fields are present in user_data
    checkmovie = Movie().get_by_title(data["title"])
    if checkmovie:
        return jsonify({"message": "Movie already exist"}), 400

    for field in required_fields:
        if field not in data:
            return jsonify({"message": f"Required field '{field}' is missing in user_data"})
    
    movieDate_str = movieDate[:-1] 
    
    try:
        movieDate = parse(movieDate_str)
    except ValueError:
        return jsonify({"message": "Invalid movieDate format. Please use YYYY-MM-DDTHH:mm"}), 400


    # Create a new Movie instance
    print(data)
    movie = Movie().create(data)

    return jsonify(movie), 201
@movies_bp.route('/api/movies/<movie_id>', methods=['GET'])
def get_movie(movie_id):
    movie = Movie().get_by_id(movie_id)
    if movie:
        # Convert the ObjectId to a string representation
        movie["_id"] = str(movie["_id"])

        return jsonify(movie), 200
    else:
        return jsonify({"message": "Movie not found"}), 404

@movies_bp.route('/api/movies/<movie_id>', methods=['PUT'])
def update_movie(movie_id):
    movie = Movie().get_by_title(movie_id)
    data = request.get_json()
    # Update movie attributes
    movie.update(data)

    return jsonify(movie), 200

@movies_bp.route('/api/movies/<movie_id>', methods=['DELETE'])
def delete_movie(movie_id):
    movie = Movie().get_by_title(movie_id)
    movie.delete()
    return jsonify(message='Movie deleted'), 200





@movies_bp.route('/api/movies/<movie_id>/shows', methods=['GET'])
def get_movie_shows(movie_id):
    shows = Show.get_by_movie(movie_id)
    return jsonify(shows), 200

@movies_bp.route('/api/movies/<movie_id>/shows', methods=['POST'])
def create_show(movie_id):
    data = request.get_json()
    data['movie'] = movie_id  # Associate the show with the movie

    show = Show.create(data)
    return jsonify(show), 201