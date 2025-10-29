from flask import Blueprint, request, render_template, redirect, session
from functools import wraps

sensor_ = Blueprint("sensor", __name__, template_folder="templates")

sensores = {
    "Sensor1": "Temperatura",
    "Sensor2": "Umidade", 
    "Sensor3": "Luminosidade"
}

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logado' not in session:
            return redirect('/')
        return f(*args, **kwargs)
    return decorated_function

@sensor_.route('/sensores')
@login_required
def list_sensores():
    return render_template("sensores.html", devices=sensores)

@sensor_.route('/registrar_sensor')
@login_required
def registrar_sensor():
    return render_template("registrar_sensor.html")

@sensor_.route('/adicionar_sensor', methods=['GET','POST'])
@login_required
def adicionar_sensor():
    global sensores
    if request.method == 'POST':
        nome = request.form['nome']
    else:
        nome = request.args.get('nome')
    return render_template("sensores.html", devices=sensores)

@sensor_.route('/remover_sensor')
@login_required
def remover_sensor():
    return render_template("remover_sensor.html", devices=sensores)

@sensor_.route('/del_sensor', methods=['GET','POST'])
@login_required
def del_sensor():
    global sensores
    if request.method == 'POST':
        sensor = request.form['sensor']
    else:
        sensor = request.args.get('sensor')
    if sensor in sensores:
        sensores.pop(sensor)
    return render_template("sensores.html", devices=sensores)