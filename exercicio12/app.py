
from flask import Flask, render_template

app = Flask(__name__, static_folder='../static')
@app.route('/')
def index():
    return render_template("menu.html")

@app.route('/quarto')
def quarto():
    return render_template("quarto.html")

@app.route('/banheiro')
def banheiro():
    return render_template("banheiro.html")

@app.route('/sensores/<local>')
def sensores(local):
    sensores = {'Sensor de Temperatura': 301, 'Sensor de Umidade': 302, 'Sensor de Luz': 303}
    atuadores = {'Aquecedor': 401, 'Ventilador': 402, 'Interruptor': 403}

    if local == "quarto":
        local_usuario = "Quarto"
    else:
        local_usuario = "Banheiro"

    return render_template("sensores.html", sensores = sensores, atuadores = atuadores, local_usuario = local_usuario)

@app.route('/atuadores/<local>')
def atuadores(local):
    sensores = {'Sensor de Temperatura': 301, 'Sensor de Umidade': 302, 'Sensor de Luz': 303}
    atuadores = {'Aquecedor': 401, 'Ventilador': 402, 'Interruptor': 403}

    if local == "quarto":
        local_usuario = "Quarto"
    else:
        local_usuario = "Banheiro"
        
    return render_template("atuadores.html", sensores = sensores, atuadores = atuadores, local_usuario = local_usuario)

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 8080, debug = True)