
from flask import Flask, render_template

app = Flask(__name__, static_folder='../static')
@app.route('/')
def index():
    return render_template("menu.html")

@app.route('/quarto')
def quarto():
    sensores = ['Sensor de Temperatura', 'Sensor de Umidade', 'Sensor de Luz']
    atuadores = ['Aquecedor', 'Ventilador', 'Interruptor']
    return render_template("quarto.html", sensores = sensores, atuadores = atuadores)

@app.route('/banheiro')
def banheiro():
    sensores = ['Sensor de Temperatura', 'Sensor de Umidade', 'Sensor de Luz']
    atuadores = ['Aquecedor', 'Ventilador', 'Interruptor']
    return render_template("banheiro.html", sensores = sensores, atuadores = atuadores)

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 8080, debug = True)