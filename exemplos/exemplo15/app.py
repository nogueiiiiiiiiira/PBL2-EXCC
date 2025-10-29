
from flask import Flask, render_template, redirect, url_for, request
from login import login
from sensores import sensor_
from atuadores import atuador_

app = Flask(__name__, static_folder = '../../static')

app.register_blueprint(login, url_prefix='/')
app.register_blueprint(sensor_, url_prefix='/')
app.register_blueprint(atuador_, url_prefix='/')

@app.route('/')
def index():
    return render_template('login.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
