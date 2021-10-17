from flask_wtf import FlaskForm
from wtforms import validators
from wtforms.fields.core import DateField, SelectField, StringField, RadioField
from wtforms.fields.simple import PasswordField, SubmitField,HiddenField, TextAreaField
from wtforms.fields.html5 import DecimalRangeField
from models import reservas,usuario_final,usuario_administrador

#Inicio formulario validación en Login#######################################################

class formlogin(FlaskForm):
    user = StringField('Usuario', validators=[validators.required(), validators.length(max=100)]) #Cómo se centra aquí?
    password = PasswordField('Contraseña', validators=[validators.required(), validators.length(max=100)])
    tipoUsuario = RadioField('Tipo de usuario', choices=[('UF','Usuario Final'),('A','Administrador'),('SA','Super Administrador')])
    enviar = SubmitField('Ingresar')

#Fin formulario validación en Login##########################################################

#Inicio formulario validación en 0-1-3-3-2 calificar habitaciones #######################################################
class FormCalificarHabitacion(FlaskForm):
    calificacion = DecimalRangeField('calificacion')
    enviar = SubmitField('Calificar') 
#fin formulario validación en 0-1-3-3-2 calificar habitaciones #######################################################

   
# Aquí se desarrollan todas las funciones que tienen que ver con la conexión de la base de datos
# Es necesario sectorizar por tipo CRUD, las funciones anteriores, sirven para orientas pero en 
# En varios de los html faltan los formularios, se sugiere revisar según los crud en todas las
# visualizaciones

# INICIO CLASES Y FUNCIONES RELACIONADAS CON EL CRUD RESERVAS ##################################

#Usuario Final
# 0-1-3-4-modulo_reservas
class formreservas(FlaskForm):
    lista_habitaciones = reservas.listado_choices_habitaciones()
    initialdate = DateField('Fecha Inicial', validators=[validators.required()])
    finaldate = DateField('Fecha Final', validators=[validators.required()])
    bedroom = SelectField('ID Habitación', validators=[validators.required()], choices=['', 1, 2, 3]) 
    #Cambiar el select a Dinámico, podría ser un objeto de tipo habitación 
    # aplicando un método tipo listado
    consult = SubmitField('Consultar')

# 0-1-3-4-1-crear_reservas
class formreservanueva(FlaskForm):
    lista_habitaciones = reservas.listado_choices_habitaciones()
    lista_usuarios = reservas.listado_choices_usuarios()
    bedroom = SelectField('ID Habitación', validators=[validators.required()], choices=['', 1, 2, 3])
    user = SelectField('ID Usuario', validators=[validators.required()], choices=['', 4, 5, 6])
    initialdate = DateField('Fecha Inicial', validators=[validators.required()])
    finaldate = DateField('Fecha Final', validators=[validators.required()])
    comment = TextAreaField('Comentario Hospedaje', validators=[validators.required(), validators.length(max=200)]) 
    #Cambiar el select a Dinámico, podría ser un objeto de tipo habitación 
    # aplicando un método tipo listado
    newreservation = SubmitField('Reservar')  

# 0-1-3-4-2-modificar_reservas

class formmodificarreserva(FlaskForm):
    lista_habitaciones = reservas.listado_choices_habitaciones()
    bedroom = StringField('ID Habitación', validators=[validators.required()])
    initialdate = StringField('Fecha Inicial', validators=[validators.required()])
    finaldate = StringField('Fecha Final', validators=[validators.required()])
    comment = TextAreaField('Comentario Hospedaje Previo', validators=[validators.required(), validators.length(max=200)]) 
    newbedroom = SelectField('Nuevo ID Habitación', validators=[validators.required()], choices=['', 1, 2, 3])
    newinitialdate = DateField('Nueva Fecha Inicial', validators=[validators.required()])
    newfinaldate = DateField('Nueva Fecha Final', validators=[validators.required()])
    newcomment = TextAreaField('Nuevo Comentario Hospedaje', validators=[validators.required(), validators.length(max=200)]) 
    #Cambiar el select a Dinámico, podría ser un objeto de tipo habitación 
    # aplicando un método tipo listado
    modifyreservation = SubmitField('Modificar Reserva') 

# 0-1-3-4-3-cancelar_reservas
class formcancelarreserva(FlaskForm):
    bedroom = StringField('ID Habitación', validators=[validators.required()])
    initialdate = StringField('Fecha Inicial', validators=[validators.required()])
    finaldate = StringField('Fecha Final', validators=[validators.required()])
    comment = TextAreaField('Comentario Hospedaje Previo', validators=[validators.required(), validators.length(max=200)]) 
    cancelreservation = SubmitField('Cancelar Reserva') 

