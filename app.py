from config import Config
from flask import Flask, render_template, request, redirect, url_for
from flask import flash
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
from models import db, Alumnos
import forms

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
db.init_app(app)
csrf = CSRFProtect(app)

@app.route("/")
@app.route("/index")
def index():
	return render_template("index.html")

@app.route("/usuarios", methods=["GET", "POST"])
def usuarios():
	mat=0
	nom=''
	apa=''
	ama=''
	edad=0
	email=''
	usuario_clas=forms.UserForm(request.form)
	if request.method == "POST" and usuario_clas.validate():
		mat=usuario_clas.mat.data
		nom=usuario_clas.nom.data
		apa=usuario_clas.apa.data
		ama=usuario_clas.ama.data
		edad=usuario_clas.edad.data
		email=usuario_clas.email.data

	return render_template("usuarios.html",form=usuario_clas, mat=mat, nom=nom, apa=apa, ama=ama, edad=edad, email=email)

if __name__ == '__main__':
	csrf.init_app(app)
	with app.app_context():
		db.create_all()
	app.run()
