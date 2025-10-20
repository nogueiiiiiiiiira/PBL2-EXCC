
from flask import Flask, render_template, abort

app = Flask(__name__, static_folder = '../../static')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/sensores')
def sensores():
    return render_template("sensores.html")

@app.route('/atuadores')
def atuadores():
    return render_template("atuadores.html")

@app.errorhandler(400)
def bad_request(error):
    return render_template('400.html'), 400

@app.route('/400')
def force_400():
    abort(400)

@app.errorhandler(401)
def unauthorized(error):
    return render_template('401.html'), 401

@app.route('/401')
def force_401():
    abort(401)

@app.errorhandler(403)
def forbidden(error):
    return render_template('403.html'), 403

@app.route('/403')
def force_403():
    abort(403)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@app.route('/404')
def force_404():
    abort(404)

@app.errorhandler(405)
def method_not_allowed(error):
    return render_template('405.html'), 405


@app.route('/405')
def force_405():
    abort(405)

@app.errorhandler(408)
def request_timeout(error):
    return render_template('408.html'), 408

@app.route('/408')
def force_408():
    abort(408)

@app.errorhandler(429)
def too_many_requests(error):
    return render_template('429.html'), 429

@app.route('/429')
def force_429():
    abort(429)

@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html'), 500

@app.route('/500')
def force_500():
    abort(500)

@app.errorhandler(503)
def service_unavailable(error):
    return render_template('503.html'), 503

@app.route('/503')
def force_503():
    abort(503)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
