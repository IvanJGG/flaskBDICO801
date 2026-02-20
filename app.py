from flask import Flask, render_template, request
import forms

app = Flask(__name__)

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
	app.run(debug=True)
