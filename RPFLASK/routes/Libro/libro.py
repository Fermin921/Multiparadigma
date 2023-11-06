from models import Libro
from form import LibroForm
from flask import Blueprint, request, redirect, render_template, url_for
from app import db
from routes.Prestamo.prestamo import Prestamo

applibro = Blueprint("applibro", __name__, template_folder="templates")


@applibro.route("/")
@applibro.route("/index")
def inicio():
    libros = Libro.query.all()
    prestamos = Prestamo.query.all()
    return render_template("index.html", libros=libros, prestamo=prestamos)


@applibro.route("/agregarlibro", methods=["GET", "POST"])
def agregar():
    libro = Libro()
    libroForm = LibroForm(obj=libro)
    if request.method == "POST":
        if libroForm.validate_on_submit():
            libroForm.populate_obj(libro)
            db.session.add(libro)
            db.session.commit()
            return redirect(url_for("applibro.inicio"))
    return render_template("libro/agregar.html", forma=libroForm)


@applibro.route("/editarlibro/<int:id>", methods=["GET", "POST"])
def editar(id):
    libro = Libro.query.get_or_404(id)
    libroForm = LibroForm(obj=libro)
    if request.method == "POST":
        if libroForm.validate_on_submit():
            libroForm.populate_obj(libro)
            db.session.commit()
            return redirect(url_for("applibro.inicio"))
    return render_template("libro/editar.html", forma=libroForm)


@applibro.route("/eliminarlibro/<int:id>")
def eliminar(id):
    libro = Libro.query.get_or_404(id)
    db.session.delete(libro)
    db.session.commit()
    return redirect(url_for("applibro.inicio"))
