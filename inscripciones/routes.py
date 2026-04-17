from . import inscripcion_bp
from flask import Flask, render_template, request, redirect, url_for
from models import db
from models import Inscripcion, Curso, Alumnos

import forms

@inscripcion_bp.route("/inscripciones")
def inscripciones():
    inscripciones_list = Inscripcion.query.all()
    return render_template("inscripciones/inscripciones.html", inscripciones=inscripciones_list)

@inscripcion_bp.route("/nueva_inscripcion", methods=['GET', 'POST'])
def nueva_inscripcion():
    form = forms.InscripcionForm(request.form)
    cursos = Curso.query.all()
    alumnos = Alumnos.query.all()
    if request.method == 'POST' and form.validate():
        curso = Curso.query.get_or_404(form.curso_id.data)
        inscripcion = Inscripcion(alumno_id=form.alumno_id.data, curso_id=form.curso_id.data, maestro_id=curso.maestro_id)
        db.session.add(inscripcion)
        db.session.commit()
        return redirect(url_for('inscripciones.inscripciones'))
    return render_template("inscripciones/nueva_inscripcion.html", form=form, cursos=cursos, alumnos=alumnos)

@inscripcion_bp.route("/modificar_inscripcion", methods=['GET', 'POST'])
def modificar_inscripcion():
    form = forms.InscripcionForm(request.form)
    cursos = Curso.query.all()
    alumnos = Alumnos.query.all()
    id = request.args.get('id') or request.form.get('id')
    inscripcion = Inscripcion.query.get_or_404(id)
    
    if request.method == 'GET':
        form.id.data = inscripcion.id
        form.alumno_id.data = inscripcion.alumno_id
        form.curso_id.data = inscripcion.curso_id
    
    if request.method == 'POST' and form.validate():
        curso = Curso.query.get_or_404(form.curso_id.data)
        inscripcion.alumno_id = form.alumno_id.data
        inscripcion.curso_id = form.curso_id.data
        inscripcion.maestro_id = curso.maestro_id
        db.session.commit()
        return redirect(url_for('inscripciones.inscripciones'))
    
    return render_template("inscripciones/modificar_inscripcion.html", form=form, cursos=cursos, alumnos=alumnos)

@inscripcion_bp.route("/eliminar_inscripcion", methods=['GET', 'POST'])
def eliminar_inscripcion():
    form = forms.InscripcionForm(request.form)
    id = request.args.get('id') or request.form.get('id')
    inscripcion = Inscripcion.query.get_or_404(id)
    
    if request.method == 'GET':
        form.id.data = inscripcion.id
        form.alumno_id.data = inscripcion.alumno_id
        form.curso_id.data = inscripcion.curso_id
    
    if request.method == 'POST':
        db.session.delete(inscripcion)
        db.session.commit()
        return redirect(url_for('inscripciones.inscripciones'))
    
    return render_template("inscripciones/eliminar_inscripcion.html", form=form, inscripcion=inscripcion)
