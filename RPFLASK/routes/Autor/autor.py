from flask import Blueprint, request, redirect, render_template, url_for
from models import Autor
from form import AutorForm
from app import db
from routes.Prestamo.prestamo import Prestamo

appautor = Blueprint("appautor", __name__, template_folder="templates")


@appautor.route("/")
@appautor.route("/index")
def inicio():
    autores = Autor.query.all()
    prestamos = Prestamo.query.all()
    return render_template("index.html", autores=autores, prestamo=prestamos)


@appautor.route("/agregarautor", methods=["GET", "POST"])
def agregar():
    autor = Autor()
    autorForm = AutorForm(obj=autor)
    if request.method == "POST":
        if autorForm.validate_on_submit():
            autorForm.populate_obj(autor)
            db.session.add(autor)
            db.session.commit()
            return redirect(url_for("appautor.inicio"))
    return render_template("autor/agregar.html", forma=autorForm)


@appautor.route("/editarautor/<int:id>", methods=["GET", "POST"])
def editar(id):
    autor = Autor.query.get_or_404(id)
    autorForm = AutorForm(obj=autor)
    if request.method == "POST":
        if autorForm.validate_on_submit():
            autorForm.populate_obj(autor)
            db.session.commit()
            return redirect(url_for("appautor.inicio"))
    return render_template("editar.html", forma=autorForm)


@appautor.route("/eliminarautor/<int:id>")
def eliminar(id):
    autor = Autor.query.get_or_404(id)
    db.session.delete(autor)
    db.session.commit()
    return redirect(url_for("appautor.inicio"))
