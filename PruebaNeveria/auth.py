from models import User
from functools import wraps
from flask import jsonify, request


def obtenerInfo(token):
    if token:
        resp = User.decode_auth_token(token)
        print(resp)
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
            error = {"status": "fail", "message": "Usuario no encontrado"}
            return error


def tokenCheck(f):
    @wraps(f)
    def verificar(*args, **kwargs):
        token = None
        if "token" in request.headers:
            token = request.headers["token"]
        if not token:
            return jsonify({"message": "Token no encontrado"})
        try:
            info = obtenerInfo(token)
            print(info)
            if info["status"] == "fail":
                return jsonify({"message": info["message"]})
        except Exception as e:
            print(e)
            return jsonify({"message": "Error"})
        return f(info.get("data"), *args, **kwargs)

    return verificar


def verificar(token):
    if not token:
        return {"status": "fail", "message": "Token no encontrado"}
    try:
        info = obtenerInfo(token)
        return info
    except Exception as e:
        print(e)
        return {"status": "fail", "message": "Error"}


# def verificar(token):
#     if not token:
#         return jsonify({"token": "Token no valido"})
#     try:
#         info = obtenerInfo(token)
#         if info["status"] == "fail":
#             return jsonify({"message": "Token failed"})
#     except Exception as e:
#         print(f"Error al verificar el token: {e}")
#         return jsonify({"message": "Token invalid"})
#     return info
