from flask import Blueprint, request, render_template, redirect, url_for, session
from functools import wraps

login = Blueprint("login", __name__, template_folder="templates")

usuarios = {
    "usuario@gmail.com": "1234",
    "usuario2@gmail.com": "1234"
}

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logado' not in session:
            return redirect('/')
        return f(*args, **kwargs)
    return decorated_function

@login.route('/')
def index():
    if 'logado' in session:
        return redirect('/home')
    return render_template('login.html')

@login.route('/validated_usuario', methods=['POST'])
def validated_usuario():
    if request.method == 'POST':
        usuario = request.form['usuario']
        password = request.form['password']
        if usuario in usuarios and usuarios[usuario] == password:
            session['logado'] = True
            session['usuario'] = usuario
            return redirect('/home')
        else:
            return '<h1>Invalid Credentials</h1>'

@login.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@login.route('/home')
@login_required
def home():
    return render_template("home.html")

@login.route('/usuarios')
@login_required
def list_usuarios():
    global usuarios
    return render_template("usuarios.html", devices=usuarios)

@login.route('/registrar_usuario')
@login_required
def registrar_usuario():
    return render_template("registrar_usuario.html")

@login.route('/adicionar_usuario', methods=['GET','POST'])
@login_required
def adicionar_usuario():
    global usuarios
    if request.method == 'POST':
        usuario = request.form['usuario']
        password = request.form['password']
    else:
        usuario = request.args.get('usuario')
        password = request.args.get('password')
    usuarios[usuario] = password
    return render_template("usuarios.html", devices=usuarios)

@login.route('/remover_usuario')
@login_required
def remover_usuario():
    return render_template("remover_usuario.html", devices=usuarios)

@login.route('/del_usuario', methods=['GET','POST'])
@login_required
def del_usuario():
    global usuarios
    if request.method == 'POST':
        usuario = request.form['usuario']
    else:
        usuario = request.args.get('usuario')
    usuarios.pop(usuario)
    return render_template("usuarios.html", devices=usuarios)