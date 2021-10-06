from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Inicio navegación inicio de la aplicación ********************************************************
@app.route('/')
def inicio():
    return render_template('0-inicio.html') 

@app.route('/0-1-login.html/', methods=['GET', 'POST'])
def usuario_registrado():
    return render_template('0-1-login.html')

@app.route('/0-2-opciones_invitado/', methods=['GET', 'POST'])
def opciones_invitado():
    return render_template('0-2-opciones_invitado.html')

# Fin navegación inicio de la aplicación ***********************************************************

#Inicio navegación login de la aplicación *********************************************************


#Fin navegación login de la aplicación *********************************************************

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

@app.route('/0-1-3-2-consulta_habitaciones_disponibles_usuario_final', methods=['GET', 'POST'])
def consulta_habitaciones_disponibles_usuario_final():
    return render_template('0-1-3-2-consulta_habitaciones_disponibles_usuario_final.html')

@app.route('/0-1-3-3-gestion_habitaciones_reservadas_usuario_final', methods=['GET', 'POST'])
def gestion_habitaciones_reservadas_usuario_final():
    return render_template('0-1-3-3-gestion_habitaciones_reservadas_usuario_final.html')

@app.route('/0-1-3-4-modulo_reservas', methods=['GET', 'POST'])
def modulo_reservas():
    return render_template('0-1-3-4-modulo_reservas.html')

@app.route('/0-1-3-1-1-modificar_datos_usuario', methods=['GET', 'POST'])
def modificar_datos_usuario():
    return render_template('0-1-3-1-1-modificar_datos_usuario.html')

@app.route('/0-1-3-2-1-consulta_comentarios_habitacion_usuario', methods=['GET', 'POST'])
def consulta_comentarios_habitacion_usuario():
    return render_template('0-1-3-2-1-consulta_comentarios_habitacion_usuario.html')

@app.route('/0-1-3-3-1-modificar_comentarios_habitacion', methods=['GET', 'POST'])
def modificar_comentarios_habitacion():
    return render_template('0-1-3-3-1-modificar_comentarios_habitacion.html')

@app.route('/0-1-3-3-2-calificar_habitaciones', methods=['GET', 'POST'])
def calificar_habitaciones():
    return render_template('0-1-3-3-2-calificar_habitaciones.html')

# Templates con ruteos actualizados al Git
# 0-1-3-opciones_usuario_final_registrado 
#  0-1-3-1-consulta_datos_usuario
#  0-1-3-2-consulta_habitaciones_disponibles_usuario_final
#  0-1-3-3-gestion_habitaciones_reservadas_usuario_final
#  0-1-3-4-modulo_reservas.html

# Fin Navegación usuario final registrado *************************************

# Inicio Navegación usuario invitado  *****************************************


# Fin Navegación usuario invitado  *****************************************
