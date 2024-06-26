import ubinascii              # Conversions between binary data and various encodings
import machine                # To Generate a unique id from processor


WIFI_SSID = "PUT WIFI SSID HERE"
WIFI_PASS = "PUT WIFI PASS HERE"

# Adafruit IO (AIO) configuration
AIO_SERVER = "io.adafruit.com"
AIO_PORT = 1883
AIO_USER = "PUT YOUR USER HERE FOR AIO"
AIO_KEY = "PUT YOUR AIO KEY HERE"
AIO_CLIENT_ID = ubinascii.hexlify(machine.unique_id())  # Can be anything
AIO_TEMP_FEED = "PUT YOUR FEED FOR TEMPERATURE HERE"
AIO_HUMIDITY_FEED = "PUT YOUR FEED FOR HUMIDITY HERE"
AIO_SOIL_FEED = "PUT YOUR FEED FOR SOIL MOISTURE HERE"
AIO_LIGHT_FEED = "PUT YOUR FEED FOR LIGHT LEVEL HERE"