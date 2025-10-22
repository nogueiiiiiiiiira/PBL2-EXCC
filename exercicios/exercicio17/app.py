from flask import Flask, render_template, request
app = Flask(__name__, static_folder = '../../static')

global usuarios
global sensores
global atuadores

usuarios = {
    'usuario@gmail.com@gmail.com' : '1234',
    'usuario2@gmail.com@gmail.com' : '1234'
}

sensores = {}
atuadores = {}

@app.route('/')
def login():
    return render_template("login.html")

@app.route('/validar_usuario', methods=['POST'])
def validar_usuario():
    if request.method == 'POST':
        usuario = request.form['usuario']
        password = request.form['password']
        print(usuario, password)
        if usuario in usuarios and usuarios[usuario] == password:
            return render_template('home.html')
        else:
            return '<h1>Credenciais Inválidas!</h1>'
    else:
        return render_template('login.html')
    
@app.route('/registrar_usuario')
def registrar_usuario():
    return render_template("registrar_usuario.html")

@app.route('/registrar_sensor')
def registrar_sensor():
    return render_template("registrar_sensor.html")

@app.route('/registrar_atuador')
def registrar_atuador():
    return render_template("registrar_atuador.html")

@app.route('/adicionar_usuario', methods = ['GET', 'POST'])
def adicionar_usuario():
    if request.method == 'POST':
        usuario = request.form['usuario']
        password = request.form['password']
    else:
        usuario = request.args.get('usuario')
        password = request.args.get('password')
    usuarios[usuario] = password
    return render_template("usuarios.html", usuarios = usuarios)

@app.route('/adicionar_sensor', methods = ['GET', 'POST'])
def adicionar_sensor():
    if request.method == 'POST':
        sensor = request.form['sensor']
        sensores[sensor] = True
    else:
        sensor = request.args.get('sensor')
        if sensor:
            sensores[sensor] = True

    return render_template("sensores.html", sensores = sensores)

@app.route('/adicionar_atuador', methods = ['GET', 'POST'])
def adicionar_atuador():
    if request.method == 'POST':
        atuador = request.form['atuador']
        atuadores[atuador] = True
    else:
        atuador = request.args.get('atuador')
        if atuador:
            atuadores[atuador] = True

    return render_template("atuadores.html", atuadores = atuadores)

@app.route('/listar_usuarios')
def listar_usuarios():
    return render_template("usuarios.html", usuarios = usuarios)

@app.route('/listar_sensores')
def listar_sensores():
    return render_template("sensores.html", sensores = sensores)

@app.route('/listar_atuadores')
def listar_atuadores():
    return render_template("atuadores.html", atuadores = atuadores)

@app.route('/remover_usuario')
def remover_usuario():
    return render_template("remover_usuario.html", usuarios = usuarios)

@app.route('/remover_sensor')
def remover_sensor():
    return render_template("remover_sensor.html", sensores = sensores)

@app.route('/remover_atuador')
def remover_atuador():
    return render_template("remover_atuador.html", atuadores = atuadores)

@app.route('/deletar_usuario', methods = ['GET', 'POST'])
def deletar_usuario():
    if request.method == 'POST':
        usuario = request.form['usuario']
        if usuario in usuarios:
            usuarios.pop(usuario)
    else:
        usuario = request.args.get('usuario')
        if usuario and usuario in usuarios:
            usuarios.pop(usuario)

    return render_template("usuarios.html", usuarios = usuarios)

@app.route('/deletar_atuador', methods = ['GET', 'POST'])
def deletar_atuador():
    if request.method == 'POST':
        atuador = request.form['atuador']
        if atuador in atuadores:
            atuadores.pop(atuador)
    else:
        atuador = request.args.get('atuador')
        if atuador and atuador in atuadores:
            atuadores.pop(atuador)

    return render_template("atuadores.html", atuadores = atuadores)

@app.route('/deletar_sensor', methods = ['GET', 'POST'])
def deletar_sensor():
    if request.method == 'POST':
        sensor = request.form['sensor']
        if sensor in sensores:
            sensores.pop(sensor)
    else:
        sensor = request.args.get('sensor')
        if sensor and sensor in sensores:
            sensores.pop(sensor)

    return render_template("sensores.html", sensores = sensores)

@app.route('/home')
def home():
    return render_template("home.html")


if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 8080, debug = True)
