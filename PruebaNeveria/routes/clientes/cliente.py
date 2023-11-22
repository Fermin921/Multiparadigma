from flask import Blueprint, request, jsonify, render_template, redirect
from sqlalchemy import exc
from models import User, Cliente
from app import db, bcrypt
from auth import tokenCheck, verificar
import datetime

appcliente = Blueprint("appcliente", __name__, template_folder="templates")


@appcliente.route("/altaempleado", methods=["GET", "POST"])
def sign_post():
    try:
        token = request.args.get("token")
        verification_result = verificar(token)["data"]

        if "data" in verification_result:
            info = verification_result["data"]
            # Verificar si el usuario tiene permisos de administrador
            if info["admin"]:
                print("Si entre bro,si jala la verificacion")
                if request.method == "GET":
                    return render_template("agregar_cliente.html")
                else:
                    cliente = Cliente(
                        nombre_empresa=request.json("nombre_empresa"),
                        direccion=request.json("direccion"),
                        fecha_registro=datetime.datetime.utcnow(),
                        sucursal_id=request.json("sucursal_id"),
                    )
                    # Agrega y commit a la base de datos
                    db.session.add(cliente)
                    db.session.commit()
                    responseObject = {
                        "status": "success",
                        "message": "Registro Exitoso",
                    }
                return jsonify(responseObject)
        else:
            # Si no hay "data", manejar el error
            return jsonify(
                {"message": verification_result.get("message", "Error desconocido")}
            )

    except exc.SQLAlchemyError as e:
        # Manejar otras excepciones
        responseObject = {"status": "error", "message": str(e)}
        return jsonify(responseObject)
