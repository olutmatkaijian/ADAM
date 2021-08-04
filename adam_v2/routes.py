from adam_v2 import app, socketio
from flask import render_template


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

# I can't for the love of it figure out how this is supposed to work
@app.route("/register_device")
def register_device():
    return render_template("register_device.html", title="Register Device")




#TODO: 
# - Inventory system with QR-Code
# - Customer order system
# - Integrate inventory system with process system so quantites are always known and tracked
# - Financial system integrated with inventory system so that cost of recipe is always known
#   and can be altered according to changing market situation
