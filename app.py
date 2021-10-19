from flask import Flask, render_template, request, redirect, url_for, session, g
from flask.templating import render_template
from wtforms.validators import Length
from forms import formcancelarreserva, formlogin, FormCalificarHabitacion, formmodificarreserva, formreservanueva, formreservas, formcancelarreserva, formreservasadmin, formreservanuevaadmin
from forms import formreservassuperadmin, formreservanuevasuperadmin, formmodificarreservasuperadmin, formcancelarreservasuperadmin
from forms import formmodificarreservaadmin, formcancelarreservaadmin,FormAgregarUsuarioFinalCRUD,FormModificarUsuarioFinalCRUD,FormAgregarUsuarioAdmonCRUD,FormModificarUsuarioAdmonCRUD,FormModificarUsuarioRegistrado,FormCrearUsuarioRegistrado
import os
import functools
from werkzeug.utils import redirect
from models import reservas,usuario_final,usuario_administrador,login

app = Flask(__name__)

app.config['SECRET_KEY'] = os.urandom(32)

#Decorador para verificar que el usuario es autenticado
#Tan pronto esté listo debemos insertar en todas las vistas el decorador
#@login_required
def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect( url_for('usuario_registrado') )

        return view(**kwargs)

    return wrapped_view

@app.before_request
def cargar_usuario_autenticado():
    nombre_usuario = session.get('nombre_usuario')
    if nombre_usuario is None:
        g.user = None
    else:
        g.user = login.cargar(nombre_usuario)

#Falta implementar el botón cerrar sesión en todas las vistas
@app.route("/logout/")
@login_required
def logout():
    session.clear()
    return redirect( url_for('usuario_registrado') )

# La metodología propuesta es la siguiente: 
# funciones para conectar base de datos (bd.py)
# funciones para tratar los datos (models.py) entre el frontend y el backend
# funciones para capturar los datos de los usuarios (forms.py)
# funciones para interactuar con el frontend (app.py)

# Inicio navegación inicio de la aplicación ********************************************************
@app.route('/')
def inicio():
    return render_template('0-inicio.html') 

@app.route('/0-2-opciones_invitado/', methods=['GET', 'POST'])
def opciones_invitado():
    return render_template('0-2-opciones_invitado.html')

# Fin navegación inicio de la aplicación ***********************************************************

# Inicio navegación Login **************************************************************************

#@app.route('/0-1-login/', methods=['GET', 'POST'])
#def usuario_registrado():
#    if request.method =="GET":
#        formulario =formlogin()
#        return render_template('0-1-login.html', form=formulario)
#    else:
#        formulario = formlogin(request.form)
#        if formulario.validate_on_submit() and formulario.tipoUsuario.data == "UF":        
#            return redirect(url_for('registrado_UF'))
#        elif formulario.validate_on_submit() and formulario.tipoUsuario.data == "SA":          
#            return redirect(url_for('registrado_SA'))
#        elif formulario.validate_on_submit() and formulario.tipoUsuario.data == "A":
#            return redirect(url_for('registrado_A'))
#        return render_template('0-1-login.html', mensaje="Todos los campos son obligatorios.", form=formulario)

@app.route('/0-1-login/', methods=['GET', 'POST'])
def usuario_registrado():
    if request.method =="GET":
        formulario =formlogin()
        return render_template('0-1-login.html', form=formulario)
    else:
        formulario = formlogin(request.form)

        usr = formulario.user.data.replace("'","")
        pwd = formulario.password.data.replace("'","")

        obj_login = login(usr,pwd,"","","")

        if obj_login.autenticar() and formulario.tipoUsuario.data == "UF": 
            session.clear()
            session["nombre_usuario"] = usr
            return redirect( url_for('registrado_UF'))

        if obj_login.autenticar() and formulario.tipoUsuario.data == "SA": 
            session.clear()
            session["nombre_usuario"] = usr
            return redirect( url_for('registrado_SA'))

        if obj_login.autenticar() and formulario.tipoUsuario.data == "A": 
            session.clear()
            session["nombre_usuario"] = usr
            return redirect( url_for('registrado_A'))

        return render_template('0-1-login.html', mensaje="Nombre de usuario o contraseña incorrecta.", 
        form=formulario)

        # Código obsoleto con la implementación del Hash
        #if formulario.validate_on_submit() and formulario.tipoUsuario.data == "UF":        
        #    objeto_login =login.cargar(formulario.user.data,formulario.password.data,'UF')
        #    if objeto_login:
        #        session['id_usuario_logueado'] = objeto_login.id_usuario
        #        session['usuario_logueado'] = objeto_login.usuario
        #        return redirect(url_for('registrado_UF'))
        #        #return render_template('0-1-3-opciones_usuario_final_registrado.html', form=formulario)
        #    else: 
        #        formulario =formlogin()
        #        formulario.user.data = None
        #        formulario.password.data = None
        #        return render_template('0-1-login.html', mensaje="Usuario o contraseña de usuario final no son válidos.", form=formulario)

        #elif formulario.validate_on_submit() and formulario.tipoUsuario.data == "SA":          
        #    objeto_login =login.cargar(formulario.user.data,formulario.password.data,'SA')
        #    if objeto_login:
        #        session['id_usuario_logueado'] = objeto_login.id_usuario
        #        session['usuario_logueado'] = objeto_login.usuario
        #        return redirect(url_for('registrado_SA'))
        #        #return render_template('0-1-1-opciones_super_administrador.html', form=formulario)
        #    else: 
        #        formulario =formlogin()
        #        formulario.user.data = None
        #        formulario.password.data = None
        #        return render_template('0-1-login.html', mensaje="Usuario o contraseña de usuario SuperAdministrador no son válidos.", form=formulario)

        #elif formulario.validate_on_submit() and formulario.tipoUsuario.data == "A":
        #    objeto_login =login.cargar(formulario.user.data,formulario.password.data,'A')
        #    if objeto_login:
        #        session['id_usuario_logueado'] = objeto_login.id_usuario
        #        session['usuario_logueado'] = objeto_login.usuario
        #        return redirect(url_for('registrado_A'))
        #        #return render_template('0-1-3-opciones_usuario_final_registrado.html', form=formulario)
        #    else: 
        #        formulario =formlogin()
        #        formulario.user.data = None
        #        formulario.password.data = None
        #        return render_template('0-1-login.html', mensaje="Usuario o contraseña de usuario Administrador no son válidos.", form=formulario)

        #return render_template('0-1-login.html', mensaje="Todos los campos son obligatorios.", form=formulario)


