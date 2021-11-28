from adam_v2 import app, socketio, db
from config import ADAM_PSK
from flask_socketio import Namespace, emit
from uuid import uuid4
#from adam_v2.models.PID_Control import PID_Controller
from flask import flash

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
        # Generate a UUID for the device and send it to the device
        device_uuid = uuid4()

        # Save the device UUID to the database as a new device
        new_device = PID_Controller(device_uuid=device_uuid)

        db.session.add(new_device)
        db.session.commit()
        flash('Successfully commited device to database')
        socketio.emit('UUID_REGISTER_SUCCESS', str(device_uuid),
            namespace = '/register_device')
            
        # Write the UUID into the device database, now the device is
        # considered trusted and can be configured
    else:
        socketio.emit('uuid event', "FAIL", namespace = '/register_device')
