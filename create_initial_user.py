from adam_v2 import db
from adam_v2 import users
import os
from config import Config, GROUPS
from werkzeug.security import generate_password_hash
from datetime import datetime

if os.path.isfile('adam_v2/users.db'):
    print (len(users.User.query.all()))
    if len(users.User.query.all()) == 0:
        print("No user found, adding initial user")
        res = [lis[0] for lis in GROUPS]
        initial_user = users.User(username = "administrator", password=generate_password_hash("administrator"), permission_group=str(res), last_pw_change=None, created=datetime.now())
        db.session.add(initial_user)
        db.session.commit()
        print("Initial user 'administrator' added with password 'administrator'")