@app.route('/0-1-3-opciones_usuario_final_registrado/', methods=['GET', 'POST'])
def registrado_UF():
    if request.method =="GET":
        formulario =formlogin()
        return render_template('0-1-3-opciones_usuario_final_registrado.html', form=formulario)

@app.route('/0-1-1-opciones_super_administrador/', methods=['GET', 'POST'])
def registrado_SA():
    if request.method =="GET":
        formulario =formlogin()
        return render_template('0-1-1-opciones_super_administrador.html', form=formulario)

@app.route('/0-1-2-opciones_administrador/', methods=['GET', 'POST'])
def registrado_A():
    if request.method =="GET":
        formulario =formlogin()
        return render_template('0-1-2-opciones_administrador.html', form=formulario)

# Fin navegación Login ****************************************************************************

# Inicio Navegación usuario Final registrado SA **************************************************************************

@app.route('/0-1-1-1-consulta_datos_usuario')
def consulta_datos_usuario():
    return render_template('0-1-1-1-consulta_datos_usuario.html',lista=login.datos_usuario_logueado(session['id_usuario_logueado']))

#@app.route('/0-1-1-1-1-modificar_datos_usuario')
#def modificar_datos_usuario_SA():
#    return render_template('0-1-1-1-1-modificar_datos_usuario.html')    

@app.route('/0-1-1-1-1-modificar_datos_usuario', methods=['GET', 'POST'])
def modificar_datos_usuario_SA():
    if request.method =="GET":    
        objeto_usuario =usuario_final.cargar(session['id_usuario_logueado'])
        formulario = FormModificarUsuarioRegistrado()
        formulario.nombre.data = objeto_usuario.nombres
        formulario.documento.data = objeto_usuario.documento
        formulario.usuario.data = objeto_usuario.usuario
        formulario.contrasena1.data = objeto_usuario.contrasena
        formulario.contrasena2.data = objeto_usuario.contrasena
        return render_template('0-1-1-1-1-modificar_datos_usuario.html', form=formulario)
    else:
        formulario =FormModificarUsuarioRegistrado(request.form)
        objeto_usuario = usuario_administrador(session['id_usuario_logueado'], formulario.documento.data, formulario.nombre.data, formulario.contrasena1.data, 
                                'SA', 'SI', formulario.usuario.data)
        objeto_usuario.modificar()
        return render_template('0-1-1-1-consulta_datos_usuario.html',lista=login.datos_usuario_logueado(session['id_usuario_logueado']))

    # Fin Navegación usuario final registrado SA *************************************    

# Inicio Navegación Gestion de Usuarios Administradores SA **************************************************************************

@app.route('/0-1-1-2-gestion_usuarios_administradores', methods=["GET"])
def gestion_usuarios_administradores():
    return render_template('0-1-1-2-gestion_usuarios_administradores.html', lista=usuario_administrador.listado())

@app.route('/0-1-1-2-1-agregar_usuario_administrador_crud', methods=['GET', 'POST'])
def agregar_usuario_administrador_crud():
    if request.method =="GET":
        formulario =FormAgregarUsuarioAdmonCRUD()
        return render_template('0-1-1-2-1-agregar_usuario_administrador_crud.html', form=formulario)
    else:
        formulario =FormAgregarUsuarioAdmonCRUD(request.form)
        objeto_usuario = usuario_administrador(0, formulario.documento.data, formulario.nombre.data, formulario.documento.data, 
                                'A', 'SI', formulario.documento.data)
        # print (formulario.nombre.data)
        # por defecto al agregar un usuario el user y password se cargan por defecto con el documento de identidad
        if objeto_usuario.insertar():   
            return render_template('0-1-1-2-gestion_usuarios_administradores.html', lista=usuario_administrador.listado())
        else:
            return render_template('0-1-1-2-gestion_usuarios_administradores.html', lista=usuario_administrador.listado())    

@app.route('/0-1-1-2-2-modificar_eliminar_usuario_administrador_crud/<id_usuario>/<accion>', methods=["GET", 'POST'])
def modificar_eliminar_usuario_administrador_crud(id_usuario,accion):
    objeto_usuario =usuario_administrador.cargar(id_usuario)
    if accion=='modificar':
        formulario = FormModificarUsuarioAdmonCRUD()
        formulario.id_usuario.data = objeto_usuario.id_usuario
        formulario.nombre.data = objeto_usuario.nombres
        formulario.documento.data = objeto_usuario.documento
        formulario.activo.data = objeto_usuario.activo
        return render_template('0-1-1-2-2-modificar_usuario_administrador_crud.html',form = formulario)
    else:
        objeto_usuario.eliminar()
        return render_template('0-1-1-2-gestion_usuarios_administradores.html', lista=usuario_administrador.listado())


