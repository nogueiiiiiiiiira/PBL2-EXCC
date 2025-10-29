from flask import Flask, render_template, request, redirect, url_for, session
from functools import wraps
from login import login, usuarios
from sensores import sensores, sensores_lista

app = Flask(__name__, static_folder='../../static')
app.secret_key = 'chave_secreta_aqui'

app.register_blueprint(login, url_prefix='/')
app.register_blueprint(sensores, url_prefix='/sensores')

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logado' not in session:
            return redirect('/')
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def login_route():
    if 'logado' in session:
        return redirect('/home')
    return render_template("login.html")

@app.route('/home')
@login_required
def home():
    return render_template("home.html")

@app.route('/registrar_usuario')
@login_required
def registrar_usuario():
    return render_template("registrar_usuario.html")

@app.route('/listar_usuarios')
@login_required
def listar_usuarios():
    return render_template("usuarios.html", usuarios=usuarios)

@app.route('/remover_usuario')
@login_required
def remover_usuario():
    return render_template("remover_usuario.html", usuarios=usuarios)

@app.route('/registrar_sensor')
@login_required
def registrar_sensor():
    return render_template("registrar_sensor.html")

@app.route('/listar_sensores')
@login_required
def listar_sensores():
    return render_template("sensores.html", sensores_lista=sensores_lista)

@app.route('/remover_sensor')
@login_required
def remover_sensor():
    return render_template("remover_sensor.html", sensores_lista=sensores_lista)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)