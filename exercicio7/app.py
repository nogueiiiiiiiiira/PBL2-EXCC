from flask import Flask, render_template

app = Flask(__name__, static_folder='../static')
@app.route('/')
def index():
    return render_template("menu.html")

@app.route('/sensores')
def sensores():
    sensores = {'Sensor de Temperatura': 301, 'Sensor de Umidade': 302, 'Sensor de Luz': 303}
    atuadores = {'Aquecedor': 401, 'Ventilador': 402, 'Interruptor': 403}
    return render_template("sensores.html", sensores = sensores, atuadores = atuadores)

@app.route('/atuadores')
def atuadores():
    sensores = {'Sensor de Temperatura': 301, 'Sensor de Umidade': 302, 'Sensor de Luz': 303}
    atuadores = {'Aquecedor': 401, 'Ventilador': 402, 'Interruptor': 403}
    return render_template("atuadores.html", sensores = sensores, atuadores = atuadores)

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 8080, debug = True)