@app.route('/0-1-1-2-2-modificar_usuario_administrador_crud', methods=["GET", 'POST'])
def modificar_usuario_administrador_crud():
    formulario =FormModificarUsuarioAdmonCRUD(request.form)
    objeto_usuario = usuario_administrador(formulario.id_usuario.data, formulario.documento.data, formulario.nombre.data, formulario.documento.data, 
                                'A', formulario.activo.data, formulario.documento.data)
    objeto_usuario.modificar()
    return render_template('0-1-1-2-gestion_usuarios_administradores.html', lista=usuario_administrador.listado())

# Fin Navegación Gestion de Usuarios Administradores SA *************************************    


# Inicio Navegación Gestion de Usuarios Finales SA **************************************************************************

@app.route('/0-1-1-3-gestion_usuarios_finales', methods=["GET"])
def gestion_usuarios_finales():
    return render_template('0-1-1-3-gestion_usuarios_finales.html', lista=usuario_final.listado())

@app.route('/0-1-1-3-1-agregar_usuario_final_crud', methods=['GET', 'POST'])
def agregar_usuario_final_crud():
    if request.method =="GET":
        formulario =FormAgregarUsuarioFinalCRUD()
        return render_template('0-1-1-3-1-agregar_usuario_final_crud.html', form=formulario)
    else:
        formulario =FormAgregarUsuarioFinalCRUD(request.form)
        objeto_usuario = usuario_final(0, formulario.documento.data, formulario.nombre.data, formulario.documento.data, 
                                'UF', 'SI', formulario.documento.data)
        # por defecto al agregar un usuario el user y password se cargan por defecto con el documento de identidad
        if objeto_usuario.insertar():   
            return render_template('0-1-1-3-gestion_usuarios_finales.html', lista=usuario_final.listado())
        else:
            return render_template('0-1-1-3-gestion_usuarios_finales.html', lista=usuario_final.listado())    
   
@app.route('/0-1-1-3-2-modificar_eliminar_usuario_final_crud/<id_usuario>/<accion>', methods=["GET", 'POST'])
def modificar_eliminar_usuario_final_crud(id_usuario,accion):
    objeto_usuario =usuario_final.cargar(id_usuario)
    if accion=='modificar':
        formulario = FormModificarUsuarioFinalCRUD()
        formulario.id_usuario.data = objeto_usuario.id_usuario
        formulario.nombre.data = objeto_usuario.nombres
        formulario.documento.data = objeto_usuario.documento
        formulario.activo.data = objeto_usuario.activo
        return render_template('0-1-1-3-2-modificar_usuario_final_crud.html',form = formulario)
    else:
        objeto_usuario.eliminar()
        return render_template('0-1-1-3-gestion_usuarios_finales.html', lista=usuario_final.listado())

@app.route('/0-1-1-3-2-modificar_usuario_final_crud', methods=["GET", 'POST'])
def modificar_usuario_final_crud():
    formulario =FormModificarUsuarioFinalCRUD(request.form)
    objeto_usuario = usuario_final(formulario.id_usuario.data, formulario.documento.data, formulario.nombre.data, formulario.documento.data, 
                                'UF', formulario.activo.data, formulario.documento.data)
    objeto_usuario.modificar()
    return render_template('0-1-1-3-gestion_usuarios_finales.html', lista=usuario_final.listado())

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

@app.route('/0-1-1-4-4-consulta_reservas', methods=['GET', 'POST'])
def consulta_reservas():
    if request.method =="GET":
        formulario =formreservassuperadmin()
        lista_habitaciones = reservas.listado_choices_habitaciones()
        #for i in lista:
            #lista_choices = lista[0][i]
        # Aquí es necesario crear el vector de choices
        #FORMULARIO.BEDROOM.CHOICES 
        return render_template('0-1-1-4-4-consulta_reservas.html', form=formulario, mostrar = 0)

    else:  
        formulario = formreservassuperadmin(request.form)
        if formulario.validate_on_submit():
            return render_template('0-1-1-4-4-consulta_reservas.html', form=formulario, 
                    lista=reservas.listado(0, formulario.bedroom.data, formulario.initialdate.data, 
                    formulario.finaldate.data), mostrar = 1)
        return render_template('0-1-1-4-4-consulta_reservas.html', mensaje="Todos los campos son obligatorios.", form=formulario)

@app.route('/0-1-1-4-4-1-crear_reservas', methods=['GET', 'POST'])
def crear_reservas_superadmin():
    if request.method == "GET":
        formulario = formreservanuevasuperadmin()
        return render_template('0-1-1-4-4-1-crear_reservas.html', form = formulario)
    
    else:
        formulario = formreservanuevasuperadmin(request.form)
        if formulario.validate_on_submit():
            objeto_reserva = reservas(0, formulario.bedroom.data,
            formulario.user.data, formulario.comment.data, None,
            formulario.initialdate.data, formulario.finaldate.data,
             'SI', 'NO')
            
            if objeto_reserva.insertar():
                return render_template('0-1-1-4-4-1-crear_reservas.html',
                mensaje="Su reserva se ha realizado con exito, si quiere realizar una nueva reserva actualice los campos anteriores", 
                form = formulario)
            else:
                return render_template('0-1-1-4-4-1-crear_reservas.html', 
                mensaje="Su reserva no se pudo realizar, por favor intente nuevamente.", form = formulario)
        return render_template('0-1-1-4-4-1-crear_reservas.html', mensaje="Todos los campos son obligatorios", form=formulario)

