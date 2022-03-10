from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "SecretKey1234"

#Indicamos la ruta de nuestra aplicacion (URL)
@app.route("/hola")
def index():
    flash("¿Cuál es tu nombre?")
    return render_template("index.html")

@app.route("/saludar", methods=["POST","GET"])
def saludar():
    flash("Bienvenido " + str(request.form['name_input']) + ", me alegro de verte!")
    return render_template("index.html")
