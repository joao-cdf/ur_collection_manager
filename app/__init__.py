from flask import Flask
from config import Config

# Flask App
flask_app = Flask(__name__)

# Initiate config envs
flask_app.config.from_object(Config)

from app import routes

if __name__ == "__main__":
    flask_app.run(host='0.0.0.0')