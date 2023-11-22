from flask import Blueprint, request, jsonify, render_template, redirect
from sqlalchemy import exc
from models import User, Empleado
from app import db, bcrypt
from auth import tokenCheck, verificar
import datetime

appempleado = Blueprint("appempleado", __name__, template_folder="templates")


@appempleado.route("/altaempleado", methods=["GET", "POST"])
@tokenCheck
def sign_post(info):
    try:
        if info["admin"]:
            print("Si entre bro,si jala la verificacion")
            if request.method == "GET":
                return render_template("agregar_empleado.html")
            else:
                # Resto del código para manejar la solicitud POST
                # Obtener la fecha de nacimiento desde la solicitud
                fecha_nacimiento_str = request.json["fecha_nacimiento"]
                fecha_nacimiento = datetime.datetime.strptime(
                    fecha_nacimiento_str, "%Y-%m-%d"
                )
                # Calcular la edad
                edad = datetime.datetime.utcnow().year - fecha_nacimiento.year
                # Crea el objeto Empleado
                empleado = Empleado(
                    clave=request.json["clave"],
                    rfc=request.json["rfc"],
                    nombres=request.json["nombres"],
                    apellidos=request.json["apellidos"],
                    fecha_nacimiento=fecha_nacimiento,
                    edad=edad,
                    sueldo=request.json["sueldo"],
                    area_laboral=request.json["area_laboral"],
                    sucursal_id=request.json["sucursal"],
                )
                # Agrega y commit a la base de datos
                db.session.add(empleado)
                db.session.commit()
                responseObject = {
                    "status": "success",
                    "message": "Registro Exitoso",
                }
            return jsonify(responseObject)
        else:
            print("Que rollo no entra")
            # Si no hay "data", manejar el error
            return jsonify(
                {"message": verification_result.get("message", "Error desconocido")}
            )

    except exc.SQLAlchemyError as e:
        # Manejar otras excepciones
        responseObject = {"status": "error", "message": str(e)}
        return jsonify(responseObject)


# @appempleado.route("/altaempleado", methods=["GET", "POST"])
# def sign_post():
#     try:
#         token = request.args.get("token")
#         info = verificar(token)["data"]
#         print(info)
#         # Verificar si el usuario tiene permisos de administrador
#         if info["admin"]:
#             if request.method == "GET":
#                 return render_template("agregar_empleado.html")
#             else:
#                 # Obtener la fecha de nacimiento desde la solicitud
#                 fecha_nacimiento_str = request.json["fecha_nacimiento"]
#                 fecha_nacimiento = datetime.datetime.strptime(
#                     fecha_nacimiento_str, "%Y-%m-%d"
#                 )

#                 # Calcular la edad
#                 edad = datetime.datetime.utcnow().year - fecha_nacimiento.year

#                 # Crea el objeto Empleado
#                 empleado = Empleado(
#                     clave=request.json["clave"],
#                     rfc=request.json["rfc"],
#                     nombres=request.json["nombres"],
#                     apellidos=request.json["apellidos"],
#                     fecha_nacimiento=fecha_nacimiento,
#                     edad=edad,
#                     sueldo=request.json["sueldo"],
#                     area_laboral=request.json["area_laboral"],
#                     sucursal_id=request.json["sucursal"],
#                 )

#                 # Agrega y commit a la base de datos
#                 db.session.add(empleado)
#                 db.session.commit()

#                 responseObject = {"status": "success", "message": "Registro Exitoso"}
#                 return jsonify(responseObject)

#         # Si no hay permisos de administrador
#         responseObject = {"status": "error", "message": "Acceso no autorizado"}
#         return jsonify(responseObject)

#     except exc.SQLAlchemyError as e:
#         # Manejar otras excepciones
#         responseObject = {"status": "error", "message": str(e)}
#         return jsonify(responseObject)
