# main.py -- put your code here!

from machine import Pin, ADC, I2C
from time import sleep
import dht

# Function to read data from the soil sensor
from lib.seesaw import Seesaw

# Function for the flashing led is imported from the led_flash module and instance with the repeat count argument
from lib.led_flash import led_flash

# Import the buzzer settings, variables and functions. The song variable is stored here and is passed to the playsong(song) function when instanced.
from lib.buzzer import *

# Import the variables and settings for the LCD screen and the custom characters we created
from lib.lcd_screen_logic import *

# Import the Wi-Fi settings so we can connect and disconnect and not waste energy
import lib.wifi_connection as wifi_connection

# Import the MQTT client class
from lib.mqtt import MQTTClient

# import the keys file for use with the MQTT settings 
import lib.keys as keys

# Function to send data to our MQTT broker and visualization platform
import lib.send_sensor_data as send_data

print("Libraries loaded successfully!")

# Setup for humidity and temp sensor DHT11
tempSensor = dht.DHT11(Pin(22))

# Setup for Soil Moisture Sensor (Adafruit Stemma)
i2c_soil = I2C(0, scl=Pin(17), sda=Pin(16))
# i2c_soil = I2C(0, scl=Pin(17, Pin.PULL_UP), sda=Pin(16, Pin.PULL_UP))
ss = Seesaw(i2c_soil)

# Setup for LDR/Photo Resistor
photo_resistor = ADC(Pin(27))
light = photo_resistor.read_u16()
# Light level is calculated as a percentage by subtracting the 16-bit integer reading from ADC from the ceiling value of the 16-bit integer (65535), this value is divided by the ceiling value and then multiplied by 100 to get the light level as a percentage.
light_level = round((65535 - light) / 65535 * 100, 2)

# Main logic for monitoring, will run endlessly until disconnected from power.
while True:
    try:
        # Read humidity and air temp from DHT11
        tempSensor.measure()
        temperature = tempSensor.temperature()
        humidity = tempSensor.humidity()
    
        # Read moisture level from the soil sensor
        moist = round(ss.get_moisture())

        # Read the light level from the photo resistor and display as a percentage
        light = photo_resistor.read_u16()
        light_level = round((65535 - light) / 65535 * 100)


        print(f"Temperature is {temperature} degrees Celsius and Humidity is {humidity}%")
        print(f"Soil Moisture: {moist}%")
        print(f"Light level: {light_level}%")
        
        # Need to switch backlight on here for the loop to display on repeat
        lcd.backlight_on()
        backlight_state = True
        lcd.clear()
        lcd.putstr(f"{chr(0)}: {temperature}{chr(5)}C  {chr(1)}: {humidity}%")
        lcd.move_to(0, 1)
        lcd.putstr(f"{chr(2)}: {moist}%   {chr(3)}: {light_level}%")
        
        try:

            # Connect to Wi-Fi to send data
            wifi_connection.connect()

            # Send the MQTT data to Adafruit IO
            send_data.client.connect()
            send_data.send_sensor_data(temperature, humidity, moist, light_level)
            sleep(5)
            send_data.client.disconnect()

            # Disconnect from Wi-Fi to save energy
            wifi_connection.disconnect()

        except Exception as error:
            print("Could not connect to Wi-Fi and send data...", error)

        
        # Here is our if statement to check the condition we want, in this case if the soil moisture is below 32% or above 58%
        if moist < 32 or moist > 58:
            led_flash(10)
            playsong(song)

        sleep(20)
        lcd.backlight_off()
        backlight_state = False  # Sync the state with the actual state of the backlight
    
    except Exception as error:
        print("Exception occurred", error)
    
    print("Waiting for 1 hour...")
    sleep(3600)
