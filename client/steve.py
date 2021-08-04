from config import ADAM_PSK, MAINFRAME_URL, MAINFRAME_PORT, DEVICE_UUID, DEVICE_NAME, IS_PRODUCTION

import socketio
import asyncio
import sys
import os
import time
from socketio import Namespace



# Testing wrong PSK
ADAM_PSK = "Wrong_PSK"
sio = socketio.AsyncClient(logger=True, engineio_logger=True, ssl_verify=False)

@sio.on('connect', namespace='/register_device')
async def on_connect():
    await sio.send(f"\n Client {sio.sid} connected\n", namespace="/register_device")

@sio.on("RECV UUID", namespace='/register_device')
async def recv_ack_msg(msg):
    print(msg)



async def main():
    # Initialize the client
    is_running = True

    try:
        sio.register_namespace(RegistrationNamespace('/register_device'))
    except:
        print("ERROR: Could not register namespace /register_device")
    while is_running is True: 
        try:
            if not sio.connected:
                try: 
                    print("Connecting to: "+str(MAINFRAME_URL+":"+str(MAINFRAME_PORT)))
                    await sio.connect(MAINFRAME_URL+":"+str(MAINFRAME_PORT), namespaces=['/register_device'])
                except socketio.exceptions.ConnectionError as err:
                    print("ERROR: " + str(err))

                # Tester function
            try:
                await sio.emit('register_device_uuid', {"PSK":str(ADAM_PSK)}, namespace='/register_device')
            except:
                    print("TEST FALIED")
            
            is_running = False
            await sio.wait()
            await sio.disconnect()
            
        except KeyboardInterrupt:
            sys.exit(0)

if __name__=="__main__":
    asyncio.run(main())
