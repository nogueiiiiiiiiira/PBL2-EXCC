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
        <li><a class="botao" href="/atuadores">Atuadores</a></li>
    </ul>
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
    <h1>MINHA CASA</h1>
    <h2>Lista de Atuadores</h2>
    <ul>
        <li><a>Aquecedor</a></li>
        <li><a>Ventilador</a></li>
        <li><a>Interruptor</a></li>
    </ul>
    <br>
    <br>
    <a class="botao" href="/">Voltar</a>
</body>
</html>
"""

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 8080, debug = True)
    

