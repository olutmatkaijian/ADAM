import os

ADAM_PSK = "dev1234"
GROUPS = [("PE", "Process Editor"),("PS", "Process Status"), ("DBV", "Database Viewer"), ("INV", "Inventory"), ("HWS", "Hardware Setup"), ("SALE", "SALES"), ("DELI", "Deliveries"), ("USRADM", "User Administration")]
LANGUAGE = "en"
# Choices for Node Editor
POSSIBLE_ELEMENTS = ['None', 'input', 'selectfield', 'radio', 'button', 'date', 'file', 'month']


class Config(object):
    SQLALCHEMY_DATABASE_URI = "sqlite:///main.sqldb"
    # Seems like a good idea to have them seperate
    SQLALCHEMY_BINDS= {
    "users":"sqlite:///users.sqldb",
    "process":"sqlite:///process.sqldb"}
    
    
    # For devices, MongoDB is used since no schema constraints allow for 
    # Certain stuff that would be constrained by everything else
    SECRET_KEY="dev1234" # CHANGE THIS MUST NOT BE SAME AS ADAM PSK
    UPLOAD_FOLDER="media/"
    # This is for the allowed extensions in the SVG of the Node Editor
    NE_ALLOWED_EXTENSIONS = {'svg', 'json'}
