
from flask import Flask, render_template

app = Flask(__name__, static_folder = '../../static')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/sensors')
def sensors():
    sensores = ['Umidade', 'Temperatura', 'Luminosidade']
    return render_template("sensors.html", sensores=sensores)

@app.route('/actuators')
def actuators():
    atuadores = ['Servo Motor', 'Lâmpada']
    return render_template("actuators.html", atuadores=atuadores)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
