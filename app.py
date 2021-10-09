from flask import Flask, render_template, request, redirect, url_for
from flask.templating import render_template
from forms import formlogin
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = os.urandom(32)

# Inicio navegación inicio de la aplicación ********************************************************
@app.route('/')
def inicio():
    return render_template('0-inicio.html') 

#Iniciando la construcción del forms########################################
#No es la versión definitiva, está en prueba
@app.route('/0-1-login/', methods=['GET', 'POST'])
def usuario_registrado():
    if request.method =="GET":
        formulario =formlogin()
        return render_template('0-1-login.html', form=formulario)

    else:
        formulario = formlogin(request.form)
        if formulario.validate_on_submit():
            #Condición que se debe cumplir para que cada boton redireccione a donde corresponde, hay valores de prueba
            return redirect(url_for('registrado_UF'))

            #return redirect(url_for('registrado_SA'))

            #return redirect(url_for('registrado_A'))
            #Condición que se debe cumplir para que cada boton redireccione a donde corresponde, hay valores de prueba
        return render_template('0-1-3-opciones_usuario_final_registrado.html', mensaje="Todos los campos son obligatorios.", form=formulario)

#@app.route('/registrado_UF/', methods=['GET', 'POST'])
#def usuario_registrado1():
    #if request.method =="GET":
        #formulario =formlogin()
        #return render_template('0-1-3-opciones_usuario_final_registrado.html',mensaje="Bienvenido.", form=formlogin())

    #else:
        #formulario = formlogin(request.form)
        #if formulario.validate_on_submit():
            #Condición que se debe cumplir para que cada boton redireccione a donde corresponde, hay valores de prueba
            #return render_template('0-1-3-opciones_usuario_final_registrado.html',mensaje="Bienvenido.", form=formlogin())
            #Condición que se debe cumplir para que cada boton redireccione a donde corresponde, hay valores de prueba
        #return render_template('0-1-3-opciones_usuario_final_registrado.html', mensaje="Todos los campos son obligatorios.", form=formulario)

#Fin la construcción del forms##############################################

@app.route('/0-2-opciones_invitado/', methods=['GET', 'POST'])
def opciones_invitado():
    return render_template('0-2-opciones_invitado.html')

# Fin navegación inicio de la aplicación ***********************************************************

#Inicio navegación login de la aplicación *********************************************************

@app.route('/0-1-3-opciones_usuario_final_registrado/', methods=['GET', 'POST'])
def opciones_usuario_final_registrado():
    return render_template('0-1-3-opciones_usuario_final_registrado.html') 

@app.route('/0-1-2-opciones_administrador/', methods=['GET', 'POST'])
def opciones_administrador():
    return render_template('0-1-2-opciones_administrador.html')

@app.route('/0-1-1-opciones_super_administrador/', methods=['GET', 'POST'])
def opciones_super_administrador():
    return render_template('0-1-1-opciones_super_administrador.html') 

#Fin navegación login de la aplicación *********************************************************

# Inicio Navegación usuario Final registrado SA **************************************************************************

@app.route('/0-1-1-1-consulta_datos_usuario')
def consulta_datos_usuario():
    return render_template('0-1-1-1-consulta_datos_usuario.html')

@app.route('/0-1-1-1-1-modificar_datos_usuario')
def modificar_datos_usuario_SA():
    return render_template('0-1-1-1-1-modificar_datos_usuario.html')    

# Fin Navegación usuario final registrado SA *************************************    

# Inicio Navegación Gestion de Usuarios Administradores SA **************************************************************************

@app.route('/0-1-1-2-gestion_usuarios_administradores')
def gestion_usuarios_administradores():
    return render_template('0-1-1-2-gestion_usuarios_administradores.html')

@app.route('/0-1-1-2-1-agregar_usuario_administrador_crud')
def agregar_usuario_administrador_crud():
    return render_template('0-1-1-2-1-agregar_usuario_administrador_crud.html')

