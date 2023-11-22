from flask import Blueprint, request, jsonify, render_template, redirect
from sqlalchemy import exc
from models import User, Venta
from app import db, bcrypt
from auth import tokenCheck, verificar

appventas = Blueprint("appventas", __name__, template_folder="templates")


@appventas.route("/altaventa", methods=["GET", "POST"])
def sign_post():
    try:
        token = request.args.get("token")
        verification_result = verificar(token)

        if "data" in verification_result:
            info = verification_result["data"]
            # Verificar si el usuario tiene permisos de administrador
            if info["admin"]:
                print("Si entre bro,si jala la verificacion")
                if request.method == "GET":
                    return render_template("agregar_venta.html")
                else:
                    venta = Venta(
                        fecha_venta=request.json["fecha_venta"],
                        monto_total=request.json["monto_total"],
                        sucursal_id=request.json["sucursal_id"],
                        empleado_clave=request.json["empleado_clave"],
                    )
                    # Agrega y commit a la base de datos
                    db.session.add(venta)
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
