# Introduction

ADAM is short for Automated Data Acquisition and Management. It aims to be a SCADA (Supervisory Control and Data Acquisition) type system for Single-Board Computers like the Raspberry Pi Zero W. 

# Motivation

Secure, open source, configureable process control systems are hard to come by these days. 

# Software architecture

This suite is based off two elements: The ADAM mainframe and the STEVE client. Using Flask-SocketIO and Python-SocketIO in asynchronous configuration, it allows to send data back and forth. 
A preshared key is set in the ADAM config and the corresponding STEVE device config. Using SSL (in the hopes to avoid MITM attacks), the PSK is sent from STEVE to ADAM in order to verify that the device may connect to the network.

On the ADAM end a SQLite database keeps meticolous records of measurements of processes. However, these are also logged onto the steve client.

TODO:
- Shutdown AsyncIO connection correctly
- Finish UUID scheme for STEVE device
- Check if CORS works if STEVE runs on an external device
- Add granular user management
- Add UI for SCADA type controls

# Test Setup
My test setup is a modified jam preserver connected to a Raspberry Pi Zero W, using the ADS1115 and ZS-042 Realtime Clock, connected via GX16-8 plug. 
This allows me to drive the heating element using solid-state relays. I do not recommend this setup, as it requires in-depth knowledge of high voltage electricity precautions.

# Development Setup
I use virtual environments in order to develop for ADAM:
`python3 -m venv ADAM_VENV`
`python3 -m venv STEVE_VENV`

Using two different terminals for each software:
`source ADAM_VENV/source/bin/activate`
`source STEVE_VENT/source/bin/activate`

Installing the required software in ADAM_VENV:
`pip install --upgrade pip wheel`
`pip install -r requirements.txt`

Please consider that this software is an active development and the requirements may therefor be outdated or subject to change. This applies to both the ADAM mainframe and the STEVE server.

Gevent, Gevent-Websocket and Gunicorn should already exist in the virtual environment after requirments are installed.
To start the ADAM mainframe:
`gunicorn -k gevent -w 1 -b :5000 adam_v2:app --certfile=testcert.crt --keyfile=testcert.key`

Installing the required software in STEVE_VENV:
`pip install --upgrade pip wheel`
`pip install -r requirements.txt`

Running the STEVE client:
`python3 steve.py`

Please note that KeyboardInterrupt in STEVE client is buggy and it does not behave always as expected. I recommend using htop (F3->steve.py->F9->F9->Enter) in order to terminate STEVE client when necessary.

# Boring License stuff
So far I have chosen no license, and therefor the IP rights remain by me. Do ask if you're interested in using or developing this system.
