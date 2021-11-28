from flask import Flask
from config import Config, GROUPS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_socketio import SocketIO
from flask_login import LoginManager
import os
from datetime import datetime
from werkzeug.security import generate_password_hash


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
mirgate = Migrate(app, db)
login_manager = LoginManager()
login_manager.init_app(app)


socketio = SocketIO(app, engineio_logger=True, logger=True, async_mode="threading")

from adam_v2.models import users, PID_Control

# There would be better ways to do this
# TODO: Remove this add new function "Install" when first running ADAM
print (len(users.User.query.all()))
if len(users.User.query.all()) == 0:
    print("No user found, adding initial user")
    res = [lis[0] for lis in GROUPS]
    initial_user = users.User(username = "administrator", password=generate_password_hash("administrator"), permission_group=str(res), last_pw_change=None, created=datetime.now())
    db.session.add(initial_user)
    db.session.commit()
    print("Initial user 'administrator' added with password 'administrator'")

from adam_v2 import routes, socket_io
