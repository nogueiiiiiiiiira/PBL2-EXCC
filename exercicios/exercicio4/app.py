from flask import Flask, render_template

app = Flask(__name__, static_folder = '../../static')
@app.route('/')
def index():
    return render_template('menu.html') 

@app.route('/quarto')
def sensores():
    return render_template('quarto.html')

@app.route('/banheiro')
def atuadores():
    return render_template('banheiro.html')

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 8080, debug = True)
