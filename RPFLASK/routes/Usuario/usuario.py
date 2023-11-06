from flask import Blueprint, request, redirect, render_template, url_for
from models import Usuario
from form import UsuarioForm
from app import db
from routes.Prestamo.prestamo import Prestamo

appusuario = Blueprint("appusuario", __name__, template_folder="templates")


@appusuario.route("/")
@appusuario.route("/index")
def inicio():
    usuarios = Usuario.query.all()
    prestamos = Prestamo.query.all()
    return render_template("index.html", usuarios=usuarios, prestamo=prestamos)


@appusuario.route("/agregarusuario", methods=["GET", "POST"])
def agregar():
    usuario = Usuario()
    usuarioForm = UsuarioForm(obj=usuario)
    if request.method == "POST":
        if usuarioForm.validate_on_submit():
            usuarioForm.populate_obj(usuario)
            db.session.add(usuario)
            db.session.commit()
            return redirect(url_for("appusuario.inicio"))
    return render_template("usuario/agregar.html", forma=usuarioForm)


@appusuario.route("/editarusuario/<int:id>", methods=["GET", "POST"])
def editar(id):
    usuario = Usuario.query.get_or_404(id)
    usuarioForm = UsuarioForm(obj=usuario)
    if request.method == "POST":
        if usuarioForm.validate_on_submit():
            usuarioForm.populate_obj(usuario)
            db.session.commit()
            return redirect(url_for("appusuario.inicio"))
    return render_template("editar.html", forma=usuarioForm)


@appusuario.route("/eliminarusuario/<int:id>")
def eliminar(id):
    usuario = Usuario.query.get_or_404(id)
    db.session.delete(usuario)
    db.session.commit()
    return redirect(url_for("appusuario.inicio"))
