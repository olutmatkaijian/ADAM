# Database models for hardware configuration
import os
import sys
from random import randint
import datetime

from adam_v2 import db
# There is only one main server, which is the server on which the web interface
# is running on. The server can have a total of N PID_Contollers.
# Each PID Controller has N GPIO Pins
# Attatched to each GPIO pin is some soft of GPIO hardware, for example:
# Moisture sensor
# Thermal sensor
# Pump actuator
# And so forth. While Sensors can be one-wire using only one GPIO Pin,
# some hardware requires multiple GPIO Pins

# When a PID_Controller is added to the Server the first time, it acquires
# a unique Identifier
# Hardware is set up by hand in the online interface





# The main PID_Controller only knows it's own name, and which GPIO_Hardware is
# attached to it
class PID_Controller(db.Model):
    __bind_key__ = "devices"
    __tablename__ = "pid_controllers"

    id = db.Column(db.Integer, primary_key = True)

    # Boolean Field that is set when controller is online
    online = db.Column(db.Boolean)

    # Name of PID_Controller (i.e. "Water Pump 1")
    name = db.Column(db.String(128), nullable=False)

    # GPIO hardware of the PID_Controller
    gpio_hw = db.relationship('GPIO_Hardware')

# This class is only for a single GPIO Pin. The GPIO Pin can either be used or
# unused, and it can be online or offline.
class GPIO_Pin(db.Model):
    __bind_key__ = "devices"
    __tablename__ = "gpio_pins"

    id = db.Column(db.Integer, primary_key=True)

    # Identifier of the GPIO pin, e.g. "GPIO Pin #3 on Raspberry Pi"
    pin = db.Column(db.Integer)

    # Set this Boolean if the GPIO Pin is currently in use
    used = db.Column(db.Boolean(False))

    # Assign this Pin to a group of GPIO Pins from a PID_Controller
    gpio_hw_id = db.Column(db.Integer, db.ForeignKey('gpio_hardware.id'))

# This class defines GPIO Hardware, which has a name and an id.
class GPIO_Hardware(db.Model):
    __bind_key__ = "devices"
    __tablename__ = "gpio_hardware"

    id = db.Column(db.Integer, primary_key=True)

    # Name of the hardware group
    name = db.Column(db.String(128), nullable=False)
