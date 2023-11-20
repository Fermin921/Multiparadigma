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


@appuser.route("/loginprueba")
def prubea():
    return render_template("index.html")


@appuser.route("/login", methods=["GET", "POST"])
def login_post():
    if request.method == "GET":
        token = request.args.get("token")
        if token:
            info = verificar(token)
            if info["status"] != "fail":
                responseObject = {
                    "status": "success",
                    "message": "valid token",
                    "info": info,
                }
                return jsonify(responseObject)
        return render_template("../sucursal/templates/index.html")
    else:
        email = request.json["email"]
        password = request.json["password"]
        print(request.json)
        usuario = User(email=email, password=password)
        searchUser = User.query.filter_by(email=email).first()
        if searchUser:
            validation = bcrypt.check_password_hash(searchUser.password, password)
            if validation:
                auth_token = usuario.encode_auth_token(user_id=searchUser.id)
                responseObject = {
                    "status": "success",
                    "login": "Loggin exitoso",
                    "auth_token": auth_token,
                }
                return jsonify(responseObject)
        return jsonify({"message": "Datos incorrectos"})
