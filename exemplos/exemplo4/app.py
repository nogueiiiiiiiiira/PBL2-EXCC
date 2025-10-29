from flask import Flask
app = Flask(__name__, static_folder = '../../static')

@app.route('/')
def index():
    return """
<html>
    <head>
        <title>Minha Casa</title>
        <link rel="stylesheet" href="/static/css/style.css">
    </head>
    <body>
    <h1>MINHA CASA</h1>
        <h2>Acesse o menu:</h2>
        <ul>
            <li><a class="botao" href="/sensores">Listar Sensores</a></li>
            <li><a class="botao" href="/atuadores">Listar Atuadores</a></li>
        </ul>
    </body>
</html>
"""

@app.route('/sensores')
def sensores():
    return """
<html>
    <head>
        <title>Minha Casa</title>
    <link rel="stylesheet" href="/static/css/style.css">
    </head>
    <body>
        <h1>Sensores</h1>
        <br>
        <ul>
            <li><a>Sensor de Temperatura</a></li>
            <li><a>Sensor de Umidade</a></li>
            <li><a>Sensor de Luz</a></li>
        </ul>
        <br>
        <br>
        <a class="botao" href="/">Voltar</a>
    </body>
</html>
"""

@app.route('/atuadores')
def atuadores():
    return """
<html>
    <head>
        <title>Minha Casa</title>
    <link rel="stylesheet" href="/static/css/style.css">
    </head>
    <body>
        <h1>Atuadores</h1>
        <br>
        <ul>
            <li>Servo Motor</li>
            <li>Lâmpada</li>
        </ul>
        <br>
        <br>
        <a class="botao" href="/">Voltar</a>
    </body>
</html>
"""

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
