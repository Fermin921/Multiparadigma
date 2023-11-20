from flask import Flask
from flask_cors import CORS
from database import db
from encriptador import bcrypt
from flask_migrate import Migrate
from config import BaseConfig
from routes.users.user import appuser
import logging

app = Flask(__name__)
app.register_blueprint(appuser)
app.config.from_object(BaseConfig)
CORS(app)  # Quita el error de cors
bcrypt.init_app(app)
db.init_app(app)
migrate = Migrate()
migrate.init_app(app, db)
logging.basicConfig(level=logging.DEBUG, filename="logs.log")
