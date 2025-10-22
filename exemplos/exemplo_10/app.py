
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

@app.route('/registrar_usuario')
def registrar_usuario():
    return render_template("registrar_usuario.html")

@app.route('/adicionar_usuario', methods=['GET','POST'])
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

@app.route('/usuarios', endpoint='usuarios')
def list_usuarios():
    global usuarios
    return render_template("usuarios.html", devices=usuarios)

@app.route('/sensores')
def list_sensores():
    sensores = {'Umidade': 22, 'Temperatura': 23, 'Luminosidade': 1034}
    return render_template("sensores.html", devices=sensores)

@app.route('/atuadores')
def list_atuadores():
    atuadores = {'Umidade': 22, 'Temperatura': 23, 'Luminosidade': 1034}
    return render_template("atuadores.html", devices=atuadores)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
