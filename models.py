from flask_sqlalchemy import SQLAlchemy #ORM
import datetime

db = SQLAlchemy()

class Alumnos(db.Model):
    __tablename__ = 'alumnos'
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(250), nullable=False)
    apa = db.Column(db.String(250), nullable=False)
    ama = db.Column(db.String(250), nullable=False)
    edad = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    created_date = db.Column(db.DateTime, default=datetime.datetime.now)
    cursos = db.relationship(
        'Curso', 
        secondary='inscripciones', 
        back_populates='alumnos')

class Maestros(db.Model):
    __tablename__ = 'maestros'
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(250), nullable=False)
    apa = db.Column(db.String(250), nullable=False)
    ama = db.Column(db.String(250), nullable=False)
    edad = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

    cursos = db.relationship(
        'Curso', 
        secondary='inscripciones', 
        back_populates='maestros')
    
class Curso(db.Model):
    __tablename__ = 'cursos'
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(250), nullable=False)
    descripcion = db.Column(db.String(500), nullable=False)

    maestro_id = db.Column(db.Integer, db.ForeignKey('maestros.id'),  nullable=False)

    maestros = db.relationship(
        'Maestros', 
        secondary='inscripciones', 
        back_populates='cursos')
    
    alumnos = db.relationship(
        'Alumnos', 
        secondary='inscripciones', 
        back_populates='cursos')

class Inscripcion(db.Model):
    __tablename__ = 'inscripciones'

    id = db.Column(db.Integer, primary_key=True)

    alumno_id = db.Column(
        db.Integer, 
        db.ForeignKey('alumnos.id'), 
        nullable=False)

    curso_id = db.Column(
        db.Integer, 
        db.ForeignKey('cursos.id'), 
        nullable=False)
    
    maestro_id = db.Column(
        db.Integer,
        db.ForeignKey('maestros.id'), 
        nullable=False)
    
    fecha_inscripcion = db.Column(
        db.DateTime, 
        default=datetime.datetime.now)
    
    __table_args__ = (
        db.UniqueConstraint('alumno_id', 'curso_id', 
                            name='uq_alumno_curso'),
    )
