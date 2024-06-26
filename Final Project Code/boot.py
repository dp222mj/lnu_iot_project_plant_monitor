# boot.py -- run on boot-up
import lib.wifi_connection as wifi_connection

# WiFi Connection
try:
    ip = wifi_connection.connect()
except KeyboardInterrupt:
    print("Keyboard interrupt")
