from adam_v2 import db
from werkzeug.security import check_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __bind_key__ = "users"
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, unique = True)

    # Username, it must be unique
    username = db.Column(db.String(32), nullable=False, unique=True)

    # Password
    # TODO: Hash password for security reasons
    password = db.Column(db.String(), nullable=False)

    # Permission groups
    permission_group = db.Column(db.String())
    # Permissions are stored in a list
    # This way the admin can make the user have different types
    # of permission such as Process Control but not Process Editing
    # as well as view of inventory
    # Admin has the permission groups:
    # ["PE", "PS", "DV", "INV", "HWS", "SALE", "DELI" "USERS", "PROF"]
    # If this field is empty, the user will never expire
    # Otherwise, the user cannot log in and will be deleted after
    # a set time
    expire_date = db.Column(db.DateTime())

    last_pw_change = db.Column(db.DateTime()) # Last Password Change, if 
    # None it means the user is still using initial password
    created = db.Column(db.DateTime())
    def __repr__(self):
        return "<User %r>" % self.username
        
    def verify_password(self, password):
        return check_password_hash(self.password, password)
