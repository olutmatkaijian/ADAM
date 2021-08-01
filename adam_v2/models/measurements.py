from adam_v2 import db

class Measurement(db.Model):
    __bind_key__ = "devices"
    __tablename__ = "measurements"

    id = db.Column(db.Integer, primary_key=True)

    # Any measurement can be done in float. If a higher precision is needed,
    # change this to the amount of digits needed (e.g. "0.1" is "1", "0.02" is 2)
    value = (db.Column(db.Float(precision=2)))
    # The time on which the measurement was made
    time = db.Column(db.Time, nullable=False)

    # In order to group the measurements to specific GPIO_Hardware
    gpio_hw_id = db.Column(db.Integer, db.ForeignKey("gpio_hardware.id"))

    # Measurement values can be grouped to a process
    control_process = db.relationship('Control_Process')
