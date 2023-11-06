from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SubmitField,
    DateField,
    IntegerField,
    TextAreaField,
    SelectField,
)
from wtforms.validators import DataRequired, Email


class AutorForm(FlaskForm):
    nombre = StringField("Nombre", validators=[DataRequired()])
    apellidos = StringField("Apellidos", validators=[DataRequired()])
    edad = IntegerField("Edad", validators=[DataRequired()])
    pais = StringField("Pais", validators=[DataRequired()])
    descripcion = TextAreaField("Descripcion")
    email = StringField("Email", validators=[DataRequired(), Email()])  # Nuevo campo
    enviar = SubmitField("Enviar")


class LibroForm(FlaskForm):
    titulo = StringField("Título", validators=[DataRequired()])
    autor_id = SelectField(
        "Autor", coerce=int, validators=[DataRequired()], choices=[]
    )  # Las opciones se llenarán dinámicamente
    enviar = SubmitField("Enviar")


class UsuarioForm(FlaskForm):
    nombre = StringField("Nombre", validators=[DataRequired()])
    enviar = SubmitField("Enviar")


class PrestamoForm(FlaskForm):
    usuario_id = IntegerField("ID del Usuario", validators=[DataRequired()])
    libro_id = IntegerField("ID del Libro", validators=[DataRequired()])
    fecha_prestamo = DateField(
        "Fecha de Préstamo (YYYY-MM-DD)", format="%Y-%m-%d", validators=[DataRequired()]
    )
    fecha_devolucion = DateField("Fecha de Devolución (YYYY-MM-DD)", format="%Y-%m-%d")
    enviar = SubmitField("Enviar")
