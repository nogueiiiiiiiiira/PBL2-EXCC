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
    <br>
    <ul>
        <a class="botao" href="/quarto">Quarto</a>
        <li><a class="botao" href="/banheiro">Banheiro</a></li>
    </ul>
</body>
</html>
"""

@app.route('/banheiro')
def banheiro():
    return """
<html>
<head>
    <title>Minha Casa</title>
        <link rel="stylesheet" href="/static/css/style.css">
</head>
<body>
    <h1>MINHA CASA</h1>
    <h2>Sensores do Banheiro:</h2>
    <ul>
        <li><a>Sensor de Temperatura</a></li>
        <li><a>Sensor de Umidade</a></li>
    </ul>
    <br>
    <br>
    <a class="botao" href="/">Voltar</a>
</body>
</html>

"""

@app.route('/quarto')
def quarto():
    return """
<html>
<head>
    <title>Minha Casa</title>
        <link rel="stylesheet" href="/static/css/style.css">
</head>
<body>
    <h1>MINHA CASA</h1>
    <h2>Sensores do Quarto:</h2>
    <ul>
        <li><a>Sensor de Temperatura</a></li>
        <li><a>Sensor de Umidade</a></li>
    </ul>
    <br>
    <br>
    <a class="botao" href="/">Voltar</a>
</body>
</html>

"""

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 8080, debug = True)
    

