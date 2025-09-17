from flask import Flask, render_template, request
app = Flask(__name__, static_folder = '../static')

usuarios = {
    'usuario1@gmail.com' : '1234',
    'usuario2@gmail.com' : '1234'
}

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
    
@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/sensores')
def sensores():
    return render_template("sensores.html")

@app.route('/atuadores')
def atuadores():
    return render_template("atuadores.html")

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 8080, debug = True)