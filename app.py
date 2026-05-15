from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def inicio():
    titulo = "Inicio"
    usuario = "Valentina"
    mensaje = "Bienvenida a mi pagina Flask"
    fecha = datetime.now().strftime("%Y-%m-%d")

    return render_template(
        "index.html",
        titulo=titulo,
        usuario=usuario,
        mensaje=mensaje,
        fecha=fecha
    )

@app.route("/acerca")
def acerca():
    return render_template("acerca.html")

@app.route("/contacto")
def contacto():
    return render_template("contacto.html")

if __name__ == "__main__":
    app.run(debug=True)