@app.route('/0-1-1-4-4-2-modificar_reservas/<id_reserva_modificar>', methods=['GET', 'POST'])
def modificar_reservas_superadmin(id_reserva_modificar):
    if request.method == "GET":
        formulario = formmodificarreservasuperadmin()
        objeto_reserva = reservas.cargar(id_reserva_modificar)
        if objeto_reserva:
            formulario.bedroom.data = objeto_reserva.id_habitacion
            formulario.initialdate.data = objeto_reserva.fecha_inicial
            formulario.finaldate.data = objeto_reserva.fecha_final
            formulario.comment.data = objeto_reserva.comentario
            return render_template('0-1-1-4-4-2-modificar_reservas.html',id_reserva=id_reserva_modificar, form = formulario)

        return render_template('0-1-1-4-4-2-modificar_reservas.html',id_reserva=id_reserva_modificar, mensaje="No se encontró una reserva para el id especificado.")

    else:
        formulario =formmodificarreservasuperadmin(request.form)

        if formulario.validate_on_submit():

            objeto_reserva = reservas.cargar(id_reserva_modificar)
            objeto_reserva.id_habitacion = formulario.newbedroom.data
            objeto_reserva.fecha_inicial = formulario.newinitialdate.data
            objeto_reserva.fecha_final = formulario.newfinaldate.data
            objeto_reserva.comentario = formulario.newcomment.data

            if objeto_reserva.actualizar():
                return render_template('0-1-1-4-4-2-modificar_reservas.html',id_reserva=id_reserva_modificar, form = formulario,
                mensaje="Su reserva ha sido actualizada.")

            else:
                return render_template('0-1-1-4-4-2-modificar_reservas.html',id_reserva=id_reserva_modificar, form=formulario, 
                mensaje="No se pudo actualizar la reserva. Por favor intentelo nuevamente.")
        
        return render_template('0-1-1-4-4-2-modificar_reservas.html', id_reserva=id_reserva_modificar, form=formulario, mensaje="Todos los datos son obligatorios.")

@app.route('/0-1-1-4-4-3-cancelar_reservas/<id_reserva_cancelar>', methods=['GET', 'POST'])
def cancelar_reservas_superadmin(id_reserva_cancelar):
    if request.method == "GET":
        formulario = formcancelarreservasuperadmin()
        objeto_reserva = reservas.cargar(id_reserva_cancelar)
        if objeto_reserva:
            formulario.bedroom.data = objeto_reserva.id_habitacion
            formulario.initialdate.data = objeto_reserva.fecha_inicial
            formulario.finaldate.data = objeto_reserva.fecha_final
            formulario.comment.data = objeto_reserva.comentario
            return render_template('0-1-1-4-4-3-cancelar_reservas.html',id_reserva=id_reserva_cancelar, form = formulario)

        return render_template('0-1-1-4-4-3-cancelar_reservas.html',id_reserva=id_reserva_cancelar, mensaje="No se encontró una reserva para el id especificado.")

    else:
        formulario =formcancelarreservasuperadmin(request.form)

        if formulario.validate_on_submit():
            objeto_reserva = reservas.cargar(id_reserva_cancelar)
            if objeto_reserva.eliminar():
                return render_template('0-1-1-4-4-3-cancelar_reservas.html',id_reserva=id_reserva_cancelar, form = formulario,
                mensaje="Su reserva ha sido cancelada.")

            else:
                return render_template('0-1-1-4-4-3-cancelar_reservas.html',id_reserva=id_reserva_cancelar, form=formulario, 
                mensaje="No se pudo cancelar la reserva. Por favor intentelo nuevamente.")
        
        return render_template('0-1-1-4-4-3-cancelar_reservas.html', id_reserva=id_reserva_cancelar, form=formulario, mensaje="Todos los campos son obligatorios.")

# Templates con ruteos actualizados al Git del Super Administrador
# 0-1-1-Opciones Usuario SuperAdministrador (ok)
# 0-1-1-5-Restringir Comentarios (ok)
# 0-1-1-1-1-Modifica datos Usuario Registrado (ok)
# 0-1-1-1-Consulta datos Usuario Registrado (ok)
# 0-1-1-2-Gestión de Usuarios Administradores (ok)
# 0-1-1-2-1-Registro Nuevo Usuario Administrador (ok)
# 0-1-1-2-2-Modifica Datos Usuario Administrador (ok)

# Fin Navegación  Gestion de Habitaciones SA *************************************  

# Inicio Navegación Restringir comentarios SA **************************************************************************

@app.route('/0-1-1-5-restringir_comentarios')
def restringir_comentarios():
    return render_template('0-1-1-5-restringir_comentarios.html')

# Fin Navegación Restringir comentarios SA *************************************


# 2021-10-10  Inicio *******************    Navegación usuario final registrado *************************************
@app.route('/0-1-3-1-consulta_datos_usuario', methods=['GET', 'POST'])
def consulta_datos_usuario_final():
    return render_template('0-1-3-1-consulta_datos_usuario.html',lista=login.datos_usuario_logueado(session['id_usuario_logueado']))

@app.route('/0-1-3-opciones_usuario_final_registrado', methods=['GET', 'POST'])
def consulta_opciones_usuario_final_registrado():
    return render_template('0-1-3-opciones_usuario_final_registrado.html')

@app.route('/0-1-3-2-consulta_habitaciones_disponibles_usuario_final', methods=['GET', 'POST'])
def consulta_habitaciones_disponibles_usuario_final():
    return render_template('0-1-3-2-consulta_habitaciones_disponibles_usuario_final.html')

