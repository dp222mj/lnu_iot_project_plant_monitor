# Function to send sensor data via MQTT to Adafruit IO 
import keys
from mqtt import MQTTClient


# Use the MQTT protocol to connect to Adafruit IO
client = MQTTClient(keys.AIO_CLIENT_ID, keys.AIO_SERVER, keys.AIO_PORT, keys.AIO_USER, keys.AIO_KEY)
# need to connect to the client to send data but we do this in the main loop so we can ensure it connects each time and disconnects
# client.connect() 

def send_sensor_data(temperature, humidity, moist, light_level):

    print("Publishing: {0} to {1} ... ".format(temperature, keys.AIO_TEMP_FEED))
    print("Publishing: {0} to {1} ... ".format(humidity, keys.AIO_HUMIDITY_FEED))
    print("Publishing: {0} to {1} ... ".format(moist, keys.AIO_SOIL_FEED))
    print("Publishing: {0} to {1} ... ".format(light_level, keys.AIO_LIGHT_FEED))
    try:
        client.publish(topic=keys.AIO_TEMP_FEED, msg=str(temperature))
        client.publish(topic=keys.AIO_HUMIDITY_FEED, msg=str(humidity))
        client.publish(topic=keys.AIO_SOIL_FEED, msg=str(moist))
        client.publish(topic=keys.AIO_LIGHT_FEED, msg=str(light_level))
        print("DONE")
    except Exception as e:
        print("FAILED")
