from flask import Blueprint

inscripcion_bp=Blueprint(
	'inscripciones',
	 __name__,
	 template_folder='templates')

from . import routes