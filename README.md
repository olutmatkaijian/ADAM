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


# Recent Changes
- (Partially) Implemented the GUI for the Process Editor. 
- Added nimiq QrCode Scanner for Inventory system (not attached to anything yet)
- Pepped up the design a bit

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