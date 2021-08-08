from config import ADAM_PSK, MAINFRAME_URL, MAINFRAME_PORT, DEVICE_UUID, DEVICE_NAME, IS_PRODUCTION

import socketio
import asyncio
import sys
import os
import time
from socketio import Namespace
import keyboard
from signal import SIGINT, SIGTERM


# Testing wrong PSK
ADAM_PSK = "Wrong_PSK"
sio = socketio.AsyncClient(logger=True, engineio_logger=True, ssl_verify=False)

@sio.on('connect', namespace='/register_device')
async def on_connect():
    await sio.send(f"\n Client {sio.sid} connected\n", namespace="/register_device")

@sio.on("RECV UUID", namespace='/register_device')
async def recv_ack_msg(msg):
    print(msg)
    
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
            # When the device has recieved a UUID, end the loop
            is_running = 0
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
    
    try:
        await device_registration()
    except:
        print("[ERROR] Problem while registering device, see output above")
        
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
    try:
        loop.run_forever()
    except KeyboardInterrupt as kbi:
        print("TEST")
        loop.close()
