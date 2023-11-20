from flask import Flask
from flask_cors import CORS
from database import db
from encriptador import bcrypt
from flask_migrate import Migrate
from config import BaseConfig
from routes.user import appuser
from routes.imagenes.imagen import imagesUser
from routes.pdf.pdf import apppdf
from routes.csv.indexCsv import appcsv

app = Flask(__name__)
app.register_blueprint(appuser)
app.register_blueprint(imagesUser)
app.register_blueprint(apppdf)
app.register_blueprint(appcsv)
app.config.from_object(BaseConfig)
CORS(app)  # Quita el error de cors
bcrypt.init_app(app)
db.init_app(app)
migrate = Migrate()
migrate.init_app(app, db)
