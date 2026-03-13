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

class Maestros(db.Model):
    __tablename__ = 'maestros'
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(250), nullable=False)
    apa = db.Column(db.String(250), nullable=False)
    ama = db.Column(db.String(250), nullable=False)
    edad = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

   