
import sys
import os
from flask import Flask
from flask_mongoengine import MongoEngine
from dotenv import load_dotenv
import urllib.parse
from flask_cors import CORS
from routes.user_route import users_bp
load_dotenv()

app = Flask(__name__)

mongodb_url = os.getenv('MONGODB_URL')
mongodb_url_encoded = urllib.parse.quote_plus(mongodb_url)

app.config['MONGODB_SETTINGS'] = {
    'host': mongodb_url_encoded,
    'db': os.getenv('DATABASE_NAME')
}

db = MongoEngine(app)

app.register_blueprint(users_bp)



@app.route('/')
def home():
    return "Welcome to the Book Your Events API!"



if __name__ == '__main__':
    app.run(debug=True,PORT=8080)
