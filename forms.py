from flask_wtf import FlaskForm
from wtforms import validators
from wtforms.fields.core import StringField, RadioField
from wtforms.fields.simple import PasswordField, SubmitField

#Inicio formulario validación en Login#######################################################

class formlogin(FlaskForm):
    user = StringField('Usuario', validators=[validators.required(), validators.length(max=100)]) #Cómo se centra aquí?
    password = PasswordField('Contraseña', validators=[validators.required(), validators.length(max=100)])
    tipoUsuario = RadioField('Tipo de usuario', choices=[('UF','Usuario Final'),('A','Administrador'),('SA','Super Administrador')])
    enviar = SubmitField('Ingresar')

#Fin formulario validación en Login##########################################################
    
# 2021-10-09 Inicio Formulario Modificar Comentario 0-1-3-3-1-modificar_comentarios_habitacion
# Descripción de la lógica: 
# Se verifica el contenido del comentario, si se encuetra vacio se emite un mensaje que diga "Comentario vacío" 

# 2021-10-09 Fin Formulario Modificar Comentario
