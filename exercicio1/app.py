from flask import Flask

app = Flask(__name__, static_folder='../static')
@app.route('/')
def index():
    return """
<html>
<head>
    <title>Minha Casa</title>
    <link rel="stylesheet" href="/static/style.css">
</head>
<body>
    <h1>MINHA CASA</h1>
    <h2>Acesse o menu:</h2>
    <ul>
        <button onclick="window.location.href='/sensores'">Sensores</button>
        <button onclick="window.location.href='/atuadores'">Atuadores</button>
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
    <link rel="stylesheet" href="/static/style.css">
</head>
<body>
    <h1>MINHA CASA</h1>
    <h2>Sensores:</h2>
    <ul>
        <li><a>Sensor de Temperatura</a></li>
        <li><a>Sensor de Umidade</a></li>
        <li><a>Sensor de Luz</a></li>
    </ul>
    <br>
    <br>
    <button onclick="window.location.href='/'">Voltar</button>
</body>
</html>

"""

@app.route('/atuadores')
def atuadores():
    return """
<html>
<head>
    <title>Minha Casa</title>
    <link rel="stylesheet" href="/static/style.css">
</head>
<body>
    <h1>MINHA CASA</h1>
    <h2>Atuadores:</h2>
    <ul>
        <li><a>Aquecedor</a></li>
        <li><a>Ventilador</a></li>
        <li><a>Interruptor</a></li>
    </ul>
    <br>
    <br>
    <button onclick="window.location.href='/'">Voltar</button>
</body>
</html>

"""

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 8080, debug = True)
    

