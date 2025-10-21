
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, static_folder = '../../static')

usuarios = {
    'usuario@gmail.com': '1234',
    'usuario2@gmail.com': '1234'
}

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/validated_usuario', methods=['POST'])
def validated_usuario():
    if request.method == 'POST':
        usuario = request.form['usuario']
        password = request.form['password']
        print(usuario, password)
        if usuario in usuarios and usuarios[usuario] == password:
            return render_template('home.html')
        else:
            return '<h1>invalid credentials!</h1>'
    else:
        return render_template('login.html')

@app.route('/register_usuario')
def register_usuario():
    return render_template("register_usuario.html")

@app.route('/add_usuario', methods=['GET','POST'])
def add_usuario():
    global usuarios
    if request.method == 'POST':
        usuario = request.form['usuario']
        password = request.form['password']
    else:
        usuario = request.args.get('usuario', None)
        password = request.args.get('password', None)
    usuarios[usuario] = password
    return render_template("usuarios.html", devices=usuarios)

@app.route('usuarios')
def list_usuarios():
    global usuarios
    return render_template("usuarios.html", devices=usuarios)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
