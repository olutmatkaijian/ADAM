from adam_v2 import db


## This class shall contain information on sensors and their respective measurements
## Each sensor is attached to one Hardware Node
## Each sensor has a GPIO-Range
## Each sensor has a one-to-n relation with measurements

## Each measurements has:
## Timestamp
## Measurement Value
## A measurement unit (Kelvin, Amps, Volts, PSI per Square Intch [Rethink your life if you use this measurement system]
## Sensor ID relation
## Process ID relation
## This way it should be possible to make nice graphs for processes


class Sensor(db.Model):
    ___bind_key__ = "sensor_data"
    __tablename__ = "sensor"
    id = db.Column(db.Integer(), unique=True, primary_key=True)
    
    ## Add rest here
    
class Measurement(db.Model):
    __bind_key__ = "sensor_data"
    __tablename__ = "measurements"
    id = db.Column(db.Integer(), unique=True, primary_key=True)
    
    ## Add rest here
