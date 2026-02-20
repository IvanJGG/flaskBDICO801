from wtforms import Form
from wtforms import StringField, IntegerField, EmailField
from wtforms.validators import DataRequired, Length, Email

class UserForm(Form):
    mat = IntegerField('Matrícula')
    nom = StringField('Nombre', validators=[DataRequired(), Length(min=2, max=50)])
    apa = StringField('Apellido Paterno', validators=[DataRequired(), Length(min=2, max=50)])
    ama = StringField('Apellido Materno', validators=[DataRequired(), Length(min=2, max=50)])
    edad = IntegerField('Edad')
    email = EmailField('Correo Electrónico', validators=[DataRequired(), Email()])