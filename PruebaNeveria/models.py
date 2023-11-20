import jwt  # Libreria para utilizar el token
import datetime  # Para usar tipo de dato datetime
from config import BaseConfig  # La configuración de la base de datos
from app import (
    db,
    bcrypt,
)  # Refencia al programa principal trayendo la libreria de base de datos y la de encriptacion


# Modelo categoria
class Categoria(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(255), unique=True, nullable=False)
    precio = db.Column(db.Float, nullable=False)
    # Relacion de 1 a muchos con el modelo producto
    productos = db.relationship("Producto", backref="categoria", lazy=True)


# Modelo producto
class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sabor = db.Column(db.String(255), unique=True, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    # Referencia de que un producto pertenece a una categoria
    categoria_id = db.Column(db.Integer, db.ForeignKey("categoria.id"), nullable=False)
    # Referencia de que un producto pertecene a una sucursal
    sucursal_id = db.Column(db.Integer, db.ForeignKey("sucursal.id"), nullable=False)
    # Relacion producto tiene muchos productos vendidos
    productovendido = db.relationship(
        "Productosvendidos", backref="producto", lazy=True
    )


# Modelo sucursal
class Sucursal(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(255), unique=True, nullable=False)
    direccion = db.Column(db.String(255), unique=True, nullable=False)
    # Relacion uno a muchos con el modelo producto
    productos = db.relationship("Producto", backref="sucursal", lazy=True)
    # Relación uno a muchos con Proveedor
    proveedores = db.relationship("Proveedor", backref="sucursal", lazy=True)
    # Relacion con el modelo telefono
    telefono = db.relationship("Telefono", backref="sucursal", uselist=False, lazy=True)
    # Relacion sucursal tiene muchos clientes
    clientes = db.relationship("Cliente", backref="sucursal", lazy=True)
    # Relacion sucursal tiene muchas materias primas
    materiasprimas = db.relationship("Materiaprima", backref="sucursal", lazy=True)
    # Relacion sucursal tiene muchos empleados
    empleado = db.relationship("Empleado", backref="sucursal", lazy=True)
    # Relacion sucursal tiene muchas ventas
    venta = db.relationship("Venta", backref="sucursal", lazy=True)


# Modelo Telefono
class Telefono(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    no_tel = telefono = db.Column(db.String(10), nullable=False)
    # Referencia a un telefono tiene una sucursal
    sucursal_id = db.Column(db.Integer, db.ForeignKey("sucursal.id"), nullable=False)


# Modelo cliente
class Cliente(db.Model):
    nombre_empresa = db.Column(db.String(50), primary_key=True, nullable=False)
    direccion = db.Column(db.String(255), nullable=False)
    fecha_registro = db.Column(db.DateTime, nullable=False)
    # Relacion un cliente tiene una sucursal
    sucursal_id = db.Column(db.Integer, db.ForeignKey("sucursal.id"), nullable=False)


# Modelo Materia Prima
class Materiaprima(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(255), nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    precio_unitario = db.Column(db.Float, nullable=False)
    # Relacion una materia prima pertenece a una sucursal
    sucursal_id = db.Column(db.Integer, db.ForeignKey("sucursal.id"), nullable=False)


# Modelo Empleados
class Empleado(db.Model):
    clave = db.Column(db.String(50), primary_key=True, nullable=False)
    rfc = db.Column(db.String(255), nullable=False, unique=True)
    nombres = db.Column(db.String(255), nullable=False)
    apellidos = db.Column(db.String(255), nullable=False)
    fecha_nacimiento = db.Column(db.DateTime, nullable=False)
    edad = db.Column(db.Integer, nullable=False)
    sueldo = db.Column(db.Float, nullable=False)
    area_laboral = db.Column(db.String(50), nullable=False)
    # Relación uno a uno con Usuario
    usuario = db.relationship("User", back_populates="empleado")
    # Referencia de que un empleado tiene una sucursal
    sucursal_id = db.Column(db.Integer, db.ForeignKey("sucursal.id"), nullable=False)
    # Relacion empleado tiene muchas ventas
    venta = db.relationship("Venta", backref="sucursal", lazy=True)


# Modelo proveedor
class Proveedor(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(255), nullable=False)
    apellido = db.Column(db.String(255), nullable=False)
    direccion = db.Column(db.String(255), nullable=False)
    telefono = db.Column(db.String(10), nullable=False)
    nombre_empresa = db.Column(db.String(50), nullable=False)
    # Clave foránea para establecer la relación con Sucursal
    sucursal_id = db.Column(db.Integer, db.ForeignKey("sucursal.id"), nullable=False)


# Modelo Encargo
class Encargo(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre_encargo = db.Column(db.String(255), nullable=False)
    cantidad_encargo = db.Column(db.Integer, nullable=False)
    cantidad_a_pagar = db.Column(db.Float, nullable=False)
    forma_de_pago = db.Column(db.String(255), nullable=False)
    fecha_encargo = db.Column(db.DateTime, nullable=False)
    # Clave foránea para establecer la relación con Sucursal
    sucursal_id = db.Column(db.Integer, db.ForeignKey("sucursal.id"), nullable=False)
    # Clave foránea para establecer la relación con proveedor
    proveedor_id = db.Column(db.Integer, db.ForeignKey("proveedor.id"), nullable=False)


# Modelo Venta
class Venta(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fecha_venta = db.Column(db.DateTime, nullable=False)
    monto_total = db.Column(db.Float, nullable=False)
    # Clave foránea para establecer la relación con Sucursal
    sucursal_id = db.Column(db.Integer, db.ForeignKey("sucursal.id"), nullable=False)
    # Clave foránea para establecer la relación con Empleado
    empleado_clave = db.Column(
        db.String, db.ForeignKey("empleado.clave"), nullable=False
    )
    # Relacion venta tiene muchos productos vendidos
    producto = db.relationship("Producto", backref="venta", lazy=True)


# Modelo Productosvendidos
class Productosvendidos(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # Clave foránea para establecer la relación con Venta
    venta_id = db.Column(db.Integer, db.ForeignKey("venta.id"), nullable=False)
    # Clave foránea para establecer la relación con producto
    producto_id = db.Column(db.Integer, db.ForeignKey("producto.id"), nullable=False)


class User(db.Model):  # Modelo de las clase usuario
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)
    # Relación uno a uno con Empleado
    empleado = db.relationship("Empleado", back_populates="user", uselist=False)

    def __init__(self, email, password, admin=False) -> None:
        self.email = email
        self.password = bcrypt.generate_password_hash(
            password, BaseConfig.BCRYPT_LOG_ROUNDS
        ).decode()

        self.registered_on = datetime.datetime.now()
        self.admin = admin

    def encode_auth_token(self, user_id):  # Encriptador de usuarios
        try:
            payload = {
                "exp": datetime.datetime.utcnow()
                + datetime.timedelta(
                    minutes=10
                ),  # Sirve para especificar la cantidad de tiempo que servira el token
                "iat": datetime.datetime.utcnow(),
                "sub": user_id,
            }
            return jwt.encode(payload, BaseConfig.SECRET_KEY, algorithm="HS256")
        except Exception as e:
            print("Error")
            print(e)
            return e

    @staticmethod
    def decode_auth_token(auth_token):  # Decodificador de encriptado
        try:
            payload = jwt.decode(
                auth_token, BaseConfig.SECRET_KEY, algorithms=["HS256"]
            )
            return payload
        except jwt.ExpiredSignatureError as e:
            return "Signature Expired Prelase log in again"

        except jwt.InvalidTokenError as e:
            return "Invalid Token"
