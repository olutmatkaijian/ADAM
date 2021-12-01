from adam_v2 import app, socketio, login_manager, db
from flask import render_template, request, flash, redirect, url_for
from config import ADAM_PSK, GROUPS
from flask_login import login_user, logout_user, login_required, fresh_login_required
from adam_v2.forms.login_form import LoginForm
from adam_v2.forms.user_administration import AddUserForm
from adam_v2.forms.databaseviewerform import RefreshDataForm
from adam_v2.forms.change_password_form import change_password_form
from adam_v2.models.users import User
from werkzeug.security import generate_password_hash
from flask_login import current_user
from os import urandom
import string
import os
from datetime import datetime

# Create random UUID
from uuid import uuid4


@app.route('/')
def index():
    return render_template("base.html", title="ADAM 0.1", content="Welcome to ADAM")



# Database viewer to see database scheme for debug purposes
@app.route('/database_viewer', methods=["GET","POST"])
@login_required
def database_viewer():
    #Call SchemaCrawler
    if check_permission(current_user, "DBV"):
        refresh_form = RefreshDataForm()
        
        if request.method == "POST" and refresh_form:
            os.system("./schemacrawler/_schemacrawler/schemacrawler.sh --server sqlite --database=adam_v2/main.db --info-level=maximum --command=schema --output-format=png --output-file=adam_v2/static/main.png")
            os.system("./schemacrawler/_schemacrawler/schemacrawler.sh --server sqlite --database=adam_v2/users.db --info-level=maximum --command=schema --output-format=png --output-file=adam_v2/static/users.png")
            os.system("./schemacrawler/_schemacrawler/schemacrawler.sh --server sqlite --database=adam_v2/devices.db --info-level=maximum --command=schema --output-format=png --output-file=adam_v2/static/devices.png")
            os.system("./schemacrawler/_schemacrawler/schemacrawler.sh --server sqlite --database=adam_v2/customers.db --info-level=maximum --command=schema --output-format=png --output-file=adam_v2/static/customers.png")


        return render_template("database_viewer.html", title="DB Viewer", refreshform=refresh_form)

# Inventory system
@app.route('/inventory_system')
@login_required
def inventory():
    if check_permission(current_user, "INV"):
        return render_template("inventory.html", title="Inventory Management")

# About page
@app.route('/about')
def about():
    return render_template("about.html", title="About ADAM")

# Process Editor
# Testing my wonderfully shitty constructor for writing javascript and html
@app.route('/process_editor')
@login_required
def process_editor():
    if check_permission(current_user, "PE"):
        #TODO:
        #Create Process Element Database, MongoDB
        #Put Drawflow node args into Database
        #Take Drawflow node args, put them into list
        #In template, iterate node args
        #And avoid passing unsafe html
        #Great success guaranteed!
        return render_template("process_editor.html", title="Process Editor")

# Process Status
# This is where you can see the ongoing process
@app.route('/index')
@app.route('/process_status')
@login_required
def process_status():
    if check_permission(current_user, "PS"):
        return render_template("process_status.html", title="Process Status")

# Hardware Setup
# This is where you can set up new hardware
@app.route("/hardware_setup")
@login_required
def hardware_setup():
    if check_permission(current_user, "HWS"):
        return render_template("hardware_setup.html", title="Hardware Setup")

# This now works - kind of 
@app.route("/register_device")
def register_device():
    
    return render_template("register_device.html", title="Register Device")

