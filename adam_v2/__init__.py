from flask import Flask
from config import Config, GROUPS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_socketio import SocketIO
from flask_login import LoginManager
import os
from datetime import datetime
from werkzeug.security import generate_password_hash
from flask_jsglue import JSGlue

app = Flask(__name__)
#jsglue is necessary for process editor front end

app.config.from_object(Config)
# SQL for user management and other non-flexible stuff
db = SQLAlchemy(app)
# MongoDB for flexible stuff like device setup
migrate = Migrate(app, db)

login_manager = LoginManager()
login_manager.init_app(app)

jsglue = JSGlue()
jsglue.init_app(app)
migrate.init_app(app, db)
"""! Initialize SocketIO 

SocketIO is used to recieve data from the SoC hardware running STEVE 
"""
socketio = SocketIO(app, engineio_logger=True, logger=True, async_mode="threading")

from adam_v2.models import users, PID_Control, process_editor_nodes

# There would be better ways to do this
# TODO: Remove this add new function "Install" when first running ADAM
# Check if database exists -> else error when trying to migrate
from adam_v2 import routes, socket_io
