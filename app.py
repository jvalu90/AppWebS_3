from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def inicio():
    return render_template('0-inicio.html') #Algo no está funcionando aquí, realizar verificación

# Inicio de la aplicación ********************************************************

@app.route('/usuario_registrado/', methods=['GET', 'POST'])
def usuario_registrado():
    return render_template('0-1-login.html') #Algo no está funcionando aquí, realizar verificación

# Inicio Navegación usuario Final registrado SA **************************************************************************

@app.route('/0-1-1-1-consulta_datos_usuario')
def consulta_datos_usuario():
    return render_template('0-1-1-1-consulta_datos_usuario.html')

# Fin Navegación usuario final registrado SA *************************************    

# Inicio Navegación Gestion de Usuarios Administradores SA **************************************************************************

@app.route('/0-1-1-2-gestion_usuarios_administradores')
def gestion_usuarios_administradores():
    return render_template('0-1-1-2-gestion_usuarios_administradores.html')

# Fin Navegación Gestion de Usuarios Administradores SA *************************************    


# Inicio Navegación Gestion de Usuarios Finales SA **************************************************************************

@app.route('/0-1-1-3-gestion_usuarios_finales')
def gestion_usuarios_finales():
    return render_template('0-1-1-3-gestion_usuarios_finales.html')

# Fin Navegación  Gestion de Usuarios Finales SA *************************************   
 
# Inicio Navegación Gestion de Habitaciones SA **************************************************************************

@app.route('/0-1-1-4-gestion_habitaciones')
def gestion_habitaciones():
    return render_template('0-1-1-4-gestion_habitaciones.html')

# Fin Navegación  Gestion de Habitaciones SA *************************************  

# Inicio Navegación Restringir comentarios SA **************************************************************************

@app.route('/0-1-1-5-restringir_comentarios')
def restringir_comentarios():
    return render_template('0-1-1-5-restringir_comentarios.html')

# Fin Navegación Restringir comentarios SA *************************************


# Inicio Navegación usuario final registrado *************************************
@app.route('/0-1-3-1-consulta_datos_usuario')
def consulta_datos_usuario_final():
    return render_template('0-1-3-1-consulta_datos_usuario.html')

@app.route('/0-1-3-opciones_usuario_final_registrado')
def opciones_usuario_final_registrado():
    return render_template('0-1-3-opciones_usuario_final_registrado.html')

# Fin Navegación usuario final registrado *************************************
