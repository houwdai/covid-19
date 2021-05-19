from flask import Flask ## import Flask
from flask import *
from flask import request
from app.models.user import User  ## import kelas User dari model
from app.models.form import data


app = Flask(__name__)

@app.route('/', methods = ['GET'])
def index():
	user = User() ## membuat objek dari kelas user
	nama = user.getName() ## memanggil method untuk mengambil nama
	return render_template('index.html', nama=nama)

@app.route('/ini_system', methods=['GET', 'POST'])
def form():
    # form = data()
    form = data(request.form, csrf_enabled=False)
    return render_template('system.html', form=form)

