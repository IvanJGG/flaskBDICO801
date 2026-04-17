from . import curso_bp
from flask import Flask, render_template, request, redirect, url_for
from models import db
from models import Curso, Alumnos, Inscripcion, Maestros

import forms

@curso_bp.route("/cursos")
def cursos():
    form = forms.CursoForm()
    cursos_list = Curso.query.all()
    return render_template("cursos/cursos.html", cursos=cursos_list, form=form)

@curso_bp.route("/nuevo_curso", methods=['GET', 'POST'])
def nuevo_curso():
    form = forms.CursoForm(request.form)
    maestros = Maestros.query.all()
    if request.method == 'POST' and form.validate():
        curso = Curso(nom=form.nom.data, descripcion=form.descripcion.data, maestro_id=form.maestro_id.data)
        db.session.add(curso)
        db.session.commit()
        return redirect(url_for('curso.cursos'))
    return render_template("cursos/nuevo_curso.html", form=form, maestros=maestros)

@curso_bp.route("/modificar_curso", methods=['GET', 'POST'])
def modificar_curso():
    form = forms.CursoForm(request.form)
    maestros = Maestros.query.all()
    
    # Obtenemos el ID ya sea de la URL (GET) o del formulario (POST)
    id = request.args.get('id') or request.form.get('id')
    
    if request.method == 'GET':
        curso = Curso.query.get_or_404(id)
        form.id.data = curso.id
        form.nom.data = curso.nom
        form.descripcion.data = curso.descripcion
        form.maestro_id.data = curso.maestro_id
    
    if request.method == 'POST' and form.validate():
        curso = Curso.query.get_or_404(id)
        curso.nom = form.nom.data
        curso.descripcion = form.descripcion.data
        curso.maestro_id = form.maestro_id.data
        db.session.commit()
        return redirect(url_for('curso.cursos'))
    return render_template("cursos/modificar_cursos.html", form=form, maestros=maestros)

@curso_bp.route("/detalles_cursos")
def detalles_cursos():
    id = request.args.get('id')
    curso = Curso.query.get_or_404(id)
    return render_template("cursos/detalles_cursos.html", curso=curso)

@curso_bp.route("/eliminar_cursos", methods=['GET', 'POST'])
def eliminar_cursos():
    form = forms.CursoForm(request.form)
    id = request.args.get('id') or request.form.get('id')
    curso = Curso.query.get_or_404(id)
    
    if request.method == 'GET':
        form.id.data = curso.id
        form.nom.data = curso.nom
        form.descripcion.data = curso.descripcion
        form.maestro_id.data = curso.maestro_id
    
    if request.method == 'POST':
        db.session.delete(curso)
        db.session.commit()
        return redirect(url_for('curso.cursos'))
    
    return render_template("cursos/eliminar_cursos.html", form=form, curso=curso, maestros=Maestros.query.all())

@curso_bp.route("/inscribir", methods=['GET', 'POST'])
def inscribir():
    form = forms.InscripcionForm(request.form)
    cursos = Curso.query.all()
    alumnos = Alumnos.query.all()
    if request.method == 'GET' and request.args.get('curso_id'):
        form.curso_id.data = request.args.get('curso_id')
    if request.method == 'POST' and form.validate():
        curso = Curso.query.get_or_404(form.curso_id.data)
        inscripcion = Inscripcion(alumno_id=form.alumno_id.data, curso_id=form.curso_id.data, maestro_id=curso.maestro_id)
        db.session.add(inscripcion)
        db.session.commit()
        return redirect(url_for('curso.cursos'))
    return render_template("inscripciones/nueva_inscripcion.html", form=form, cursos=cursos, alumnos=alumnos)