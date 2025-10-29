from flask import Blueprint, render_template, request, redirect, url_for, session
from functools import wraps

sensores = Blueprint("sensores", __name__, template_folder="templates")

sensores_lista = {}

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logado' not in session:
            return redirect('/')
        return f(*args, **kwargs)
    return decorated_function

@sensores.route('/adicionar_sensor', methods=['GET', 'POST'])
@login_required
def adicionar_sensor():
    if request.method == 'POST':
        sensor = request.form['sensor']
        sensores_lista[sensor] = True
    else:
        sensor = request.args.get('sensor')
        if sensor:
            sensores_lista[sensor] = True

    return render_template("sensores.html", sensores_lista=sensores_lista)

@sensores.route('/deletar_sensor', methods=['GET', 'POST'])
@login_required
def deletar_sensor():
    if request.method == 'POST':
        sensor = request.form['sensor']
        if sensor in sensores_lista:
            sensores_lista.pop(sensor)
    else:
        sensor = request.args.get('sensor')
        if sensor and sensor in sensores_lista:
            sensores_lista.pop(sensor)

    return render_template("sensores.html", sensores_lista=sensores_lista)