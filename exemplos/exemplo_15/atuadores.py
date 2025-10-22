# atuadores.py
from flask import Blueprint, request, render_template

atuador_ = Blueprint("atuador", __name__, template_folder="templates")

atuadores = []

@atuador_.route('/atuadores')
def list_atuadores():
    return render_template("atuadores.html", devices=atuadores)

@atuador_.route('/registrar_atuador')
def registrar_atuador():
    return render_template("registrar_atuador.html")

@atuador_.route('/adicionar_atuador', methods=['GET','POST'])
def adicionar_atuador():
    global atuadores
    if request.method == 'POST':
        nome = request.form['nome']
        atuadores.append(nome)
    else:
        nome = request.args.get('nome', None)
        if nome:
            atuadores.append(nome)
    return render_template("atuadores.html", devices=atuadores)

@atuador_.route('/remover_atuador')
def remover_atuador():
    return render_template("remover_atuador.html", devices=atuadores)

@atuador_.route('/del_atuador', methods=['GET','POST'])
def del_atuador():
    global atuadores
    if request.method == 'POST':
        atuador = request.form['atuador']
    else:
        atuador = request.args.get('atuador', None)
    if atuador in atuadores:
        atuadores.remove(atuador)
    return render_template("atuadores.html", devices=atuadores)
