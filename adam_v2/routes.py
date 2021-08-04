7
from adam_v2 import app, socketio
from flask import render_template
# For asynchronious handling of the data collection process
import asyncio


@app.route('/index')
@app.route('/')
def index():
    return render_template("base.html", title="ADAM 0.1")



# Database viewer to see database scheme for debug purposes
@app.route('/database_viewer')
def database_viewer():
    return render_template("base.html", title="DB Viewer")

# About page
@app.route('/about')
def about():
    return render_template("base.html", title="About ADAM")

# Process Designer
# This is where for example, "PID CONTROLLER 1 SET TEMPERATURE 40" is done
@app.route('/process_designer')
def process_designer():
    return render_template("base.html", title="Process Designer")

# Process Status
# This is where you can see the ongoing process
@app.route('/process_status')
def process_status():
    return render_template("base.html", title="Process Status")

# Hardware Setup
# This is where you can set up new hardware
@app.route("/hardware_setup")
def hardware_setup():
    return render_template("base.html", title="hardware setup")

    
# When a new device wants to be added, check its pre-shared key against the ADAM PSK
@socketio.on("OBTAIN_UUID", namespace="/Register_Device")
def register_device(data):
    print("Recieved Data: ", data)

# See if there were any errors in Register Device
@socketio.on_error(namespace="/Register_Device")
def register_device_error(e):
    print("An error has occured while registering the device: " + str(e))

#TODO: 
# - Inventory system with QR-Code
# - Customer order system
# - Integrate inventory system with process system so quantites are always known and tracked
# - Financial system integrated with inventory system so that cost of recipe is always known
#   and can be altered according to changing market situation
