from adam_v2 import db

class User(db.Model):
    __bind_key__ = "users"
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    # Username
    username = db.Column(db.String(32), nullable=False)

    # Password
    # TODO: Hash password for security reasons
    password = db.Column(db.String(64), nullable=False)

    # Permissions
    permission_group = db.Column(db.Integer)
