from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def inicio():
    # Variables dinámicas
    titulo = "Mi página dinámica con Flask"
    usuario = "Valentina"
    mensaje = "Bienvenida a mi sitio web con datos desde Python"
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return render_template(
        "index.html",
        titulo=titulo,
        usuario=usuario,
        mensaje=mensaje,
        fecha=fecha
    )

if __name__ == "__main__":
    app.run(debug=True)