
import os
from flask import Flask
from dotenv import load_dotenv
from flask_cors import CORS
from routes.event_routes import events_bp
from routes.movie_routes import movies_bp
from routes.participant_routes import participants_bp
from routes.show_routes import shows_bp
from routes.user_route import users_bp
from flask_pymongo import PyMongo


load_dotenv()


# Replace 'your_mongodb_uri' with the actual URI of your MongoDB database
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MONGODB_URL = os.getenv("MONGODB_URL")
SECRET_KEY = os.getenv("SECRET_KEY")

# Create Flask application
app = Flask(__name__)
CORS(app, origins='*')
app.config['SECRET_KEY'] = SECRET_KEY
app.config['OPENAI_API_KEY'] = OPENAI_API_KEY
app.config['MONGO_URI'] = MONGODB_URL


mongo = PyMongo(app)


app.register_blueprint(users_bp)
app.register_blueprint(events_bp)
app.register_blueprint(shows_bp)
app.register_blueprint(participants_bp)
app.register_blueprint(movies_bp)


@app.route('/')
def home():
    return "Welcome to the Book Your Events API!"


if __name__ == '__main__':
  port = int(os.environ.get("PORT", 8080))
  app.run(debug=True, port=port)