@app.route('/0-1-3-4-modulo_reservas', methods=['GET', 'POST'])
def modulo_reservas():
    if request.method =="GET":
        formulario =formreservas()
        return render_template('0-1-3-4-modulo_reservas.html', form=formulario, mostrar = 0)

    else:  
        formulario = formreservas(request.form)
        if formulario.validate_on_submit():
            return render_template('0-1-3-4-modulo_reservas.html', form=formulario, 
                    lista=reservas.listado(0, formulario.bedroom.data, formulario.initialdate.data, 
                    formulario.finaldate.data), mostrar = 1)
        return render_template('0-1-3-4-modulo_reservas.html', mensaje="Todos los campos son obligatorios.", form=formulario)

@app.route('/0-1-3-4-1-crear_reservas', methods=['GET', 'POST'])
def crear_reservas():
    if request.method == "GET":
        formulario = formreservanueva()
        return render_template('0-1-3-4-1-crear_reservas.html', form = formulario)
    
    else:
        formulario = formreservanueva(request.form)
        if formulario.validate_on_submit():
            objeto_reserva = reservas(0, formulario.bedroom.data,
            formulario.user.data, formulario.comment.data, None,
            formulario.initialdate.data, formulario.finaldate.data,
             'SI', 'NO')
            
            if objeto_reserva.insertar():
                return render_template('0-1-3-4-1-crear_reservas.html',
                mensaje="Su reserva se ha realizado con exito, si quiere realizar una nueva reserva actualice los campos anteriores", 
                form = formulario)
            else:
                return render_template('0-1-3-4-1-crear_reservas.html', 
                mensaje="Su reserva no se pudo realizar, por favor intente nuevamente.", form = formulario)
        return render_template('0-1-3-4-1-crear_reservas.html', mensaje="Todos los campos son obligatorios", form=formulario)

@app.route('/0-1-3-4-2-modificar_reservas/<id_reserva_modificar>', methods=['GET', 'POST'])
def modificar_reservas(id_reserva_modificar):
    if request.method == "GET":
        formulario = formmodificarreserva()
        objeto_reserva = reservas.cargar(id_reserva_modificar)
        if objeto_reserva:
            formulario.bedroom.data = objeto_reserva.id_habitacion
            formulario.initialdate.data = objeto_reserva.fecha_inicial
            formulario.finaldate.data = objeto_reserva.fecha_final
            formulario.comment.data = objeto_reserva.comentario
            return render_template('0-1-3-4-2-modificar_reservas.html',id_reserva=id_reserva_modificar, form = formulario)

        return render_template('0-1-3-4-2-modificar_reservas.html',id_reserva=id_reserva_modificar, mensaje="No se encontró una reserva para el id especificado.")

    else:
        formulario =formmodificarreserva(request.form)

        if formulario.validate_on_submit():

            objeto_reserva = reservas.cargar(id_reserva_modificar)
            objeto_reserva.id_habitacion = formulario.newbedroom.data
            objeto_reserva.fecha_inicial = formulario.newinitialdate.data
            objeto_reserva.fecha_final = formulario.newfinaldate.data
            objeto_reserva.comentario = formulario.newcomment.data

            if objeto_reserva.actualizar():
                return render_template('0-1-3-4-2-modificar_reservas.html',id_reserva=id_reserva_modificar, form = formulario,
                mensaje="Su reserva ha sido actualizada.")

            else:
                return render_template('0-1-3-4-2-modificar_reservas.html',id_reserva=id_reserva_modificar, form=formulario, 
                mensaje="No se pudo actualizar la reserva. Por favor intentelo nuevamente.")
        
        return render_template('0-1-3-4-2-modificar_reservas.html', id_reserva=id_reserva_modificar, form=formulario, mensaje="Todos los datos son obligatorios.")

@app.route('/0-1-3-4-3-cancelar_reservas/<id_reserva_cancelar>', methods=['GET', 'POST'])
def cancelar_reservas(id_reserva_cancelar):
    if request.method == "GET":
        formulario = formcancelarreserva()
        objeto_reserva = reservas.cargar(id_reserva_cancelar)
        if objeto_reserva:
            formulario.bedroom.data = objeto_reserva.id_habitacion
            formulario.initialdate.data = objeto_reserva.fecha_inicial
            formulario.finaldate.data = objeto_reserva.fecha_final
            formulario.comment.data = objeto_reserva.comentario
            return render_template('0-1-3-4-3-cancelar_reservas.html',id_reserva=id_reserva_cancelar, form = formulario)

        return render_template('0-1-3-4-3-cancelar_reservas.html',id_reserva=id_reserva_cancelar, mensaje="No se encontró una reserva para el id especificado.")

    else:
        formulario =formcancelarreserva(request.form)

        if formulario.validate_on_submit():
            objeto_reserva = reservas.cargar(id_reserva_cancelar)
            if objeto_reserva.eliminar():
                return render_template('0-1-3-4-3-cancelar_reservas.html',id_reserva=id_reserva_cancelar, form = formulario,
                mensaje="Su reserva ha sido cancelada.")

            else:
                return render_template('0-1-3-4-3-cancelar_reservas.html',id_reserva=id_reserva_cancelar, form=formulario, 
                mensaje="No se pudo cancelar la reserva. Por favor intentelo nuevamente.")
        
        return render_template('0-1-3-4-3-cancelar_reservas.html', id_reserva=id_reserva_cancelar, form=formulario, mensaje="Todos los campos son obligatorios.")


#@app.route('/0-1-3-1-1-modificar_datos_usuario', methods=['GET', 'POST'])
#def modificar_datos_usuario():
#    return render_template('0-1-3-1-1-modificar_datos_usuario.html')

