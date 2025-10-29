from flask import Blueprint, request, render_template, redirect, session
from functools import wraps

atuador_ = Blueprint("atuador", __name__, template_folder="templates")

atuadores = {
    "Atuador1": "Lâmpada",
    "Atuador2": "Servo Motor", 
    "Atuador3": "Ventilador"
}

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logado' not in session:
            return redirect('/')
        return f(*args, **kwargs)
    return decorated_function

@atuador_.route('/atuadores')
@login_required
def list_atuadores():
    return render_template("atuadores.html", devices=atuadores)

@atuador_.route('/registrar_atuador')
@login_required
def registrar_atuador():
    return render_template("registrar_atuador.html")

@atuador_.route('/adicionar_atuador', methods=['GET','POST'])
@login_required
def adicionar_atuador():
    global atuadores
    if request.method == 'POST':
        nome = request.form['nome']
    else:
        nome = request.args.get('nome')
    return render_template("atuadores.html", devices=atuadores)

@atuador_.route('/remover_atuador')
@login_required
def remover_atuador():
    return render_template("remover_atuador.html", devices=atuadores)

@atuador_.route('/del_atuador', methods=['GET','POST'])
@login_required
def del_atuador():
    global atuadores
    if request.method == 'POST':
        atuador = request.form['atuador']
    else:
        atuador = request.args.get('atuador')
    atuadores.pop(atuador)
    return render_template("atuadores.html", devices=atuadores)