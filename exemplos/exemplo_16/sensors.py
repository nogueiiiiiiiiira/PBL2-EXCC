# sensors.py
from flask import Blueprint, request, render_template

sensor_ = Blueprint("sensor", __name__, template_folder="templates")

sensores = {
    "Sensor1": "Temperatura",
    "Sensor2": "Umidade", 
    "Sensor3": "Luminosidade"
}

@sensor_.route('/sensors')
def list_sensors():
    return render_template("sensors.html", devices=sensores)

@sensor_.route('/register_sensor')
def register_sensor():
    return render_template("register_sensor.html")

@sensor_.route('/add_sensor', methods=['GET','POST'])
def add_sensor():
    global sensores
    if request.method == 'POST':
        nome = request.form['nome']
        tipo = request.form['tipo']
    else:
        nome = request.args.get('nome', None)
        tipo = request.args.get('tipo', None)
    sensores[nome] = tipo
    return render_template("sensors.html", devices=sensores)

@sensor_.route('/remove_sensor')
def remove_sensor():
    return render_template("remove_sensor.html", devices=sensores)

@sensor_.route('/del_sensor', methods=['GET','POST'])
def del_sensor():
    global sensores
    if request.method == 'POST':
        sensor = request.form['sensor']
    else:
        sensor = request.args.get('sensor', None)
    if sensor in sensores:
        sensores.pop(sensor)
    return render_template("sensors.html", devices=sensores)
