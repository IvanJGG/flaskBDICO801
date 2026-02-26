from flask_sqlalchemy import SQLAlchemy #ORM
import datetime

db = SQLAlchemy()

class Alumnos(db.Model):
    __tablename__ = 'alumnos'
    id = db.Column(db.Integer, primary_key=True)
    mat = db.Column(db.String(20), unique=True, nullable=False)
    nom = db.Column(db.String(50), nullable=False)
    apa = db.Column(db.String(50), nullable=False)
    ama = db.Column(db.String(50), nullable=False)
    edad = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

   