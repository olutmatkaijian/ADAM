### Work in Progress!

** This is a work in progress! It is not functional (yet)! **


# Introduction

ADAM is short for "Automated Data Acquisition and Management". This software aims to be a suite for acquiring and managing data (duh) in process control. 
It therefor will have a SCADA-esque interface. Users will be able to define Processes and Recipes. They will also be able to manage Inventory, Sales, Customers and Deliveries. 

In order to interface with real hardware and control processes, another piece of software called STEVE is included. STEVE can control each GPIO pin of a given SoC (like a Raspberry Pi) independently. 
Hopefully, this will allow for great flexibility and customization potential. 

# Structure

ADAM is structured into the ADAM Server and the STEVE client. The ADAM server does all the heavy lifting and servers the front-end (yes the Front-end should be separate from the back-end, no that is not on my list of things to do yet). 

ADAM and STEVE communicate via asyncio. 

# Usage

Enter these commands in the unix terminal:
```
git clone https://github.com/olutmatkaijian/ADAM.git
cd ADAM
chmod +x install_script.sh
./install_script.sh
```
This will generate a virtual environment located in ADAM_VENV, initialize the databases and create an initial user `administrator` with the password `administrator`. After first log in, you are asked to change the password. It must be at least 8 characters and include one upper case letter, on lower case letter and one special character. 
After that you will be logged out automatically and taken back to the login-page. There you can login with username `administrator` and the password you have entered previously.

The install script runs the ADAM Server for exactly 10 minutes. In order to restart it, do the following:
```
source ADAM_VENV/bin/activate
./run.sh
```

The above command will run it indefinitely. In order to stop it, use CTRL+C in the terminal you ran it from. 

If you wish to only run it for a specific time:

```
timeout <time in h/m/s/Y> gunicorn -k gevent -w 1 -b :5000 adam_v2:app --certfile=testing.crt --keyfile=testing.key
```

So to run it for 4 hours: 
```
timeout 4h gunicorn -k gevent -w 1 -b :5000 adam_v2:app --certfile=testing.crt --keyfile=testing.key
``

# Recent Changes
- (Partially) Implemented the GUI for the Process Editor. 
- Added nimiq QrCode Scanner for Inventory system (not attached to anything yet)
- Pepped up the design a bit
- Added install script!

# TODO
- Redo database schema, connect databases
- Sales / Customers / Delivery / Interfaces Dashboards
- Fix UUID Scheme for STEVE

# Credit
- [Flask](https://flask.palletsprojects.com/en/2.0.x/) Glues it all together
- [Drawflow](https://github.com/jerosoler/Drawflow) For the Drag-And-Drop Process Editor interface
- [SchemaCrawler](https://www.schemacrawler.com/) For the Database Viewer (to make development easier)
- [nimiq lightweight qr code readr](https://github.com/nimiq/qr-scanner) for scanning qr code

Probably quite a few others I have forgotten to add. If you're not listed, well, I'm sorry. 