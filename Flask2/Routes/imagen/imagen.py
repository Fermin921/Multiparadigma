from flask import Blueprint, request, render_template


from models import Images

from app import db

import base64


appimagen = Blueprint("appimagen", __name__, template_folder="vistas")


def renderImagen(data):
    imagenRenderizada = base64.b64encode(data).decode("ascii")

    return imagenRenderizada


@appimagen.route("/leerImagen")
def leerImagen():
    imagen = Images.query.filter_by(id=1).first().renderData

    return render_template("mostrarImagen.html", imagen=imagen)


@appimagen.route("/indexImagen", methods=["POST", "GET"])
def indexImagen():
    if request.method == "POST":
        file = request.files["img"]

        data = file.read()

        render = renderImagen(data)

        nuevaImagen = Images()

        nuevaImagen.type = "Perfil"

        nuevaImagen.renderData = render

        nuevaImagen.data = data

        db.session.add(nuevaImagen)

        db.session.commit()

    return render_template("imagenes.html")
