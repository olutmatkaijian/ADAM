### Work in Progress!



![current_progress](documents/ADAM_UI_CHEATSHEET.png)
**Current progress picture**
**This is a work in progress! It is not functional (yet)!**

# Recent Changes
- Now with CheatSheet in the Process Editor that Shows/Hides Cheat Sheet
on click
- In Process Editor, Grid Snapping now works (1px resolution), making it easier to make orderly graphs
- Added a ProcessNode element for the SQL Database. While intentionally MongoDB was aimed for it would have been more work to implement, and witha few tricks, SQL will do fine.
- New database model for GPIO-Enabled hardware, to seperate logic nodes ("Process Nodes") from hardware nodes. 

# Most important 
- Create setup page for GPIO Hardware
- Create a sensor database model
- Create measurements data base model
- somehow relate them all into a living organism

# Currently working on
- Loading the elements from the Process Element Database into the Editor
- Multiple HTML Elements for Nodes instead of just one
- Dynamic loading from PED -> PE
- Better route drawing from inputs to outputs (define the route by clicking instead of pulling)

# Future work
- Rewrite STEVE client

# Far future work
- Attempt to implement something like river or creme.py to continously improve PID parameters. Why? Why not!

# Roadmap
A roadmap for the development of the suite.

### Release 0.1
In Version 0.01 it should be possible to: 
- Create and save a SCADA type view of a process
- Create and save a process recipe for process automation 
- Connect hardware that runs the STEVE client to ADAM
- Add additional process nodes
The version 0.01 shall contain the necessary basics needed to design, view and control a process using multiple hardware devices. 

### Release 0.2
- Inventory by QrCode should be possible
- Integration of Inventory and Process

### Release 0.3:
- Sales system is integrated with inventory system

### Release 0.4:
- Delivery system is integrated with inventory system, using OSM to display markers of delivery locations, allowing for easy route planning - no I will not, ever, never, integrate Google Maps into this. As a matter of fact I am annoyed that some of the components (either Drawflow or QrCode reader) use Google products, and I will attempt to stip them out without breaking their funcionality.

### Release 0.5:
- Refactoring of the code, optimizations

### Releases 0.6-0.9
- Implemenet features asked for by users, remove bugs, make sure the software is stable

### Release 1.0
- Final release. The software works as intended and is safe to use. 


# Introduction

ADAM is short for "Automated Data Acquisition and Management". This software aims to be a suite for acempquiring and managing data (duh) in process control. 
It therefor will have a SCADA-esque interface. Users will be able to define Processes and Recipes. They will also be able to manage Inventory, Sales, Customers and Deliveries. 

In order to interface with real hardware and control processes, another piece of software called STEVE is included. STEVE can control each GPIO pin of a given SoC (like a Raspberry Pi) independently. 
Hopefully, this will allow for great flexibility and customization potential. 

# Structure

ADAM is structured into the ADAM Server and the STEVE client. The ADAM server does all the heavy lifting and servers the front-end (yes the Front-end should be separate from the back-end, no that is not on my list of things to do yet). 

ADAM and STEVE communicate via socketio (my bad, I have mistaken the names of asyncio and socketio, although asyncio may be part of ADAM for several tasks). 

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
```


**NOTE ABOUT DATABASE VIEWER**: To use the Database Viewer, you must have [schemacrawler](https://www.schemacrawler.com/) installed in ADAM/schemacrawler directory.

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
- [Red October](https://www.neogrey.com/portfolio/red-october/) font for the top navigation bar 

Probably quite a few others I have forgotten to add. If you're not listed, well, I'm sorry. 
