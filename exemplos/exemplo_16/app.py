
# app.py
from flask import Flask, render_template, request, redirect, url_for,jsonify, send_from_directory
from login import login
from sensors import sensor_
from actuators import actuator_
from flask_mqtt import Mqtt
from flask_socketio import SocketIO
import json

# https://wokwi.com/projects/322577683855704658

temperature= 10
huminity= 10

atuadores_values= 1

app = Flask(__name__, static_folder = '../../static')
## __name__ is the application name

app.register_blueprint(login, url_prefix='/')
app.register_blueprint(sensor_, url_prefix='/')
app.register_blueprint(actuator_, url_prefix='/')


app.config['MQTT_BROKER_URL'] = 'mqtt-dashboard.com'
app.config['MQTT_BROKER_PORT'] = 1883
app.config['MQTT_usuarioNAME'] = ''  # Set this item when you need to verify usuarioname and password
app.config['MQTT_PASSWORD'] = ''  # Set this item when you need to verify usuarioname and password
app.config['MQTT_KEEPALIVE'] = 5000  # Set KeepAlive time in seconds
app.config['MQTT_TLS_ENABLED'] = False  # If your broker supports TLS, set it True

mqtt_client= Mqtt()
mqtt_client.init_app(app)

topic_subscribe1 = "/aula/temperature"
topic_subscribe2 = "/aula/huminity"

@app.route('/')
def index():
    return render_template("login.html")

@app.route('/logoff')
def logoff():
    return render_template("login.html")

@app.route('/home')
def home():
    return render_template("home.html")


@app.route('/tempo_real')
def tempo_real():
    global temperature, huminity
    values = {"temperature":temperature, "huminity":huminity}
    return render_template("tr.html", values=values)

@app.route('/publish')
def publish():
    return render_template('publish.html')

@app.route('/publish_message', methods=['GET','POST'])
def publish_message():
    request_data = request.get_json()
    publish_result = mqtt_client.publish(request_data['topic'], request_data['message'])
    return jsonify(publish_result)

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory(app.static_folder, filename)


@mqtt_client.on_connect()
def handle_connect(client, usuariodata, flags, rc):
    if rc == 0:
        print('Broker Connected successfully')
        mqtt_client.subscribe(topic_subscribe1) # subscribe topic
        mqtt_client.subscribe(topic_subscribe2) # subscribe topic
    else:
        print('Bad connection. Code:', rc)

@mqtt_client.on_disconnect()
def handle_disconnect(client, usuariodata, rc):
    print("Disconnected from broker")


@mqtt_client.on_message()
def handle_mqtt_message(client, usuariodata, message):
    print(message.payload.decode())
    if(message.topic==topic_subscribe1):
        global temperature
        temperature = message.payload.decode()
    if(message.topic==topic_subscribe2):
        global huminity
        huminity = message.payload.decode()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True) 