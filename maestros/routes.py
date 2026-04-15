# Blueprint es para manejarlo como módulos
from . import maestros_bp
from flask import Flask, render_template, request, redirect, url_for
from models import db
from models import Maestros

import forms
@maestros_bp.route("/maestros")
def maestros():
	creat_maestro=forms.UserForm(request.form)
	maestros_list=Maestros.query.all()
	return render_template("maestros/maestros.html", form=creat_maestro, maestros=maestros_list)
@maestros_bp.route("/nuevo_maestro", methods=['GET','POST'])
def nuevo_maestro():
    create_form=forms.UserForm(request.form)
    if request.method=='POST':
        maestro=Maestros(nom=create_form.nom.data,
                         apa=create_form.apa.data,
                         ama=create_form.ama.data,
                         edad=create_form.edad.data,
                         email=create_form.email.data)
        db.session.add(maestro)
        db.session.commit()
        return redirect(url_for('maestros.maestros'))
    return render_template("maestros/maestros_nuevo.html", form=create_form)

@maestros_bp.route("/detalles_maestro", methods=['GET','POST'])
def detalles_maestro():
    create_form=forms.UserForm(request.form)
    id = None
    nom = None
    apa = None
    ama = None
    edad = None
    email = None
    
    if request.method=='GET':
         id=request.args.get('id')
         maestro = db.session.query(Maestros).filter(Maestros.id==id).first()
         nom=maestro.nom
         apa=maestro.apa
         ama=maestro.ama
         edad=maestro.edad     
         email=maestro.email
         
    return render_template('maestros/maestros_detalles.html',id=id,nom=nom,apa=apa,
                           ama=ama,edad=edad,email=email)

@maestros_bp.route("/modificar_maestro", methods=['GET','POST'])
def modificar_maestro():
    create_form=forms.UserForm(request.form)
    if request.method=='GET':
         id=request.args.get('id')
         maestro = db.session.query(Maestros).filter(Maestros.id==id).first()
         create_form.id.data=request.args.get('id')
         create_form.nom.data=maestro.nom
         create_form.apa.data=maestro.apa
         create_form.ama.data=maestro.ama
         create_form.edad.data=maestro.edad
         create_form.email.data=maestro.email
    
    if request.method=='POST':
        id=request.form.get('id')
        maestro = db.session.query(Maestros).filter(Maestros.id==id).first()
        maestro.nom=create_form.nom.data
        maestro.apa=create_form.apa.data
        maestro.ama=create_form.ama.data
        maestro.edad=create_form.edad.data
        maestro.email=create_form.email.data
        db.session.add(maestro)
        db.session.commit()
        return redirect(url_for('maestros.maestros'))
    return render_template("maestros/maestros_modificar.html", form=create_form)

@maestros_bp.route('/eliminar_maestro', methods=['GET','POST'])
def eliminar_maestro():
    create_form=forms.UserForm(request.form)
    if request.method=='GET':
         id=request.args.get('id')
         maestro = db.session.query(Maestros).filter(Maestros.id==id).first()
         create_form.id.data=request.args.get('id')
         create_form.nom.data=maestro.nom
         create_form.apa.data=maestro.apa
         create_form.ama.data=maestro.ama
         create_form.edad.data=maestro.edad    
         create_form.email.data=maestro.email
    if request.method=='POST':
         id=request.form.get('id')
         maestro = Maestros.query.get_or_404(id)
         db.session.delete(maestro) 
         db.session.commit()
         return redirect(url_for('maestros.maestros'))
    return render_template('maestros/maestros_eliminar.html', form=create_form)