from flask_wtf import FlaskForm
from wtforms import validators
from wtforms.fields.core import StringField, RadioField
from wtforms.fields.simple import PasswordField, SubmitField
from wtforms.fields.html5 import DecimalRangeField

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

# HTML donde deben completarse los formularios para implementar el CRUD Reservas:
# 0-1-login

# USUARIO FINAL
# 0-1-3-4-modulo_reservas
# 0-1-3-4-1-crear_reservas

# ADMINISTRADOR
# 0-1-2-3-gestion_habitaciones
# 0-1-2-3-4-consulta_reservas

# SUPER ADMINISTRADOR
# 0-1-1-4-gestion_habitaciones
# 0-1-1-4-4-consulta_reservas

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


# FIN CLASES Y FUNCIONES RELACIONADAS CON EL CRUD USUARIOS #####################################