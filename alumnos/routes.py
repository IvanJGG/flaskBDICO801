# Blueprint es para manejarlo como módulos
from . import alumnos_bp
from flask import Flask, render_template, request, redirect, url_for
from models import db
from models import Alumnos

import forms
@alumnos_bp.route("/alumno")
def alumnos():
	create_alumno=forms.UserForm(request.form)
	alumnos_list=Alumnos.query.all()
	return render_template("alumnos/alumnos.html", form=create_alumno, alumnos=alumnos_list)
@alumnos_bp.route("/nuevo_alumno",methods=['GET','POST'])
def nuevo_alumno():
    create_form=forms.UserForm(request.form)
    if request.method=='POST':
        alum=Alumnos(nom=create_form.nom.data,
                     apa=create_form.apa.data,
                     ama=create_form.ama.data,
                     edad=create_form.edad.data,
                     email=create_form.email.data)
        db.session.add(alum)
        db.session.commit()
        return redirect(url_for('alumnos.alumnos'))
    return render_template("alumnos/nuevo_alumno.html",form=create_form)
@alumnos_bp.route("/detalles",methods=['GET','POST'])
def detalles():
    create_form=forms.UserForm(request.form)
    id = None
    nom = None
    apa = None
    ama = None
    edad = None
    email = None
    
    if request.method=='GET':
         id=request.args.get('id')
         #  select * from alumnos where id == id
         alum1 = db.session.query(Alumnos).filter(Alumnos.id==id).first()
         nom=alum1.nom
         apa=alum1.apa
         ama=alum1.ama
         edad=alum1.edad     
         email=alum1.email
         
    return render_template('alumnos/detalles.html',id=id,nom=nom,apa=apa,
                           ama=ama,edad=edad,email=email)

@alumnos_bp.route("/modificar",methods=['GET','POST'])
def modificar():
    create_form=forms.UserForm(request.form)
    if request.method=='GET':
         id=request.args.get('id')
         #  select * from alumnos where id == id
         alum1 = db.session.query(Alumnos).filter(Alumnos.id==id).first()
         create_form.id.data=request.args.get('id')
         create_form.nom.data=alum1.nom
         create_form.apa.data=alum1.apa
         create_form.ama.data=alum1.ama
         create_form.edad.data=alum1.edad
         create_form.email.data=alum1.email
    
    if request.method=='POST':
        id=request.form.get('id')
         #  select * from alumnos where id == id
        alum1 = db.session.query(Alumnos).filter(Alumnos.id==id).first()
        alum1.nom=create_form.nom.data
        alum1.apa=create_form.apa.data
        alum1.ama=create_form.ama.data
        alum1.edad=create_form.edad.data
        alum1.email=create_form.email.data
        db.session.add(alum1)
        db.session.commit()
        return redirect(url_for('alumnos.alumnos'))
    return render_template("alumnos/modificar.html",form=create_form)

@alumnos_bp.route('/eliminar',methods=['GET','POST'])
def eliminar():
    create_form=forms.UserForm(request.form)
    if request.method=='GET':
         id=request.args.get('id')
         #  select * from alumnos where id == id
         alum1 = db.session.query(Alumnos).filter(Alumnos.id==id).first()
         create_form.id.data=request.args.get('id')
         create_form.nom.data=alum1.nom
         create_form.apa.data=alum1.apa
         create_form.ama.data=alum1.ama
         create_form.edad.data=alum1.edad    
         create_form.email.data=alum1.email
    if request.method=='POST':
         id=request.form.get('id')
         alum = Alumnos.query.get_or_404(id)
         #delete from alumnos where id=id
         db.session.delete(alum) 
         db.session.commit()
         return redirect(url_for('alumnos.alumnos'))
    return render_template('alumnos/eliminar.html',form=create_form)