# Libraries for GPIO hardware to work
import time
import RPi.GPIO as GPIO
import adafruit_ds3231
import board
import busio
from adafruit_ads1x15 import ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
from simple_pid import PID
from operater import itemgetter


# Client behavior:
# 1. Register to the server as configured in config.py

# Libraries for async http stuff
import aiohttp
import asyncio
from config import MAINFRAME_URL, DEVICE_UUID


# Device with UUID means that the device is not registered to a server

if DEVICE_UUID == 0:
    try:
        r = requests.get(MAINFRAME_URL+"/register_device")
        r_json = r.json()
        DEVICE_UUID = r_json['UUID']

        #TODO: Write UUID to config 
    except:
        return "Could not register device"

# The device has a UUID and should therefor be registered to a server
else if DEVICE_UUID != 0:
    try:
        # Send the server a payload telling it is online
        payload = {'UUID':str(DEVICE_UUID), 'online':'1'}
        r = requests.post(MAINFRAME_URL+'/device_listener')
    except:
        return "Connection to server failed, is it online?"

    # Now a connection can be established to the server
    
