from flask import Blueprint, request, jsonify, render_template, redirect
from sqlalchemy import exc
from models import User
from app import db, bcrypt
from auth import tokenCheck, verificar

appuser = Blueprint("appuser", __name__, template_folder="templates")


@appuser.route("/")
@appuser.route("/main")
def main():
    return render_template("main.html")


@appuser.route("/login", methods=["GET", "POST"])
def login_post():
    if request.method == "GET":
        token = request.args.get("token")
        if token:
            info = verificar(token)
            if info["status"] != "fail":
                responseObject = {
                    "status": "success",
                    "message": "valid_token",
                    "info": info,
                }
                return jsonify(responseObject)
        return render_template("/login.html")
    else:
        email = request.json["email"]
        password = request.json["password"]
        usuario = User(email=email, password=password)
        searchUser = User.query.filter_by(email=email).first()
        if searchUser:
            validation = bcrypt.check_password_hash(searchUser.password, password)
            if validation:
                auth_token = usuario.encode_auth_token(user_id=searchUser.id)
                response = {
                    "status": "success",
                    "message": "Login exitoso",
                    "auth_token": auth_token,
                    "redirect_url": "/altaempleado.html",
                }
                return jsonify(response)
        return jsonify({"message": "Datos incorrectos"})


@appuser.route("/registro", methods=["GET", "POST"])
def registro_post():
    if request.method == "GET":
        return render_template("registro.html")
    else:
        try:
            email = request.json["email"]
            password = request.json["password"]
            usuario = User(email=email, password=password)
            user_exists = User.query.filter_by(email=email).first()

            if not user_exists:
                db.session.add(usuario)
                db.session.commit()
                responseObject = {
                    "status": "success",
                    "message": "Registro Exitoso",
                    "redirect_url": "/main.html",
                }
            else:
                responseObject = {"status": "error", "message": "Ya existe el usuario"}
        except exc.SQLAlchemyError as e:
            responseObject = {"status": "error", "message": str(e)}

        return jsonify(responseObject)
