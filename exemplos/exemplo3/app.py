
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Conteúdo da Página Inicial!"

@app.route('/sensores')
def sensores():
    return "Listar Sensores"

@app.route('/atuadores')
def atuadores():
    return "Listar Atuadores"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
