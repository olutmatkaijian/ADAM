from adam_v2 import db



# This class contains process nodes
# Initially I wanted to save process nodes in MongoDB
# But setting that up was annoying and required extra software
# Instead, I'll just save JSON-Objects into the database
# And save images in a directory

class ProcessNode(db.Model):
    __bind_key__ = "process"
    __tablename__ = "ProcessNodes"
    id = db.Column(db.Integer(), unique=True, primary_key=True)
    dfn_name = db.Column(db.String(), unique=True)
    dfn_class = db.Column(db.String())
    dfn_inputs = db.Column(db.Integer())
    dfn_outputs = db.Column(db.Integer())
    # Since we can have multiple HTML elements on one node
    # We will simple store them as a nested JSON Object
    dfn_html_element = db.Column(db.String())
    dfn_data = db.Column(db.String())
    dfn_svg_element = db.Column(db.String())
    # Might be useful later
    dfn_additional_info = db.Column(db.String())
    
    # Process Node Command, for example command "Sleep 5" or "Heat 65"
    # Must be implemented to STEVE as well
    pn_command = db.Column(db.String())
    
    def __repr__(self):
        return "<Process Node %r>" % self.dfn_class


class HardwareNode(db.Model):
    __bind_key__ = "process"
    __tablename__ = "hardware"
    
    id = db.Column(db.Integer(), unique=True, primary_key=True)
    hw_name = db.Column(db.String(), unique=True) 
    hw_class = db.Column(db.String())
    
    dfn_inputs = db.Column(db.Integer())
    dfn_outputs = db.Column(db.Integer())
    # Where to start and stop counting GPIO pins
    hw_gpio_start = db.Column(db.Integer())
    hw_gpio_stop = db.Column(db.Integer())
    
    # A note that can be left for the hardware
    hw_add_info = db.Column(db.String())
    
    # To save the element
    hw_svg_element = db.Column(db.String())
    
    # A unique UUID, to make sure we always talk to right hardware
    # This is intentionally left blanck until registration, at which point
    # a UUID is generated and sent to the client
    hw_uuid = db.Column(db.String(), unique=True)