@app.route('/0-1-1-2-2-modificar_usuario_administrador_crud')
def modificar_usuario_administrador_crud():
    return render_template('0-1-1-2-2-modificar_usuario_administrador_crud.html')


# Fin Navegación Gestion de Usuarios Administradores SA *************************************    


# Inicio Navegación Gestion de Usuarios Finales SA **************************************************************************

@app.route('/0-1-1-3-gestion_usuarios_finales')
def gestion_usuarios_finales():
    return render_template('0-1-1-3-gestion_usuarios_finales.html')

@app.route('/0-1-1-3-1-agregar_usuario_final_crud')
def agregar_usuario_final_crud():
    return render_template('0-1-1-3-1-agregar_usuario_final_crud.html')

@app.route('/0-1-1-3-2-modificar_usuario_final_crud')
def modificar_usuario_final_crud():
    return render_template('0-1-1-3-2-modificar_usuario_final_crud.html')

# Fin Navegación  Gestion de Usuarios Finales SA *************************************   
 
# Inicio Navegación Gestion de Habitaciones SA **************************************************************************

@app.route('/0-1-1-4-gestion_habitaciones')
def gestion_habitaciones():
    return render_template('0-1-1-4-gestion_habitaciones.html')

@app.route('/0-1-1-4-1-nueva_habitacion')
def nueva_habitacion():
    return render_template('0-1-1-4-1-nueva_habitacion.html')

@app.route('/0-1-1-4-2-modificar_habitacion')
def modificar_habitacion():
    return render_template('0-1-1-4-2-modificar_habitacion.html')

@app.route('/0-1-1-4-3-consulta_comentarios_habitacion_usuario')
def consulta_comentarios_habitacion_usuario_SA():
    return render_template('0-1-1-4-3-consulta_comentarios_habitacion_usuario.html')

@app.route('/0-1-1-4-4-consulta_reservas')
def consulta_reservas():
    return render_template('0-1-1-4-4-consulta_reservas.html')


# Fin Navegación  Gestion de Habitaciones SA *************************************  

# Inicio Navegación Restringir comentarios SA **************************************************************************

@app.route('/0-1-1-5-restringir_comentarios')
def restringir_comentarios():
    return render_template('0-1-1-5-restringir_comentarios.html')

# Fin Navegación Restringir comentarios SA *************************************


# Inicio *******************    Navegación usuario final registrado *************************************
@app.route('/0-1-3-1-consulta_datos_usuario', methods=['GET', 'POST'])
def consulta_datos_usuario_final():
    return render_template('0-1-3-1-consulta_datos_usuario.html')

@app.route('/0-1-3-opciones_usuario_final_registrado', methods=['GET', 'POST'])
def consulta_opciones_usuario_final_registrado():
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

@app.route('/0-1-3-4-2-modificar_reservas', methods=['GET', 'POST'])
def modificar_reservas():
    return render_template('0-1-3-4-2-modificar_reservas.html')

@app.route('/0-1-3-4-1-crear_reservas', methods=['GET', 'POST'])
def crear_reservas():
    return render_template('0-1-3-4-1-crear_reservas.html')


# Templates con ruteos actualizados al Git
# 0-1-3-opciones_usuario_final_registrado (ok)
#  0-1-3-1-consulta_datos_usuario (ok)
#  0-1-3-2-consulta_habitaciones_disponibles_usuario_final (ok)
#  0-1-3-3-gestion_habitaciones_reservadas_usuario_final (ok)
#  0-1-3-4-modulo_reservas.html (ok)
#  0-1-3-1-1-modificar_datos_usuario.html (ok)
#  0-1-3-2-1-consulta_comentarios_habitacion_usuario.html (ok)
#  0-1-3-2-4-consulta_reservas.html
#  0-1-3-3-1-modificar_comentarios_habitacion (ok)
#  0-1-3-3-2-calificar_habitaciones.html (ok)
#  0-1-3-4-1-crear_reservas.html (ok)
#  0-1-3-4-2-modificar_reservas.html

