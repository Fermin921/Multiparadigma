from flask import Flask, url_for, render_template, request, abort
from werkzeug.exceptions import abort
from werkzeug.utils import redirect
import logging

app = Flask(__name__)

logging.basicConfig(filename="error.log", level=logging.DEBUG)


@app.route("/")
def index():
    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        redirect("/")
    else:
        return render_template("login.html")


@app.route("/juego", methods=["POST"])
def agregarJuego():
    try:
        token = request.headers.get({"token"})
        app.logger.debug(f"Token: {token}")
        info = request.get_json()
        nombre = info["nombre"]
        precio = info["precio"]
        return f"Nombre {nombre} , Precioo: {precio}"
    except:
        return abort(404)


@app.route("/juego/<int:idJuego>")
def obtenerJuego(idJuego):
    return f"ID Juego {idJuego}"


@app.errorhandler(404)
def paginaNoEncontrada(error):
    return render_template("error.html")
