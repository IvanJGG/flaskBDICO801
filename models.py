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
    cursos = db.relationship('Curso', secondary='inscripciones', back_populates='alumnos')

class Maestros(db.Model):
    __tablename__ = 'maestros'
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(250), nullable=False)
    apa = db.Column(db.String(250), nullable=False)
    ama = db.Column(db.String(250), nullable=False)
    matricula = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    created_date = db.Column(db.DateTime, default=datetime.datetime.now)
    # Relación 1:N (Un maestro tiene muchos cursos)
    cursos_dictados = db.relationship('Curso', backref='maestro_titular', lazy=True)

class Curso(db.Model):
    __tablename__ = 'cursos'
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(250), nullable=False)
    descripcion = db.Column(db.String(500), nullable=False)
    created_date = db.Column(db.DateTime, default=datetime.datetime.now)
    # Llave foránea al Maestro (Relación 1 a Muchos)
    maestro_id = db.Column(db.Integer, db.ForeignKey('maestros.id'), nullable=True)
    # Relación N:M con Alumnos
    alumnos = db.relationship('Alumnos', secondary='inscripciones', back_populates='cursos')

class Inscripcion(db.Model):
    __tablename__ = 'inscripciones'
    id = db.Column(db.Integer, primary_key=True)
    alumno_id = db.Column(db.Integer, db.ForeignKey('alumnos.id'), nullable=False)
    curso_id = db.Column(db.Integer, db.ForeignKey('cursos.id'), nullable=False)
    maestro_id = db.Column(db.Integer, db.ForeignKey('maestros.id'), nullable=True)
    created_date = db.Column(db.DateTime, default=datetime.datetime.now)
    
    # Relaciones para acceder a los objetos relacionados
    alumno = db.relationship('Alumnos', backref='inscripciones')
    curso = db.relationship('Curso', backref='inscripciones')
    
    __table_args__ = (db.UniqueConstraint('alumno_id', 'curso_id', name='uq_alumno_curso'),)