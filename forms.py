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


   
