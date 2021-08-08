import socketio
import asyncio
import sys
import os
import time
from socketio import Namespace
import keyboard
from signal import SIGINT, SIGTERM
import configparser



# Config object so the config can be updated on the fly
config_obj = configparser.ConfigParser()

# Read the config file
try:
    config_obj.read('config.ini')
except:
    print("[ERROR] : Could not read config.ini")


# Set the config variable

try:
    ADAM_PSK = config_obj.get('GENERAL', 'ADAM_PSK')
    MAINFRAME_URL = config_obj.get('GENERAL', 'MAINFRAME_URL')
    MAINFRAME_PORT = config_obj.get('GENERAL', 'MAINFRAME_PORT')
    DEVICE_UUID = config_obj.get('GENERAL', 'DEVICE_UUID')
    DEVICE_NAME = config_obj.get('GENERAL', 'DEVICE_NAME')
    IS_PRODUCTION = config_obj.get('GENERAL', 'IS_PRODUCTION')

    print("[STATUS] : Loaded configuration file \n" + 
        "ADAM SERVER URL : " + str(MAINFRAME_URL) + "\n" +
        "ADAM SERVER PORT: " + str(MAINFRAME_PORT) + "\n" +
        "DEVICE UUID     : " + str(DEVICE_UUID) + "\n" +
        "DEVICE NAME     : " + str(DEVICE_NAME) + "\n" +
        "IS PRODUCTION   : " + str(IS_PRODUCTION) + "\n")
except:
    print("[ERROR] : Could not load configuration file parameters")
    sys.exit(1)

# Testing wrong PSK
# ADAM_PSK = "Wrong_PSK"
if IS_PRODUCTION != 0:
    print("[WARNING] : This client does not verify SSL")
    sio = socketio.AsyncClient(logger=True, engineio_logger=True, ssl_verify=False)
elif IS_PRODUCTION == 0:
    print("[STATUS] : This client verifies SSL, starting ...")
    sio = socketio.AsyncClient(logger=True, engineio_logger=True, ssl_verify=True)
else:
    print("[STATUS] : Something is wrong with the SSL_VERIFY config")
    sys.exit(1)

@sio.on('connect', namespace='/register_device')
async def on_connect():
    await sio.send(f"\n Client {sio.sid} connected\n", namespace="/register_device")

@sio.on("RECV UUID", namespace='/register_device')
async def recv_ack_msg(msg):
    print(msg)

# Somehow this feels like GOTO spaghetti code
@sio.on('UUID_REGISTER_SUCCESS', namespace='/register_device')
async def ack_uuid_recv(msg):
    print("[STATUS] : UUID Obtained: " + msg)
    try:
        config_obj['GENERAL']['DEVICE_UUID'] = msg
        with open('config.ini', 'w') as config_file:
            config_obj.write(config_file)
        print("[STATUS] : UUID successfully written to configuration file")
    except:
        print("[STATUS] : Error while writing UUID to configuration file")
    
# Function keeps the client alive even if there is nothing to be done
# Strangely, this works ...
async def keep_alive():
    keep_alive.is_running = True
    while keep_alive.is_running == True:
        try:
            await asyncio.sleep(0.025)
        except KeyboardInterrupt as kbi:
            keep_alive.is_running = False
    
    return "Keep_Alive loop stopped"
# This function is called when DEVICE_UUID is 0

async def device_registration():
    try:
        sio.register_namespace(RegistrationNamespace('/register_device'))
    except:
        print("[ERROR] : Could not register namespace /register_device")
    
    if not sio.connected:
        try:
            print("Connecting to: "+str(MAINFRAME_URL+":"+str(MAINFRAME_PORT)))
            await sio.connect(MAINFRAME_URL+":"+str(MAINFRAME_PORT), namespaces=['/register_device'])
        except socketio.exceptions.ConnectionError as err:
            print("[ERROR] : " + str(err))
        
        # Send the PSK to ADAM, which will check if the PSK is correct
        try: 
            await sio.emit('register_device_uuid', {"PSK":str(ADAM_PSK)}, namespace='/register_device')
            # From here on, the above defined "UUID_REGISTER_SUCCESS" event takes over           
        except:
            print("[ERROR] : Emission of register_device_uuid failed!")
	
	# After the UUID has been acquired, disconnect from the namespace
    try:
        await sio.emit('disconnect', namespace='/register_device')
        print("[STATUS] : Disconnected from namespace \'register_device\'")
    except:
        print("[ERROR] : Error while disconnecting from namespace \'register_device\'")
    return 0



async def main():


    # When the DEVICE_UUID is zero, the device attempts to acquire a UUID using
    # the PSK specified in the config.ini file
    print("[STATUS] : Checking device UUID")

    # ... This only works because appearantly configparser parses DEVICE_UUID as a string instead
    # of a number, meaning that the client must pretend it's a string as well
    # I do not see where this could ever go wrong ... /sarcasm
    
    if DEVICE_UUID == str(0):
        print("[STATUS] : Attempting device registration because DEVICE_UUID="+DEVICE_UUID)
        try:
            await device_registration()
        except:
            print("[ERROR] Problem while registering device, see output above")
    else:
        print("DEVICE_UUID is not 0")
    # This is the only way I got it to work so keyboard interrupts
    # are possible
    try:
        await keep_alive()
    except KeyboardInterrupt as kbi:
        print("[STATUS] Shutting down now")
        sio.disconnect()
        
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    main_task = asyncio.ensure_future(main())
    # This is necessary, do not remove
    # For some reason it does not exit gracefully anymore
    # TODO: Make it so that when it exits, it awaits future tasks
    try:
        loop.run_forever()
    except KeyboardInterrupt as kbi:
        loop.close()
