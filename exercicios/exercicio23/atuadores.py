from flask import Blueprint, render_template, request, redirect, url_for, session
from functools import wraps

atuadores = Blueprint("atuadores", __name__, template_folder="templates")

atuadores_lista = {}

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logado' not in session:
            return redirect('/')
        return f(*args, **kwargs)
    return decorated_function

@atuadores.route('/adicionar_atuador', methods=['GET', 'POST'])
@login_required
def adicionar_atuador():
    if request.method == 'POST':
        atuador = request.form['atuador']
        atuadores_lista[atuador] = True
    else:
        atuador = request.args.get('atuador')
        if atuador:
            atuadores_lista[atuador] = True

    return render_template("atuadores.html", atuadores_lista=atuadores_lista)

@atuadores.route('/deletar_atuador', methods=['GET', 'POST'])
@login_required
def deletar_atuador():
    if request.method == 'POST':
        atuador = request.form['atuador']
        if atuador in atuadores_lista:
            atuadores_lista.pop(atuador)
    else:
        atuador = request.args.get('atuador')
        if atuador and atuador in atuadores_lista:
            atuadores_lista.pop(atuador)

    return render_template("atuadores.html", atuadores_lista=atuadores_lista)