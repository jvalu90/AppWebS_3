from flask_wtf import FlaskForm
from wtforms import validators
from wtforms.fields.core import StringField
from wtforms.fields.simple import PasswordField, SubmitField, TextAreaField

#Iniciando la construcción del forms

class formlogin(FlaskForm):
    user = StringField('Usuario', validators=[validators.required(), validators.length(max=100)]) #Cómo se centra aquí?
    password = PasswordField('Contraseña', validators=[validators.required(), validators.length(max=100)])
    usuariofinal = SubmitField('Ingresar como Usuario Final') #<!--{{ form.usuariofinal(class="btn btn-outline-dark") }}-->
    administrador = SubmitField('Ingresar como Administrador')

    # Choices, Choice, argumentos de RadioField
    #superadministrador = SubmitField('Ingresar como Super Administrador')
    
# 2021-10-09 Inicio Formulario Modificar Comentario 0-1-3-3-1-modificar_comentarios_habitacion

# 2021-10-09 Fin Formulario Modificar Comentario