# Usuario Administrador
# 0-1-2-3-4-consulta_reservas
class formreservasadmin(FlaskForm):
    lista_habitaciones = reservas.listado_choices_habitaciones()
    initialdate = DateField('Fecha Inicial', validators=[validators.required()])
    finaldate = DateField('Fecha Final', validators=[validators.required()])
    lista = reservas.listado_choices_habitaciones()
    bedroom = SelectField('ID Habitación', validators=[validators.required()], choices=['', 1, 2, 3]) 
    #Cambiar el select a Dinámico, podría ser un objeto de tipo habitación 
    # aplicando un método tipo listado
    consult = SubmitField('Consultar')

# 0-1-2-3-4-1-crear_reservas
class formreservanuevaadmin(FlaskForm):
    lista_habitaciones = reservas.listado_choices_habitaciones()
    lista_usuarios = reservas.listado_choices_usuarios()
    bedroom = SelectField('ID Habitación', validators=[validators.required()], choices=['', 1, 2, 3])
    user = SelectField('ID Usuario', validators=[validators.required()], choices=['', 4, 5, 6])
    initialdate = DateField('Fecha Inicial', validators=[validators.required()])
    finaldate = DateField('Fecha Final', validators=[validators.required()])
    comment = TextAreaField('Comentario Hospedaje', validators=[validators.required(), validators.length(max=200)]) 
    #Cambiar el select a Dinámico, podría ser un objeto de tipo habitación 
    # aplicando un método tipo listado
    newreservation = SubmitField('Reservar')

# 0-1-2-3-4-2-modificar_reservas 
class formmodificarreservaadmin(FlaskForm):
    lista_habitaciones = reservas.listado_choices_habitaciones()
    bedroom = StringField('ID Habitación', validators=[validators.required()])
    initialdate = StringField('Fecha Inicial', validators=[validators.required()])
    finaldate = StringField('Fecha Final', validators=[validators.required()])
    comment = TextAreaField('Comentario Hospedaje Previo', validators=[validators.required(), validators.length(max=200)]) 
    newbedroom = SelectField('Nuevo ID Habitación', validators=[validators.required()], choices=['', 1, 2, 3])
    newinitialdate = DateField('Nueva Fecha Inicial', validators=[validators.required()])
    newfinaldate = DateField('Nueva Fecha Final', validators=[validators.required()])
    newcomment = TextAreaField('Nuevo Comentario Hospedaje', validators=[validators.required(), validators.length(max=200)]) 
    #Cambiar el select a Dinámico, podría ser un objeto de tipo habitación 
    # aplicando un método tipo listado
    modifyreservation = SubmitField('Modificar Reserva') 

# 0-1-2-3-4-3-cancelar_reservas
class formcancelarreservaadmin(FlaskForm):
    bedroom = StringField('ID Habitación', validators=[validators.required()])
    initialdate = StringField('Fecha Inicial', validators=[validators.required()])
    finaldate = StringField('Fecha Final', validators=[validators.required()])
    comment = TextAreaField('Comentario Hospedaje Previo', validators=[validators.required(), validators.length(max=200)]) 
    cancelreservation = SubmitField('Cancelar Reserva')

# Usuario SuperAdministrador
# 0-1-1-4-4-consulta_reservas
class formreservassuperadmin(FlaskForm):
    lista_habitaciones = reservas.listado_choices_habitaciones()
    initialdate = DateField('Fecha Inicial', validators=[validators.required()])
    finaldate = DateField('Fecha Final', validators=[validators.required()])
    lista = reservas.listado_choices_habitaciones()
    bedroom = SelectField('ID Habitación', validators=[validators.required()], choices=['', 1, 2, 3]) 
    #Cambiar el select a Dinámico, podría ser un objeto de tipo habitación 
    # aplicando un método tipo listado
    consult = SubmitField('Consultar')

# 0-1-1-4-4-1-crear_reservas
class formreservanuevasuperadmin(FlaskForm):
    lista_habitaciones = reservas.listado_choices_habitaciones()
    lista_usuarios = reservas.listado_choices_usuarios()
    bedroom = SelectField('ID Habitación', validators=[validators.required()], choices=['', 1, 2, 3])
    user = SelectField('ID Usuario', validators=[validators.required()], choices=['', 4, 5, 6])
    initialdate = DateField('Fecha Inicial', validators=[validators.required()])
    finaldate = DateField('Fecha Final', validators=[validators.required()])
    comment = TextAreaField('Comentario Hospedaje', validators=[validators.required(), validators.length(max=200)]) 
    #Cambiar el select a Dinámico, podría ser un objeto de tipo habitación 
    # aplicando un método tipo listado
    newreservation = SubmitField('Reservar')

