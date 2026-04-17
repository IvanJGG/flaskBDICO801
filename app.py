from config import Config
from flask import Flask, render_template, request, redirect, url_for
from flask import flash
from flask_wtf.csrf import CSRFProtect
from flask_migrate import Migrate
from config import DevelopmentConfig
from models import db, Alumnos, Maestros, Curso
from maestros.routes import maestros_bp
from alumnos.routes import alumnos_bp
from cursos.routes import curso_bp
from inscripciones.routes import inscripcion_bp
from jinja2 import FileSystemLoader
from sqlalchemy import text
import forms
import os

app = Flask(__name__)
app.register_blueprint(maestros_bp)
app.register_blueprint(alumnos_bp)
app.register_blueprint(curso_bp)
app.register_blueprint(inscripcion_bp)
app.jinja_loader = FileSystemLoader([
    os.path.join(os.path.dirname(__file__), 'templates'),
    os.path.dirname(__file__)
])
app.config.from_object(DevelopmentConfig)
db.init_app(app)
migrate = Migrate(app, db)
csrf = CSRFProtect(app)

@app.route("/", methods=["GET", "POST"])
def index():
	return render_template("index.html")

@app.route("/consulta", methods=["GET"])
def consulta():
    tipo = request.args.get("tipo", "alumnos")
    q = request.args.get("q", "")
    resultados = []
    
    # Filtramos usando like() para buscar coincidencias parciales
    if tipo == "alumnos":
        resultados = Alumnos.query.filter(
            (Alumnos.nom.like(f"%{q}%")) | 
            (Alumnos.apa.like(f"%{q}%")) | 
            (Alumnos.ama.like(f"%{q}%")) |
            (Alumnos.email.like(f"%{q}%"))
        ).all()
    elif tipo == "maestros":
        resultados = Maestros.query.filter(
            (Maestros.nom.like(f"%{q}%")) | 
            (Maestros.apa.like(f"%{q}%")) | 
            (Maestros.ama.like(f"%{q}%")) |
            (Maestros.matricula.like(f"%{q}%")) |
            (Maestros.email.like(f"%{q}%"))
        ).all()
    elif tipo == "cursos":
        resultados = Curso.query.filter(
            (Curso.nom.like(f"%{q}%")) |
            (Curso.descripcion.like(f"%{q}%"))
        ).all()
        
    return render_template("consulta.html", resultados=resultados, tipo=tipo, q=q)

if __name__ == '__main__':
	csrf.init_app(app)
	app.run()
