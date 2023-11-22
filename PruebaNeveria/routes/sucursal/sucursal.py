from flask import Blueprint, request, jsonify, render_template, redirect
from sqlalchemy import exc
from models import Sucursal
from app import db, bcrypt
from auth import tokenCheck, verificar

appsucursal = Blueprint("appsucursal", __name__, template_folder="templates")

from sqlalchemy import exc
from flask import jsonify, render_template


@appsucursal.route("/alta_sucursal", methods=["GET", "POST"])
@tokenCheck
def alta_sucursal(info):
    try:
        # Verificar si el usuario tiene permisos de administrador
        if info["admin"]:
            if request.method == "GET":
                # Redirigir a la página de inicio de sesión si la solicitud es GET
                return render_template("/agregar_sucursal.html")
            else:
                # Obtener datos de la solicitud POST
                nombre = request.json.get("nombre")
                direccion = request.json.get("direccion")

                # Verificar si la sucursal ya existe
                existSucursal = Sucursal.query.filter_by(nombre=nombre).first()
                if existSucursal:
                    return jsonify({"message": "La sucursal ya existe"})

                # Crear la sucursal y guardar en la base de datos
                sucursal = Sucursal(nombre=nombre, direccion=direccion)
                db.session.add(sucursal)
                db.session.commit()

                # Respuesta exitosa con el token y la URL de redirección
                response = {
                    "status": "success",
                    "message": "Sucursal creada exitosamente",
                    "auth_token": info["auth_token"],
                    "redirect_url": "/agregar_sucursal.html",
                }
                return jsonify(response)
        response = {
            "status": "fail",
            "message": "no tienes permisos",
            "auth_token": info.auth_token,
            "redirect_url": "/main.html",
        }
        # Manejar el caso en el que el usuario no tiene permisos de administrador
        return jsonify(response)

    except exc.SQLAlchemyError as e:
        # Manejar excepciones de SQLAlchemy
        return jsonify({"status": "error", "message": str(e)})

    except Exception as e:
        # Manejar otras excepciones
        return jsonify({"status": "error", "message": str(e)})
