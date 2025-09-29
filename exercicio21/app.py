from flask import Flask, render_template, request, redirect, url_for
from login import login, usuarios
from sensores import sensores, sensores_lista
from atuadores import atuadores, atuadores_lista

app = Flask(__name__, static_folder = '../static')
app.register_blueprint(login, url_prefix = '/')
app.register_blueprint(sensores, url_prefix = '/sensores')
app.register_blueprint(atuadores, url_prefix = '/atuadores')

@app.route('/')
def login():
    return render_template("login.html")

@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/registrar_usuario')
def registrar_usuario():
    return render_template("registrar_usuario.html")

@app.route('/listar_usuarios')
def listar_usuarios():
    return render_template("usuarios.html", usuarios = usuarios)

@app.route('/remover_usuario')
def remover_usuario():
    return render_template("remover_usuario.html", usuarios = usuarios)

@app.route('/registrar_sensor')
def registrar_sensor():
    return render_template("registrar_sensor.html")

@app.route('/listar_sensores')
def listar_sensores():
    return render_template("sensores.html", sensores_lista = sensores_lista)

@app.route('/remover_sensor')
def remover_sensor():
    return render_template("remover_sensor.html", sensores_lista = sensores_lista)

@app.route('/registrar_atuador')
def registrar_atuador():
    return render_template("registrar_atuador.html")

@app.route('/listar_atuadores')
def listar_atuadores():
    return render_template("atuadores.html", atuadores_lista = atuadores_lista)

@app.route('/remover_atuador')
def remover_atuador():
    return render_template("remover_atuador.html", atuadores_lista = atuadores_lista)

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 8080, debug = True)
