# sensores.py
from flask import Blueprint, request, render_template

sensor_ = Blueprint("sensor", __name__, template_folder="templates")

sensores = []

@sensor_.route('/sensores')
def list_sensores():
    return render_template("sensores.html", devices=sensores)

@sensor_.route('/registrar_sensor')
def registrar_sensor():
    return render_template("registrar_sensor.html")

@sensor_.route('/adicionar_sensor', methods=['GET','POST'])
def adicionar_sensor():
    global sensores
    if request.method == 'POST':
        nome = request.form['nome']
        sensores.append(nome)
    else:
        nome = request.args.get('nome')
        if nome:
            sensores.append(nome)
    return render_template("sensores.html", devices=sensores)

@sensor_.route('/remover_sensor')
def remover_sensor():
    return render_template("remover_sensor.html", devices=sensores)

@sensor_.route('/del_sensor', methods=['GET','POST'])
def del_sensor():
    global sensores
    if request.method == 'POST':
        sensor = request.form['sensor']
    else:
        sensor = request.args.get('sensor')
    if sensor in sensores:
        sensores.remove(sensor)
    return render_template("sensores.html", devices=sensores)