@login_required
@app.route("/user_administration", methods=["GET","POST"])
def user_administration():
    if check_permission(current_user, "USRADM"):
        adduserform = AddUserForm()
        if request.method =="POST":
            print(adduserform.errors)
            if not adduserform.groups.data:
                flash("At least one group must be selected!")
            else:
            # Ensure that the expiry date is set to the future
                if adduserform.expires.data is not None and adduserform.expires.data < datetime.now():
                    flash("Expiry date is in the past")
                elif adduserform.expires.data is None or adduserform.expires.data > datetime.now():
                    checkuser = User.query.filter_by(username=adduserform.username.data).first()
                    if not checkuser:
                        flash("Adding user!")
                        newpw = generate_pw(16)
                        flash(newpw)
                        newuser = User(username = adduserform.username.data, password=generate_password_hash(newpw), expire_date = adduserform.expires.data, permission_group=str(adduserform.groups.data), last_pw_change=None, created=datetime.now())
                        db.session.add(newuser)
                        db.session.commit()
                    else: 
                        flash("User already exists")
    else:
        flash("Insufficient Privileges")
        return redirect(url_for("ADAM_login"))
                
    return render_template("user_administration.html", title="User Administration", adduserform=AddUserForm())

@app.route("/login", methods=["GET", "POST"])
def ADAM_login():
    
    if current_user.is_authenticated:
        flash("Already logged in!")
        return redirect(url_for('index'))
    form = LoginForm()
    
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        
        if user is None or not user.verify_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        flash("Login successful!")
        
        if not user.last_pw_change:
            return redirect(url_for('change_password'))
        return redirect(url_for('index'))
    return render_template('login.html', title="Login", form=form)

@app.route("/change_password", methods=["GET","POST"])
@fresh_login_required
def change_password():
    form = change_password_form()
    # TODO: Make it so new password cannot be like old password
    if form.validate_on_submit() and request.method=="POST" and form.validate():
        print(current_user.password)
        current_user.password = generate_password_hash(form.newpassword.data)
        current_user.last_pw_change = datetime.now()
        db.session.commit()
        flash("Password updated successfully")
        return redirect(url_for("logout"))
    if not form.validate_on_submit():
        for error in form.newpassword.errors:
            flash(error)
    
    return render_template("change_password.html", title="Change Password", form=change_password_form())
@app.route("/sales")
def sales_management():
    if check_permission(current_user, "SALE"):
        return render_template("sales_management.html", title="Sales Management")

@app.route("/deliveries")
def deliveries():
    if check_permission(current_user, "DELI"):
        return render_template("deliveries.html", title="Deliveries")

@app.route("/user_profile")
@login_required
def user_profile():
    permission_list = current_user.permission_group.strip("[]")
    permission_list = list(permission_list.split(", "))
    render_list = list()
    for x in range(len(permission_list)):
        if permission_list[x].strip("'") in GROUPS[x][0]:
            render_list.append(GROUPS[x][1])
    print(render_list)
    return render_template("user_profile.html", title="Profile", rlist=render_list)
    return redirect(url_for("ADAM_login"))
# For sessions!
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route("/inv_qr_scanner")
@login_required
def inventory_qr_scanner():
    return render_template("inventory_qr_scanner.html", title="QrCode Scanner")
    
# To logout
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("ADAM_login"))
    
def generate_pw(length):
    if not isinstance(length, int) or length < 8:
        raise ValueError("Temp password must have positive length!")
        
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ23456789abcdefghijklmnopqrstuvwxyz.!/&-*+"
    pw = "".join(chars[ c % len(chars)] for c in urandom(length))
    print(pw) # Remove after testing!
    return pw

def check_permission(current_user, permission):
    print(type(permission))
    print(permission)
    # Using a tuple here is strange, possibly stupid
    # But it works
    # TODO: Find better way to do this
    if permission in current_user.permission_group:
        return True
#TODO: 
# - Inventory system with QR-Code
# - Customer order system
# - Integrate inventory system with process system so quantites are always known and tracked
# - Financial system integrated with inventory system so that cost of recipe is always known
#   and can be altered according to changing market situation


@login_manager.needs_refresh_handler
def refresh():
    return redirect(url_for("ADAM_login"))

@login_manager.unauthorized_handler
def unauthorized():
    flash("Authorization failed")
    return redirect(url_for("ADAM_login"))
