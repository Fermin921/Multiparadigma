from flask import Flask
from database import db
from config import BasicConfig
from flask_migrate import Migrate
import logging

app = Flask(__name__)
app.config.from_object(BasicConfig)
db.init_app(app)
migrate = Migrate()
migrate.init_app(app, db)
