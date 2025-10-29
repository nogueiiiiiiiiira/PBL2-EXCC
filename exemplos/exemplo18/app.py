
from flask import Flask, render_template

app = Flask(__name__, static_folder = '../../static')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/home')
def home():
    return render_template("home.html")

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(405)
def method_not_allowed(error):
    return "Método não permitido", 405

@app.errorhandler(401)
def unauthorized(error):
    return "Usuário não autorizado", 401

@app.errorhandler(500)
def internal_server_error(error):
    return "Erro interno do servidor", 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
