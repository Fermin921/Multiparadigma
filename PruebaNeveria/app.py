# Librerias de flask
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate

# Librerias de base de datos y el criptador
from database import db
from encriptador import bcrypt

# Modulo de la configuracion de la bd
from config import BaseConfig

# Rutas de los modelos y vistas
from routes.users.user import appuser
from routes.clientes.cliente import appcliente
from routes.empleado.empleado import appempleado
from routes.materia_prima.materia_prima import appmateria
from routes.producto.producto import approducto
from routes.proveedor.proveedor import approveedor
from routes.sucursal.sucursal import appsucursal

# Libreria para crear el log
import logging

app = Flask(__name__)  # Creacion de la aplicacion de flask
app.register_blueprint(
    appuser
)  # Registrando el blueprint relacionado con las rutas de usuarios.
app.register_blueprint(
    appcliente
)  # Registrando el blueprint relacionado con las rutas de clientes.
app.register_blueprint(
    appempleado
)  # Registrando el blueprint relacionado con las rutas de empleados.
app.register_blueprint(
    appmateria
)  # Registrando el blueprint relacionado con las rutas de materia prima.
app.register_blueprint(
    approducto
)  # Registrando el blueprint relacionado con las rutas de productos.
app.register_blueprint(
    approveedor
)  # Registrando el blueprint relacionado con las rutas de proveedores.
app.register_blueprint(
    appsucursal
)  # Registrando el blueprint relacionado con las rutas de sucursales.

app.config.from_object(
    BaseConfig
)  # Se agrega la configracion a la aplicacion con el archivo config
CORS(app)  # Quita el error de cors
bcrypt.init_app(app)
try:
    db.init_app(app)
    migrate = Migrate()
    migrate.init_app(app, db)
except Exception as e:
    logging.error(f"Error during initialization: {e}")
logging.basicConfig(level=logging.DEBUG, filename="logs.log")
