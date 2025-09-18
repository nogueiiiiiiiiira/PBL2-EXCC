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

@app.route('/sensores')
def sensores():
    sensores = {'Sensor de Temperatura': 1, 'Sensor de Umidade': 0, 'Sensor de Luz': 1}
    atuadores = {'Aquecedor': 0, 'Ventilador': 1, 'Interruptor': 0}
    return render_template("sensores.html", sensores = sensores, atuadores = atuadores)

@app.route('/atuadores')
def atuadores():
    sensores = {
        'Sensor de Temperatura': 1, 'Sensor de Umidade': 0, 'Sensor de Luz': 1}
    atuadores = {'Aquecedor': 0, 'Ventilador': 1, 'Interruptor': 0}
    return render_template("atuadores.html", sensores = sensores, atuadores = atuadores)

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 8080, debug = True)