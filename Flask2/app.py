from flask import Flask
from database import db
from config import BasicConfig
from flask_migrate import Migrate
import logging
from Routes.persona.personas import appersona

app = Flask(__name__)
app.register_blueprint(appersona)
app.config.from_object(BasicConfig)
db.init_app(app)
migrate = Migrate()
migrate.init_app(app, db)
logging.basicConfig(level=logging.DEBUG, filename="logs.log")
