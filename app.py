from config import Config
from flask import Flask, render_template, request, redirect, url_for
from flask import flash
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
from models import db, Alumnos, Maestros
import forms

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
db.init_app(app)
csrf = CSRFProtect(app)

@app.route("/", methods=["GET", "POST"])
@app.route("/index")
def index():
	creat_alumno=forms.UserForm(request.form)
	alumno=Alumnos.query.all()
	return render_template("index.html", form=creat_alumno, alumno=alumno)

@app.route("/", methods=["GET", "POST"])
@app.route("/maestros")
def maestros():
	creat_maestro=forms.UserForm(request.form)
	maestros=Maestros.query.all()
	return render_template("maestros.html", form=creat_maestro, maestros=maestros)

@app.route("/usuarios", methods=["GET", "POST"])
def usuarios():
	id=0
	nom=''
	apa=''
	ama=''
	edad=0
	email=''
	usuario_clas=forms.UserForm(request.form)
	if request.method == "POST" and usuario_clas.validate():
		id=usuario_clas.mat.data
		nom=usuario_clas.nom.data
		apa=usuario_clas.apa.data
		ama=usuario_clas.ama.data
		edad=usuario_clas.edad.data
		email=usuario_clas.email.data

	return render_template("usuarios.html",form=usuario_clas, id=id, nom=nom, apa=apa, ama=ama, edad=edad, email=email)

if __name__ == '__main__':
	csrf.init_app(app)
	with app.app_context():
		db.create_all()
	app.run()
