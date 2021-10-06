from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/0-1-1-1-consulta_datos_usuario')
def consulta_datos_usuario():
    return render_template('0-1-1-1-consulta_datos_usuario.html')

# Inicio Navegación usuario final registrado *************************************
@app.route('/0-1-3-1-consulta_datos_usuario')
def consulta_datos_usuario_final():
    return render_template('0-1-3-1-consulta_datos_usuario.html')

@app.route('/0-1-3-opciones_usuario_final_registrado')
def opciones_usuario_final_registrado():
    return render_template('0-1-3-opciones_usuario_final_registrado.html')

# Fin Navegación usuario final registrado *************************************
