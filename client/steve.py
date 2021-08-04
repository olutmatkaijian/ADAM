# Libraries for GPIO hardware to work
import time
#import RPi.GPIO as GPIO
#import adafruit_ds3231
#import board
#import busio
#from adafruit_ads1x15 import ads1015 as ADS
#from adafruit_ads1x15.analog_in import AnalogIn
from simple_pid import PID
from operator import itemgetter
import os
import sys
# Client behavior:
# 1. Register to the server as configured in config.py

# Libraries for async http stuff
import requests
from config import MAINFRAME_URL, DEVICE_UUID, MAINFRAME_PORT, ADAM_PSK, IS_PRODUCTION
# To connect to the flask server
import socketio
import asyncio
# Device with UUID means that the device is not registered to a server

# Using AsyncIO should allow for the collection of data while also doing other things
if IS_PRODUCTION is False:
    sio = socketio.AsyncClient()
else:
    sio = socketio.AsyncClient(logger=True, engineio_logger=True, ssl_verify=False)
@sio.on('connect', namespace="Register_Device")
async def on_connect():
    print("Connecting ...")

@sio.on('disconnect', namespace='Register_Device')
def on_disconnect():
    print("Disconnected")

@sio.event
async def get_message(data):
    print(data)

@sio.event
async def connect_error(data):
    print("Connection Failed due to: " + data)

async def mainframe_connect(hostname, port, namespaces):
    try: 
        await sio.connect(str(hostname) + ":" + str(port), namespaces=namespaces)
        print("Acquired SID: " + sio.sid)
    except socketio.exceptions.ConnectionError as err:
        print("Error establishing connection to server: %s", err)

async def register_device():
    try:
        await sio.emit("OBTAIN_UUID", {"ADAM_PSK":str(ADAM_PSK)}, namespace="/Register_Device")
    except:
        print("Error @ OBTAIN_UUID")


# In non-production environment, SSL issues do not yet arise

async def main():    
    is_running = True
    is_production = False
    while is_running == True and is_production == False:
        try:
            # Check if connection already exists
            if not sio.connected:
                await mainframe_connect(MAINFRAME_URL, MAINFRAME_PORT, namespaces="/Register_Device")
                    # If the device has a UUID, it starts sending information to ADAM
                    # If it does not, it registers to ADAM using the PSK
            if DEVICE_UUID == 0:
                await register_device()    
        except KeyboardInterrupt:
            print("Interrupted")
            is_running = False
            try: 
                print("Trying system exit...")
                sys.exit(0)
            except SystemExit:
                print("Trying os exit")
                os._exit(0)
        time.sleep(10)


if __name__=="__main__":
    asyncio.run(main())