# 0-1-1-4-4-2-modificar_reservas
class formmodificarreservasuperadmin(FlaskForm):
    lista_habitaciones = reservas.listado_choices_habitaciones()
    bedroom = StringField('ID Habitación', validators=[validators.required()])
    initialdate = StringField('Fecha Inicial', validators=[validators.required()])
    finaldate = StringField('Fecha Final', validators=[validators.required()])
    comment = TextAreaField('Comentario Hospedaje Previo', validators=[validators.required(), validators.length(max=200)]) 
    newbedroom = SelectField('Nuevo ID Habitación', validators=[validators.required()], choices=['', 1, 2, 3])
    newinitialdate = DateField('Nueva Fecha Inicial', validators=[validators.required()])
    newfinaldate = DateField('Nueva Fecha Final', validators=[validators.required()])
    newcomment = TextAreaField('Nuevo Comentario Hospedaje', validators=[validators.required(), validators.length(max=200)]) 
    #Cambiar el select a Dinámico, podría ser un objeto de tipo habitación 
    # aplicando un método tipo listado
    modifyreservation = SubmitField('Modificar Reserva') 

# 0-1-1-4-4-3-cancelar_reservas
class formcancelarreservasuperadmin(FlaskForm):
    bedroom = StringField('ID Habitación', validators=[validators.required()])
    initialdate = StringField('Fecha Inicial', validators=[validators.required()])
    finaldate = StringField('Fecha Final', validators=[validators.required()])
    comment = TextAreaField('Comentario Hospedaje Previo', validators=[validators.required(), validators.length(max=200)]) 
    cancelreservation = SubmitField('Cancelar Reserva')

# HTML donde deben completarse los formularios para implementar el CRUD Reservas:

# USUARIO FINAL
# 0-1-3-4-modulo_reservas OK
# 0-1-3-4-1-crear_reservas OK
# 0-1-3-4-2-modificar_reservas OK
# 0-1-3-4-3-cancelar_reservas OK

# ADMINISTRADOR
# 0-1-2-3-4-consulta_reservas OK
# 0-1-2-3-4-1-crear_reservas OK
# 0-1-2-3-4-2-modificar_reservas OK
# 0-1-2-3-4-3-cancelar_reservas OK

# SUPER ADMINISTRADOR
# 0-1-1-4-4-consulta_reservas
# 0-1-1-4-4-1-crear_reservas
# 0-1-1-4-4-2-modificar_reservas
# 0-1-1-4-4-3-cancelar_reservas

# USUARIO INVITADO
# No tiene CRUD Reservas


# FIN CLASES Y FUNCIONES RELACIONADAS CON EL CRUD RESERVAS #####################################

# INICIO CLASES Y FUNCIONES RELACIONADAS CON EL CRUD HABITACIONES ##############################


# FIN CLASES Y FUNCIONES RELACIONADAS CON EL CRUD HABITACIONES #################################

# INICIO CLASES Y FUNCIONES RELACIONADAS CON EL CRUD COMENTARIOS ###############################


# FIN CLASES Y FUNCIONES RELACIONADAS CON EL CRUD COMENTARIOS ##################################

# INICIO CLASES Y FUNCIONES RELACIONADAS CON EL CRUD CALIFICACION ##############################


# FIN CLASES Y FUNCIONES RELACIONADAS CON EL CRUD CALIFICACION #################################

# INICIO CLASES Y FUNCIONES RELACIONADAS CON EL CRUD USUARIOS ##################################
# Formularios Gestion usuarios 
class FormAgregarUsuarioFinalCRUD(FlaskForm):
    nombre = StringField('Nombres Completos') 
    usuario = StringField('Usuario') 
    documento = StringField('Documento') 
    enviar = SubmitField('Agregar') 

class FormModificarUsuarioFinalCRUD(FlaskForm):
    id_usuario = HiddenField('id_usuario') 
    nombre = StringField('Nombres Completos') 
    documento = StringField('Documento') 
    activo= RadioField('Activo', choices=[('SI','SI'),('NO','NO')])
    enviar = SubmitField('Modificar') 

class FormAgregarUsuarioAdmonCRUD(FlaskForm):
    nombre = StringField('Nombres Completos') 
    usuario = StringField('Usuario') 
    documento = StringField('Documento') 
    enviar = SubmitField('Agregar') 

class FormModificarUsuarioAdmonCRUD(FlaskForm):
    id_usuario = HiddenField('id_usuario') 
    nombre = StringField('Nombres Completos') 
    documento = StringField('Documento') 
    activo= RadioField('Activo', choices=[('SI','SI'),('NO','NO')])
    enviar = SubmitField('Modificar') 

# FIN CLASES Y FUNCIONES RELACIONADAS CON EL CRUD USUARIOS #####################################
