
from flask import Blueprint, jsonify, request
from models.user_model import Movie
movies_bp = Blueprint('movies', __name__)

# Movie routes
@movies_bp.route('/api/movies', methods=['GET'])
def get_movies():
    movies = Movie().get_all()
    return jsonify(movies), 200

@movies_bp.route('/api/movies', methods=['POST'])
def create_movie():
    data = request.get_json()
    # Create a new Movie instance
    movie = Movie().create(data)

    return jsonify(movie), 201

@movies_bp.route('/api/movies/<movie_id>', methods=['GET'])
def get_movie(movie_id):
    movie = Movie().get_by_title(movie_id)
    return jsonify(movie), 200

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
