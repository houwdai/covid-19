from app import app
from flask import render_template
from flask import request
from app.models.user import User ## import kelas User dari model
from app.models.form import data
from flask_wtf import Form
from flask_wtf import *
from wtforms.fields.core import RadioField
from wtforms.fields.simple import SubmitField

@app.route('/', methods = ['GET'])
def index():
	user = User() ## membuat objek dari kelas user
	nama = user.getName() ## memanggil method untuk mengambil nama
	return render_template('index.html', nama=nama)

# @app.route('/ini_system')
# def hello():
#     # pertanyaan = Pertanyaan()
#     # pertanyaan = pertanyaan.getPertanyaan()
#     # return render_template('system.html', pertanyaan=pertanyaan)

@app.route('/ini_system', method=['GET', 'POST'])
def form():
    form = data()
    return render_template('system.html', formform=form)
