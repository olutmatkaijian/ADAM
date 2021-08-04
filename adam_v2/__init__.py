from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_socketio import SocketIO

#from celery import Celery


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
socketio = SocketIO(app, logger=True, engineio_logger=True)


from adam_v2.models import measurements, PID_Control, recipes, users
from adam_v2 import routes

