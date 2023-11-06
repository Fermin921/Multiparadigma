from flask import Blueprint, request, redirect, render_template, url_for
from models import Usuario, Prestamo
from form import UsuarioForm, PrestamoForm
from app import db

appprestamo = Blueprint("appprestamo", __name__, template_folder="templates")


@appprestamo.route("/")
@appprestamo.route("/index")
def inicio():
    prestamos = Prestamo.query.all()
    return render_template("index.html", prestamos=prestamos)


@appprestamo.route("/agregarprestamo", methods=["GET", "POST"])
def agregar():
    prestamo = Prestamo()
    prestamoForm = PrestamoForm(obj=prestamo)
    if request.method == "POST":
        if prestamoForm.validate_on_submit():
            prestamoForm.populate_obj(prestamo)
            db.session.add(prestamo)
            db.session.commit()
            return redirect(url_for("appprestamo.inicio"))
    return render_template("prestamo/agregar.html", forma=prestamoForm)


@appprestamo.route("/editarprestamo/<int:id>", methods=["GET", "POST"])
def editar(id):
    prestamo = Prestamo.query.get_or_404(id)
    prestamoForm = PrestamoForm(obj=prestamo)
    if request.method == "POST":
        if prestamoForm.validate_on_submit():
            prestamoForm.populate_obj(prestamo)
            db.session.commit()
            return redirect(url_for("appprestamo.inicio"))
    return render_template("editar.html", forma=prestamoForm)


@appprestamo.route("/eliminarprestamo/<int:id>")
def eliminar(id):
    prestamo = Prestamo.query.get_or_404(id)
    db.session.delete(prestamo)
    db.session.commit()
    return redirect(url_for("appprestamo.inicio"))