# Templates con ruteos actualizados al Git del Super Administrador
# 0-1-1-Opciones Usuario SuperAdministrador (ok)
# 0-1-1-5-Restringir Comentarios (ok)
# 0-1-1-1-1-Modifica datos Usuario Registrado (ok)
# 0-1-1-1-Consulta datos Usuario Registrado (ok)
# 0-1-1-2-Gestión de Usuarios Administradores (ok)
# 0-1-1-2-1-Registro Nuevo Usuario Administrador (ok)
# 0-1-1-2-2-Modifica Datos Usuario Administrador (ok)

# Fin ************************    Navegación usuario final registrado *************************************

# Inicio Navegación usuario invitado  *****************************************
# 0-2-opciones_invitado (ok)
# 0-2-1-registro_nuevo_usuario (ok)
# 0-2-2-consulta_habitaciones_disponibles (ok)
# 0-2-2-1-consulta_comentarios_habitacion (ok)

@app.route('/0-2-1-registro_nuevo_usuario', methods=['POST'])
def registro_nuevo_usuario_final():
    return render_template('0-2-1-registro_nuevo_usuario.html')

@app.route('/0-2-2-consulta_habitaciones_disponibles', methods=['GET'])
def consulta_habitacion_disponibles():
    return render_template('0-2-2-consulta_habitaciones_disponibles.html')

@app.route('/0-2-2-1-consulta_comentarios_habitacion', methods=['GET'])
def consulta_comentario_habitacion():
    return render_template('0-2-2-1-consulta_comentarios_habitacion.html')

# Fin Navegación usuario invitado  *****************************************



# ********************************************************
# ******** Inicio Navegación usuario Adminsitrador *******
# ********************************************************

# opciones_administrador se encuentra creada en la parte superior

# Primera rama de navegación de usuario administrador
@app.route('/0-1-2-1-consulta_datos_usuario', methods=['GET', 'POST'])
def consulta_datos_usuario_admin():
    return render_template('0-1-2-1-consulta_datos_usuario.html')

@app.route('/0-1-2-1-1-modificar_datos_usuario', methods=['GET', 'POST'])
def modificar_datos_usuario_admin():
    return render_template('0-1-2-1-1-modificar_datos_usuario.html')


# Segunda rama de navegación de usuario administrador

@app.route('/0-1-2-2-gestion_usuarios_finales', methods=['GET', 'POST'])
def gestion_usuarios_finales_admin():
    return render_template('0-1-2-2-gestion_usuarios_finales.html')

@app.route('/0-1-2-2-2-modificar_usuario_final_crud')
def agregar_usuario_final_crud_admin():
    return render_template('0-1-2-2-2-modificar_usuario_final_crud.html')

@app.route('/0-1-2-2-2-modificar_usuario_final_crud')
def modificar_usuario_final_crud_admin():
    return render_template('0-1-2-2-2-modificar_usuario_final_crud.html')

# Tercera rama de navegación usuario administrador
@app.route('/0-1-2-3-gestion_habitaciones', methods=['GET', 'POST'])
def gestion_habitaciones_admin():
    return render_template('0-1-2-3-gestion_habitaciones.html')

@app.route('/0-1-2-3-1-nueva_habitacion')
def nueva_habitacion_admin():
    return render_template('0-1-2-3-1-nueva_habitacion.html')

@app.route('/0-1-2-3-2-modificar_habitacion')
def modificar_habitacion_admin():
    return render_template('0-1-2-3-2-modificar_habitacion')

@app.route('/0-1-2-3-3-consulta_comentarios_habitacion_usuario')
def consulta_comentarios_habitacion_usuario_admin():
    return render_template('0-1-2-3-3-consulta_comentarios_habitacion_usuario.html')

# ********************************************************
# ********** Fin Navegación usuario Adminsitrador ********
# ********************************************************

