from flask import Flask
from database import db
from config import BasicConfig
from flask_migrate import Migrate
import logging
from routes.Autor.autor import appautor
from routes.Libro.libro import applibro
from routes.Prestamo.prestamo import appprestamo
from routes.Usuario.usuario import appusuario

app = Flask(__name__)
app.register_blueprint(appautor)
app.register_blueprint(applibro)
app.register_blueprint(appprestamo)
app.register_blueprint(appusuario)
app.config.from_object(BasicConfig)
db.init_app(app)
migrate = Migrate()
migrate.init_app(app, db)
logging.basicConfig(level=logging.DEBUG, filename="logs.log")
