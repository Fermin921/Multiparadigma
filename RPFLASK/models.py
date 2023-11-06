from app import db


# Modelo de la entidad Autores
class Autor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    apellidos = db.Column(db.String(120), nullable=False)
    edad = db.Column(db.Integer, nullable=False)
    pais = db.Column(db.String(120), nullable=False)
    descripcion = db.Column(db.Text)
    email = db.Column(db.String(120), nullable=False, unique=True)

    def __repr__(self):
        return f"<Autor {self.nombre}>"


# Modelo de la entidad Libros
class Libro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(120), nullable=False)
    autor_id = db.Column(db.Integer, db.ForeignKey("autor.id"), nullable=False)
    autor = db.relationship("Autor", backref=db.backref("libros", lazy=True))

    def __repr__(self):
        return f"<Libro {self.titulo}>"


# Modelo de la entidad Usuarios
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f"<Usuario {self.nombre}>"


# Modelo de la entidad Préstamos
class Prestamo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuario.id"), nullable=False)
    libro_id = db.Column(db.Integer, db.ForeignKey("libro.id"), nullable=False)
    fecha_prestamo = db.Column(db.Date, nullable=False)
    fecha_devolucion = db.Column(db.Date, nullable=True)
    usuario = db.relationship("Usuario", backref=db.backref("prestamos", lazy=True))
    libro = db.relationship("Libro", backref=db.backref("prestamos", lazy=True))

    def __repr__(self):
        return f"<Prestamo {self.id}>"