@app.route('/0-1-3-1-1-modificar_datos_usuario', methods=['GET', 'POST'])
def modificar_datos_usuario():
    if request.method =="GET":
        objeto_usuario =usuario_final.cargar(session['id_usuario_logueado'])
        formulario = FormModificarUsuarioRegistrado()
        formulario.nombre.data = objeto_usuario.nombres
        formulario.documento.data = objeto_usuario.documento
        formulario.usuario.data = objeto_usuario.usuario
        formulario.contrasena1.data = objeto_usuario.contrasena
        formulario.contrasena2.data = objeto_usuario.contrasena
        return render_template('0-1-3-1-1-modificar_datos_usuario.html', form=formulario)
    else:
        formulario =FormModificarUsuarioRegistrado(request.form)
        objeto_usuario = usuario_final(session['id_usuario_logueado'], formulario.documento.data, formulario.nombre.data, formulario.contrasena1.data, 
                                'UF', 'SI', formulario.usuario.data)
        objeto_usuario.modificar()
        return render_template('0-1-3-1-consulta_datos_usuario.html',lista=login.datos_usuario_logueado(session['id_usuario_logueado']))

@app.route('/0-1-3-2-1-consulta_comentarios_habitacion_usuario', methods=['GET', 'POST'])
def consulta_comentarios_habitacion_usuario():
    return render_template('0-1-3-2-1-consulta_comentarios_habitacion_usuario.html')

@app.route('/0-1-3-3-gestion_habitaciones_reservadas_usuario_final', methods=['GET', 'POST'])
def gestion_habitaciones_reservadas_usuario_final():
    return render_template('0-1-3-3-gestion_habitaciones_reservadas_usuario_final.html')


@app.route('/0-1-3-3-1-modificar_comentarios_habitacion', methods=['GET', 'POST'])
def modificar_comentarios_habitacion():
    if request.method=="GET":
        return render_template('0-1-3-3-1-modificar_comentarios_habitacion.html')
    else:
        descripcion=request.form['descripcion']
        return render_template('0-1-3-3-gestion_habitaciones_reservadas_usuario_final.html',sentencia='UPDATE tbl_comentarios SET comentario="'+descripcion+ '" WHERE codigo_habitacion=101 AND codigo_reserva=101')

@app.route('/0-1-3-3-2-calificar_habitaciones/<int:codigo_habitacion>/<codigo_reserva>', methods=['GET', 'POST'])

def calificar_habitaciones(codigo_habitacion,codigo_reserva):
    if request.method =="GET":
        formulario =FormCalificarHabitacion()
        return render_template('0-1-3-3-2-calificar_habitaciones.html', form=formulario,numero_habitacion=codigo_habitacion,numero_reserva=codigo_reserva)
    else:
        formulario = FormCalificarHabitacion(request.form)
        valor_calificacion=str(formulario.data['calificacion'])
        return render_template('0-1-3-3-gestion_habitaciones_reservadas_usuario_final.html',sentencia='UPDATE tbl_calificaciones SET calificacion='+valor_calificacion+' WHERE codigo_habitacion='+ str(codigo_habitacion) +' AND codigo_reserva='+str(codigo_reserva))

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
#  0-1-3-4-2-modificar_reservas.html (ok)

# formularios en los que se ha implemantado logica
# modificar comentario habitacion - reserva por parte de un usuario final registrado
    # 0-1-3-3-1-modificar_comentarios_habitacion  # 0-1-3-3-gestion_habitaciones_reservadas_usuario_final
# calificar habitacion - reserva por parte de un usuario final registrado
    # 0-1-3-3-2-calificar_habitaciones  # 0-1-3-3-gestion_habitaciones_reservadas_usuario_final


# 2021-10-10  IFin ************************    Navegación  usuario final registrado *************************************

# Inicio Navegación usuario invitado  *****************************************
# 0-2-opciones_invitado (ok)
# 0-2-1-registro_nuevo_usuario (ok)
# 0-2-2-consulta_habitaciones_disponibles (ok)
# 0-2-2-1-consulta_comentarios_habitacion (ok)

@app.route('/0-2-1-registro_nuevo_usuario', methods=['GET', 'POST'])
def registro_nuevo_usuario_final():
    if request.method =="GET":
        formulario =FormCrearUsuarioRegistrado()
        return render_template('0-2-1-registro_nuevo_usuario.html', form=formulario)
    else:
        formulario =FormCrearUsuarioRegistrado(request.form)
        objeto_usuario = usuario_final(0, formulario.documento.data, formulario.nombre.data, formulario.contrasena1.data, 
                                    'UF', 'SI', formulario.usuario.data)
        # por defecto al agregar un usuario el user y password se cargan por defecto con el documento de identidad
        if objeto_usuario.insertar():   
            formulario =formlogin()
            formulario.user.data = None
            formulario.password.data = None
            return render_template('0-1-login.html', mensaje="Usuario o contraseña de usuario final no son válidos.", form=formulario)
        else:
            return render_template('0-inicio.html')

@app.route('/0-2-2-consulta_habitaciones_disponibles', methods=['GET'])
def consulta_habitacion_disponibles():
    return render_template('0-2-2-consulta_habitaciones_disponibles.html')

@app.route('/0-2-2-1-consulta_comentarios_habitacion', methods=['GET'])
def consulta_comentario_habitacion():
    return render_template('0-2-2-1-consulta_comentarios_habitacion.html')

# Fin Navegación usuario invitado  *****************************************



# ********************************************************
# ******** Inicio Navegación usuario Administrador *******
# ********************************************************

# opciones_administrador se encuentra creada en la parte superior

