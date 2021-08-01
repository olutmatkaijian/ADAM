# The recipe class contains information on any given process
# i.e. when to set the temperature, how long to hold it, etc.

from adam_v2 import db


class Control_Process(db.Model):
    __bind_key__ = "devices"
    __tablename__ = "hardware_control"

    id = db.Column(db.Integer, primary_key=True)
    # A name to define the process, e.g. "Brewing" or "Stripping"
    name = db.Column(db.String(256), nullable=False)

    # Each recipe can have multiple pid_controller
    pid_controllers = db.relationship('PID_Controller')

    # The process is online or offline
    status = db.Column(db.Boolean)

    # The process ran before
    last_online = db.Column(db.DateTime)
