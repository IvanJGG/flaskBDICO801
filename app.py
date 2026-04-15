from config import Config
from flask import Flask, render_template, request, redirect, url_for
from flask import flash
from flask_wtf.csrf import CSRFProtect
from flask_migrate import Migrate
from config import DevelopmentConfig
from models import db, Alumnos
from maestros.routes import maestros_bp
from alumnos.routes import alumnos_bp
from jinja2 import FileSystemLoader
import forms
import os

app = Flask(__name__)
app.register_blueprint(maestros_bp)
app.register_blueprint(alumnos_bp)
app.jinja_loader = FileSystemLoader([
    os.path.join(os.path.dirname(__file__), 'templates'),
    os.path.dirname(__file__)
])
app.config.from_object(DevelopmentConfig)
db.init_app(app)
migrate = Migrate(app, db)
csrf = CSRFProtect(app)

@app.route("/", methods=["GET"])
@app.route("/index")
def index():
	return render_template("index.html")

@app.route("/inscripciones")
def inscripciones():
    return render_template("inscripciones.html")

if __name__ == '__main__':
	csrf.init_app(app)
	with app.app_context():
		db.create_all()
	app.run()
