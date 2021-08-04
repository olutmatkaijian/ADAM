MAINFRAME_URL = "https://127.0.0.1"
MAINFRAME_PORT= 5000
DEVICE_UUID = 0
DEVICE_NAME = "unregistered"
ADAM_PSK = "dev1234" # Pre-shared key for the device so that ADAM knows it's a verified device
IS_PRODUCTION = 0 # If true, STEVE will require a valid SSL certificate running on the ADAM mainframe and disable all logging. Else, it will enable debug logging and not require valid SSL certificates
