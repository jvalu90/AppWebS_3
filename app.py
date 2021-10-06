from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def inicio():
    return render_template('0-inicio.html') #Algo no está funcionando aquí, realizar verificación

# Inicio de la aplicación ********************************************************

@app.route('/usuario_registrado/', methods=['GET', 'POST'])
def usuario_registrado():
    return render_template('0-1-login.html') #Algo no está funcionando aquí, realizar verificación

# Login **************************************************************************

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
