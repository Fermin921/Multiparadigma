from flask import Blueprint, request, jsonify, render_template
from sqlalchemy import exc
from models import Images
from app import db
from auth import tokenCheck
import base64

imagesUser = Blueprint("imageUser", __name__, template_folder="templates")


# Metodo que ingresa la imagen a la base de datos
def render_image(data):
    render_img = base64.b64encode(data).decode("ascii")
    return render_img


@imagesUser.route("/displayImage", methods=["GET"])
@tokenCheck
def search_page(usuario):
    searchImage = Images.query.filter_by(user_id=usuario["user_id"]).first()
    if searchImage:
        image = searchImage.rendered_data
        return render_template("PerfilUsuario.html", imagen=image)


@imagesUser.route("/uploadPerfil", methods=["POST"])
@tokenCheck
def upload(usuario):
    searchImage = Images.query.filter_by(user_id=usuario["user_id"]).first()
    if searchImage:
        file = request.file["inputFile"]
        data = file.read()
        render_file = render_image(data)
        searchImage.rendered_data = render_file
        searchImage.data = data
        db.session.commit()
        return jsonify({"Message": "Imagen Actualizada"})
    else:
        file = request.files["inputFile"]
        data = file.read()
        render_file = render_image(data)
        newFile = Images()
        newFile.type = "Perfil"
        newFile.rendered_data = render_file
        newFile.data = data
        newFile.user_id = usuario["user_id"]
        db.session.add(newFile)
        db.session.commit()
        return jsonify({"Message": "Imagen Agregada"})
