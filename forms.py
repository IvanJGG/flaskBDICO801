from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, EmailField
from wtforms.validators import DataRequired, Length, Email

class UserForm(FlaskForm):
    id = IntegerField('ID')
    nom = StringField('Nombre', validators=[DataRequired(), Length(min=2, max=50)])
    apa = StringField('Apellido Paterno', validators=[DataRequired(), Length(min=2, max=50)])
    ama = StringField('Apellido Materno', validators=[DataRequired(), Length(min=2, max=50)])
    edad = IntegerField('Edad', validators=[DataRequired()])
    email = EmailField('Correo Electrónico', validators=[DataRequired(), Email()])

class MaestroForm(FlaskForm):
    id = IntegerField('ID')
    nom = StringField('Nombre', validators=[DataRequired(), Length(min=2, max=50)])
    apa = StringField('Apellido Paterno', validators=[DataRequired(), Length(min=2, max=50)])
    ama = StringField('Apellido Materno', validators=[DataRequired(), Length(min=2, max=50)])
    matricula = StringField('Matrícula', validators=[DataRequired(), Length(min=1, max=50)])
    email = EmailField('Correo Electrónico', validators=[DataRequired(), Email()])

class CursoForm(FlaskForm):
    id = IntegerField('ID')
    nom = StringField('Nombre del Curso', validators=[DataRequired()])
    descripcion = StringField('Descripción', validators=[DataRequired()])
    maestro_id = IntegerField('ID del Maestro', validators=[DataRequired()])

class InscripcionForm(FlaskForm):
    id = IntegerField('ID')
    alumno_id = IntegerField('ID del Alumno', validators=[DataRequired()])
    curso_id = IntegerField('ID del Curso', validators=[DataRequired()])