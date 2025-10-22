# login.py
from flask import Blueprint, request, render_template, redirect, url_for

login = Blueprint("login", __name__, template_folder="templates")

usuarios = {
    "usuario@gmail.com": "1234",
    "usuario2@gmail.com": "1234"
}

@login.route('/validated_usuario', methods=['POST'])
def validated_usuario():
    if request.method == 'POST':
        usuario = request.form['usuario']
        password = request.form['password']
        print(usuario, password)
        if usuario in usuarios and usuarios[usuario] == password:
            return render_template('home.html')
        else:
            return '<h1>Invalid Credentials</h1>'
    else:
        return render_template('login.html')

@login.route('/home')
def home():
    return render_template("home.html")

@login.route('usuarios')
def list_usuarios():
    global usuarios
    return render_template("usuarios.html", devices=usuarios)

@login.route('/registrar_usuario')
def registrar_usuario():
    return render_template("registrar_usuario.html")

@login.route('/adicionar_usuario', methods=['GET','POST'])
def adicionar_usuario():
    global usuarios
    if request.method == 'POST':
        usuario = request.form.get('usuario')
        password = request.form.get('password')
        if not usuario or not password:
            return "Usuario and password are required", 400
    else:
        usuario = request.args.get('usuario')
        password = request.args.get('password')
        if not usuario or not password:
            return "Usuario and password are required", 400
    usuarios[usuario] = password
    return render_template("usuarios.html", devices=usuarios)

@login.route('/remover_usuario')
def remover_usuario():
    return render_template("remover_usuario.html", devices=usuarios)

@login.route('/del_usuario', methods=['GET','POST'])
def del_usuario():
    global usuarios
    if request.method == 'POST':
        print(request.form)
        usuario = request.form['usuario']
    else:
        usuario = request.args.get('usuario')
    usuarios.pop(usuario)
    return render_template("usuarios.html", devices=usuarios)
