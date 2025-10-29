from flask import Blueprint, render_template, request, redirect, url_for, session
from functools import wraps

login = Blueprint("login", __name__, template_folder="templates")

usuarios = {
    'usuario@gmail.com': '1234',
    'usuario2@gmail.com': '1234'
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

@login.route('/validar_usuario', methods=['POST'])
def validar_usuario():
    if request.method == 'POST':
        usuario = request.form['usuario']
        password = request.form['password']
        print(usuario, password)
        if usuario in usuarios and usuarios[usuario] == password:
            session['logado'] = True
            session['usuario'] = usuario
            return redirect('/home')
        else:
            return '<h1>Credenciais Inválidas!</h1>'
    else:
        return render_template('login.html')

@login.route('/home')
@login_required
def home():
    return render_template('home.html')

@login.route('/usuarios')
@login_required
def listar_usuarios():
    return render_template("usuarios.html", usuarios=usuarios)

@login.route('/adicionar_usuario', methods=['GET', 'POST'])
@login_required
def adicionar_usuario():
    if request.method == 'POST':
        usuario = request.form['usuario']
        password = request.form['password']
    else:
        usuario = request.args.get('usuario')
        password = request.args.get('password')
    usuarios[usuario] = password
    return render_template("usuarios.html", usuarios=usuarios)

@login.route('/deletar_usuario', methods=['GET', 'POST'])
@login_required
def deletar_usuario():
    if request.method == 'POST':
        usuario = request.form['usuario']
        if usuario in usuarios:
            usuarios.pop(usuario)
    else:
        usuario = request.args.get('usuario')
        if usuario and usuario in usuarios:
            usuarios.pop(usuario)
    return render_template("usuarios.html", usuarios=usuarios)

@login.route('/logout')
def logout():
    session.clear()
    return redirect('/')