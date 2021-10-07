from flask_wtf import FlaskForm
from wtforms import validators
from wtforms.fields.core import StringField
from wtforms.fields.simple import PasswordField, SubmitField, TextAreaField

#Iniciando la construcción del forms

class formlogin(FlaskForm):
    user = StringField('Usuario', validators=[validators.required(), validators.length(max=100)]) #Cómo se centra aquí?
    password = PasswordField('Contraseña', validators=[validators.required(), validators.length(max=100)])
    #usuariofinal = SubmitField('Ingresar como Usuario Final') <!--{{ form.usuariofinal(class="button") }}-->
    #administrador = SubmitField('Ingresar como Administrador')
    #superadministrador = SubmitField('Ingresar como Super Administrador')