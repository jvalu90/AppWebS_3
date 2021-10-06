from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('0-1-1-1-Consulta datos Usuario Registrado')
def index():
    return render_template('0-1-1-1-consulta_datos_usuario.html')