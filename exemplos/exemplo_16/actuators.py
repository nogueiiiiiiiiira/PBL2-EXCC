# actuators.py
from flask import Blueprint, request, render_template

actuator_ = Blueprint("actuator", __name__, template_folder="templates")

atuadores = {
    "Atuador1": "Lâmpada",
    "Atuador2": "Servo Motor", 
    "Atuador3": "Ventilador"
}

@actuator_.route('/actuators')
def list_actuators():
    return render_template("actuators.html", devices=atuadores)

@actuator_.route('/register_actuator')
def register_actuator():
    return render_template("register_actuator.html")

@actuator_.route('/add_actuator', methods=['GET','POST'])
def add_actuator():
    global atuadores
    if request.method == 'POST':
        nome = request.form['nome']
        tipo = request.form['tipo']
    else:
        nome = request.args.get('nome', None)
        tipo = request.args.get('tipo', None)
    atuadores[nome] = tipo
    return render_template("actuators.html", devices=atuadores)

@actuator_.route('/remove_actuator')
def remove_actuator():
    return render_template("remove_actuator.html", devices=atuadores)

@actuator_.route('/del_actuator', methods=['GET','POST'])
def del_actuator():
    global atuadores
    if request.method == 'POST':
        atuador = request.form['atuador']
    else:
        atuador = request.args.get('atuador', None)
    atuadores.pop(atuador)
    return render_template("actuators.html", devices=atuadores)