# Primera rama de navegación de usuario administrador
@app.route('/0-1-2-1-consulta_datos_usuario', methods=['GET', 'POST'])
def consulta_datos_usuario_admin():
    return render_template('0-1-2-1-consulta_datos_usuario.html',lista=login.datos_usuario_logueado(session['id_usuario_logueado']))

#@app.route('/0-1-2-1-1-modificar_datos_usuario', methods=['GET', 'POST'])
#def modificar_datos_usuario_admin():
#    return render_template('0-1-2-1-1-modificar_datos_usuario.html')

@app.route('/0-1-2-1-1-modificar_datos_usuario', methods=['GET', 'POST'])
def modificar_datos_usuario_admin():
    if request.method =="GET":
        objeto_usuario =usuario_final.cargar(session['id_usuario_logueado'])
        formulario = FormModificarUsuarioRegistrado()
        formulario.nombre.data = objeto_usuario.nombres
        formulario.documento.data = objeto_usuario.documento
        formulario.usuario.data = objeto_usuario.usuario
        formulario.contrasena1.data = objeto_usuario.contrasena
        formulario.contrasena2.data = objeto_usuario.contrasena
        return render_template('0-1-2-1-1-modificar_datos_usuario.html', form=formulario)
    else:
        formulario =FormModificarUsuarioRegistrado(request.form)
        objeto_usuario = usuario_administrador(session['id_usuario_logueado'], formulario.documento.data, formulario.nombre.data, formulario.contrasena1.data, 
                                'A', 'SI', formulario.usuario.data)
                                
        objeto_usuario.modificar()
        return render_template('0-1-2-1-consulta_datos_usuario.html',lista=login.datos_usuario_logueado(session['id_usuario_logueado']))

# Segunda rama de navegación de usuario administrador
@app.route('/0-1-2-2-gestion_usuarios_finales', methods=["GET"])
def gestion_usuarios_finales_admin():
    return render_template('0-1-2-2-gestion_usuarios_finales.html', lista=usuario_final.listado())

@app.route('/0-1-2-2-1-agregar_usuario_final_crud', methods=['GET', 'POST'])
def agregar_usuario_final_crud_admin():
    if request.method =="GET":
        formulario =FormAgregarUsuarioFinalCRUD()
        return render_template('0-1-2-2-1-agregar_usuario_final_crud.html', form=formulario)
    else:
        formulario =FormAgregarUsuarioFinalCRUD(request.form)
        objeto_usuario = usuario_final(0, formulario.documento.data, formulario.nombre.data, formulario.documento.data, 
                                'UF', 'SI', formulario.documento.data)
        # por defecto al agregar un usuario el user y password se cargan por defecto con el documento de identidad
        if objeto_usuario.insertar():   
            return render_template('0-1-2-2-gestion_usuarios_finales.html', lista=usuario_final.listado())
        else:
            return render_template('0-1-2-2-gestion_usuarios_finales.html', lista=usuario_final.listado())    

@app.route('/0-1-2-2-2-modificar_eliminar_usuario_final_crud/<id_usuario>/<accion>', methods=["GET", 'POST'])
def modificar_eliminar_usuario_final_crud_admin(id_usuario,accion):
    objeto_usuario =usuario_final.cargar(id_usuario)
    if accion=='modificar':
        formulario = FormModificarUsuarioFinalCRUD()
        formulario.id_usuario.data = objeto_usuario.id_usuario
        formulario.nombre.data = objeto_usuario.nombres
        formulario.documento.data = objeto_usuario.documento
        formulario.activo.data = objeto_usuario.activo
        return render_template('0-1-2-2-2-modificar_usuario_final_crud.html',form = formulario)
    else:
        objeto_usuario.eliminar()
        return render_template('0-1-2-2-gestion_usuarios_finales.html', lista=usuario_final.listado())

@app.route('/0-1-2-2-2-modificar_usuario_final_crud', methods=["GET", 'POST'])
def modificar_usuario_final_crud_admin():
    formulario =FormModificarUsuarioFinalCRUD(request.form)
    objeto_usuario = usuario_final(formulario.id_usuario.data, formulario.documento.data, formulario.nombre.data, formulario.documento.data, 
                                'UF', formulario.activo.data, formulario.documento.data)
    objeto_usuario.modificar()
    return render_template('0-1-2-2-gestion_usuarios_finales.html', lista=usuario_final.listado())

# Tercera rama de navegación usuario administrador
@app.route('/0-1-2-3-gestion_habitaciones', methods=['GET', 'POST'])
def gestion_habitaciones_admin():
    return render_template('0-1-2-3-gestion_habitaciones.html')

@app.route('/0-1-2-3-1-nueva_habitacion', methods=['GET', 'POST'])
def nueva_habitacion_admin():
    return render_template('0-1-2-3-1-nueva_habitacion.html')

@app.route('/0-1-2-3-2-modificar_habitacion', methods=['GET', 'POST'])
def modificar_habitacion_admin():
    return render_template('0-1-2-3-2-modificar_habitacion.html')

@app.route('/0-1-2-3-3-consulta_comentarios_habitacion_usuario', methods=['GET', 'POST'])
def consulta_comentarios_habitacion_usuario_admin():
    return render_template('0-1-2-3-3-consulta_comentarios_habitacion_usuario.html')

