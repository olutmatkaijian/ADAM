import os

ADAM_PSK = "dev1234"
GROUPS = [("PE", "Process Editor"),("PS", "Process Status"), ("DBV", "Database Viewer"), ("INV", "Inventory"), ("HWS", "Hardware Setup"), ("SALE", "SALES"), ("DELI", "Deliveries"), ("USRADM", "User Administration")]
LANGUAGE = "en"


class Config(object):
    SQLALCHEMY_DATABASE_URI = "sqlite:///main.db"
    # Seems like a good idea to have them seperate
    SQLALCHEMY_BINDS= {
    "users":"sqlite:///users.db",
    "devices":"sqlite:///devices.db",
    "customers":"sqlite:///customers.db",
    "deliveries":"sqlite:///deliveries.db"}
    SECRET_KEY="dev1234" # CHANGE THIS MUST NOT BE SAME AS ADAM PSK
