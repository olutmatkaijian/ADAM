from adam_v2 import app, socketio
from config import ADAM_PSK
from flask_socketio import Namespace, emit

@socketio.on('connect', namespace='/register_device')
def on_connect():
    print("Connection to server established")

@socketio.on('message', namespace='/register_device')
def on_message(msg):
    print(str(msg))

    socketio.emit("response event", "RECV ACK", namespace='/register_device')

@socketio.on('register_device_uuid', namespace='/register_device')
def on_register_device(msg):
    print(str(msg))

    if msg['PSK'] == str(ADAM_PSK):
        socketio.emit('uuid event', "NEW UUID", namespace = '/register_device')
    else:
        socketio.emit('uuid event', "FAIL", namespace = '/register_device')