@app.route('/0-1-2-3-4-consulta_reservas', methods=['GET', 'POST'])
def consulta_reservas_admin():
    if request.method =="GET":
        formulario =formreservasadmin()
        lista = reservas.listado_choices_habitaciones()
        #for i in lista:
            #lista_choices = lista[0][i]
        # Aquí es necesario crear el vector de choices
        #FORMULARIO.BEDROOM.CHOICES 
        return render_template('0-1-2-3-4-consulta_reservas.html', form=formulario, mostrar = 0)

    else:  
        formulario = formreservasadmin(request.form)
        if formulario.validate_on_submit():
            return render_template('0-1-2-3-4-consulta_reservas.html', form=formulario, 
                    lista=reservas.listado(0, formulario.bedroom.data, formulario.initialdate.data, 
                    formulario.finaldate.data), mostrar = 1)
        return render_template('0-1-2-3-4-consulta_reservas.html', mensaje="Todos los campos son obligatorios.", form=formulario)

@app.route('/0-1-2-3-4-1-crear_reservas', methods=['GET', 'POST'])
def crear_reservas_admin():
    if request.method == "GET":
        formulario = formreservanuevaadmin()
        return render_template('0-1-2-3-4-1-crear_reservas.html', form = formulario)
    
    else:
        formulario = formreservanuevaadmin(request.form)
        if formulario.validate_on_submit():
            objeto_reserva = reservas(0, formulario.bedroom.data,
            formulario.user.data, formulario.comment.data, None,
            formulario.initialdate.data, formulario.finaldate.data,
             'SI', 'NO')
            
            if objeto_reserva.insertar():
                return render_template('0-1-2-3-4-1-crear_reservas.html',
                mensaje="Su reserva se ha realizado con exito, si quiere realizar una nueva reserva actualice los campos anteriores", 
                form = formulario)
            else:
                return render_template('0-1-2-3-4-1-crear_reservas.html', 
                mensaje="Su reserva no se pudo realizar, por favor intente nuevamente.", form = formulario)
        return render_template('0-1-2-3-4-1-crear_reservas.html', mensaje="Todos los campos son obligatorios", form=formulario)

@app.route('/0-1-2-3-4-2-modificar_reservas/<id_reserva_modificar>', methods=['GET', 'POST'])
def modificar_reservas_admin(id_reserva_modificar):
    if request.method == "GET":
        formulario = formmodificarreservaadmin()
        objeto_reserva = reservas.cargar(id_reserva_modificar)
        if objeto_reserva:
            formulario.bedroom.data = objeto_reserva.id_habitacion
            formulario.initialdate.data = objeto_reserva.fecha_inicial
            formulario.finaldate.data = objeto_reserva.fecha_final
            formulario.comment.data = objeto_reserva.comentario
            return render_template('0-1-2-3-4-2-modificar_reservas.html',id_reserva=id_reserva_modificar, form = formulario)

        return render_template('0-1-2-3-4-2-modificar_reservas.html',id_reserva=id_reserva_modificar, mensaje="No se encontró una reserva para el id especificado.")

    else:
        formulario =formmodificarreservaadmin(request.form)

        if formulario.validate_on_submit():

            objeto_reserva = reservas.cargar(id_reserva_modificar)
            objeto_reserva.id_habitacion = formulario.newbedroom.data
            objeto_reserva.fecha_inicial = formulario.newinitialdate.data
            objeto_reserva.fecha_final = formulario.newfinaldate.data
            objeto_reserva.comentario = formulario.newcomment.data

            if objeto_reserva.actualizar():
                return render_template('0-1-2-3-4-2-modificar_reservas.html',id_reserva=id_reserva_modificar, form = formulario,
                mensaje="Su reserva ha sido actualizada.")

            else:
                return render_template('0-1-2-3-4-2-modificar_reservas.html',id_reserva=id_reserva_modificar, form=formulario, 
                mensaje="No se pudo actualizar la reserva. Por favor intentelo nuevamente.")
        
        return render_template('0-1-2-3-4-2-modificar_reservas.html', id_reserva=id_reserva_modificar, form=formulario, mensaje="Todos los datos son obligatorios.")

@app.route('/0-1-2-3-4-3-cancelar_reservas/<id_reserva_cancelar>', methods=['GET', 'POST'])
def cancelar_reservas_admin(id_reserva_cancelar):
    if request.method == "GET":
        formulario = formcancelarreservaadmin()
        objeto_reserva = reservas.cargar(id_reserva_cancelar)
        if objeto_reserva:
            formulario.bedroom.data = objeto_reserva.id_habitacion
            formulario.initialdate.data = objeto_reserva.fecha_inicial
            formulario.finaldate.data = objeto_reserva.fecha_final
            formulario.comment.data = objeto_reserva.comentario
            return render_template('0-1-2-3-4-3-cancelar_reservas.html',id_reserva=id_reserva_cancelar, form = formulario)

        return render_template('0-1-2-3-4-3-cancelar_reservas.html',id_reserva=id_reserva_cancelar, mensaje="No se encontró una reserva para el id especificado.")

    else:
        formulario =formcancelarreservaadmin(request.form)

        if formulario.validate_on_submit():
            objeto_reserva = reservas.cargar(id_reserva_cancelar)
            if objeto_reserva.eliminar():
                return render_template('0-1-2-3-4-3-cancelar_reservas.html',id_reserva=id_reserva_cancelar, form = formulario,
                mensaje="Su reserva ha sido cancelada.")

            else:
                return render_template('0-1-2-3-4-3-cancelar_reservas.html',id_reserva=id_reserva_cancelar, form=formulario, 
                mensaje="No se pudo cancelar la reserva. Por favor intentelo nuevamente.")
        
        return render_template('0-1-2-3-4-3-cancelar_reservas.html', id_reserva=id_reserva_cancelar, form=formulario, mensaje="Todos los campos son obligatorios.")

# ********************************************************
# ********** Fin Navegación usuario Adminsitrador ********
# ********************************************************

