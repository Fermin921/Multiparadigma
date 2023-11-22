from flask import Blueprint, request, jsonify, render_template, redirect
from sqlalchemy import exc
from models import User, Producto
from app import db, bcrypt
from auth import tokenCheck, verificar

approducto = Blueprint("approducto", __name__, template_folder="templates")


@approducto.route("/altaproducto", methods=["GET", "POST"])
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
                    return render_template("agregar_producto.html")
                else:
                    producto = Producto(
                        sabor=request.json["sabor"],
                        stock=request.json["stock"],
                        categoria=request.json["categoria"],
                        sucursal_id=request.json["sucursal_id"],
                    )
                    db.session.add(producto)
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
