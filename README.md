# Introduction

ADAM is short for Automated Data Acquisition and Management. It aims to be a SCADA (Supervisory Control and Data Acquisition) type system for Single-Board Computers like the Raspberry Pi Zero W. 

# Architecture Considerations

First of all, I am not a programmer by any means, but a chemical engineer. So the software architecture may seem strange to an IT-Professional.

Currently the stack is as follows: SQL to save measurement and hardware data, Python to glue it all together, HTML + CSS for the interface.
I'm currently searching for an open source, lightweight JavaScript library that allows for a SCADA type HMI

So far, this is how the software is supposed to work:
1. STEVE client is configured and placed onto the controlling SBC. I have no idea how to do GPIO-Pin autodetection, so for now they have to be defined by hand.
The client is also told which address on the network is the main server. 
2. STEVE client initiats contact with ADAM. When a connection is established, the client gets a unique ID.
3. STEVE client sends the GPIO-Hardware as was configured in the original file.
4. Now STEVE client is ready to use.

The idea here is that one writes the configuration of any said client once, so that the client hardware can be replaced quickly if necessary.

Next, the actual magic:
1. The user creates a "recipe" in ADAM UI. For starters it will consist of simple "Set Temp to X at time Y" style instructions using JSON.
2. ADAM sends that recipe to STEVE, who then saves it.
3. When the process is activated, STEVE goes through every step while streaming the measurement data to ADAM. However, this is only for visual purposes. STEVE also logs the data locally.
4. The user can in real time see and control the process using ADAM UI if necessary.
5. The process is completed, STEVE sends all measurement data and ADAM verifies it against the previously streamed data, any errors are corrected
6. The run of this process is saved in a database for historical purposes

See the attached image for a better understanding of the layout.
[ADAM](https://user-images.githubusercontent.com/88145590/127775378-02bc50f0-fb87-4955-806c-c29674ea0b4e.jpg)

# Future Features?
- The ability to control STEVE clients directly by attaching a screen and a keyboard to the SBC. This might come in handy in unreliable network situations.
- PID-Autotune for STEVE using machine learning (maybe)

# Why?

Why not? I began development on this years ago, but had to pause it due to personal reasons. However, I think such a system would be a blessing for anybody who wants cheap, affordable and reliable process control.

# Why the weird acronyms?

No specific reason other than that I can and I'm a joker :)

# Software used

So far only Flask, HTML, CSS, Simple-PID and some libraries are used. Currently searching for a sleek open source javascript library that would allow me to create beautiful dashboard, and also searching for a SCADA-type javascript library as all available ones cost an arm and a leg.

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
