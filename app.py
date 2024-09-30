from flask import Flask, render_template, request, redirect, url_for, flash

from cola import Cola
from pila import Pila
from utils import modificar_estructura

app = Flask(__name__)
app.config["SECRET_KEY"] = "wriqqj2%l-sj@i@v-l0x%yj$&_(rw&%6r0z$vgfyni5&=mn-76"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/crear", methods=["POST"])
def crear_estructura():
    tipo = request.form.get("tipo")
    if tipo == "pila":
        global pila
        pila = Pila()
    elif tipo == "cola":
        global cola
        cola = Cola()
    return redirect(url_for("index"))


@app.route("/agregar", methods=["POST"])
def agregar_elemento():
    tipo = request.form.get("tipo")
    valor = request.form.get("valor")
    valores = map(int, valor.split())
    try:
        if tipo == "pila":
            for v in valores:
                pila.apilar(v)
        elif tipo == "cola":
            for v in valores:
                cola.encolar(v)
    except NameError:
        flash(
            "Aún no has creado la {}. Por favor, créala primero.".format(tipo), "danger"
        )
    return redirect(url_for("index"))


@app.route("/eliminar", methods=["POST"])
def eliminar_elemento():
    tipo = request.form.get("tipo")
    try:
        if tipo == "pila":
            pila.desapilar()
        elif tipo == "cola":
            cola.desencolar()
    except NameError:
        flash(
            "Aún no has creado la {}. Por favor, créala primero.".format(tipo), "danger"
        )
    return redirect(url_for("index"))


@app.route("/modificar", methods=["POST"])
def modificar():
    tipo = request.form.get("tipo")
    valor = int(request.form.get("valor"))
    try:
        if tipo == "pila":
            modificar_estructura(pila, valor)
        elif tipo == "cola":
            modificar_estructura(cola, valor)
    except NameError as e:
        flash(f"Aún no has creado la {tipo}. Por favor, créala primero. {e}", "danger")
    return redirect(url_for("index"))


@app.route("/mostrar")
def mostrar_estructura():
    tipo = request.args.get("tipo")
    try:
        if tipo == "pila":
            elementos = pila.imprimir()
        elif tipo == "cola":
            elementos = cola.imprimir()
        else:
            elementos = []
    except NameError:
        flash(
            "Aún no has creado la {}. Por favor, créala primero.".format(tipo), "danger"
        )
        elementos = []  # Asignar una lista vacía para evitar errores en el template
    return render_template("mostrar.html", elementos=elementos, tipo=tipo)


if __name__ == "__main__":
    app.run(debug=True)
