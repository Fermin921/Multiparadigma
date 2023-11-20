from models import User
from functools import wraps
from flask import jsonify, request


def obtenerInfo(tokens):
    if tokens:
        resp = User.decode_auth_token(tokens)
        user = User.query.filter_by(id=resp["sub"]).first()
        if user:
            usuario = {
                "status": "success",
                "data": {
                    "user_id": user.id,
                    "email": user.email,
                    "admin": user.admin,
                    "registered_on": user.registered_on,
                },
            }
            return usuario
        else:
            error = {"status": "fail", "message": resp}
            return error


def tokenCheck(f):
    @wraps(f)
    def verificar(*args, **kwargs):
        token = None
        print(request.headers["token"])
        if "token" in request.headers:
            print("Que rollo si entre al primero")
            token = request.headers["token"]
        if not token:
            return jsonify({"token": "Token no valido"})
        try:
            info = obtenerInfo(token)
            print(info)
            if info["status"] == "fail":
                return jsonify({"message": "Token failed"})
        except Exception as e:
            print(e)
            return jsonify({"message": "Token invalid"})
        return f(info["data"], *args, **kwargs)

    return verificar


def verificar(token):
    if not token:
        return jsonify({"token": "Token no valido"})
    try:
        info = obtenerInfo(token)
        if info["status"] == "fail":
            return jsonify({"message": "Token failed"})
    except Exception as e:
        print(e)
        return jsonify({"message": "Token invalid"})
    return info
