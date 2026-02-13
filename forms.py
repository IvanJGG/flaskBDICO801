from wtforms import Form
from wtforms import StringField, PasswordField, IntegerField, EmailField
from wtforms.validators import DataRequired, Length, Email

class UserForm(Form):
    nombre = StringField('Nombre', validators=[DataRequired(), Length(min=2, max=50)])
    apaterno = StringField('Apellido Paterno', validators=[DataRequired(), Length(min=2, max=50)])
    amaterno = StringField('Apellido Materno', validators=[DataRequired(), Length(min=2, max=50)])
    edad = IntegerField('Edad', validators=[DataRequired()])
    correo = EmailField('Correo Electrónico', validators=[DataRequired(), Email()])