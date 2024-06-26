# Seesaw soil sensor, main code taken from a previous project https://github.com/realfishsam/bnbPlants/tree/main
# Just added logic to convert it to a percentage, sensor range is between 200 and 2000 according to specs https://cdn-learn.adafruit.com/downloads/pdf/adafruit-stemma-soil-sensor-i2c-capacitive-moisture-sensor.pdf
import time

class Seesaw:
    def __init__(self, i2c, addr=0x36):
        self.i2c = i2c
        self.addr = addr
        self.temp = bytearray(4)
        self.moist = bytearray(2)

    def get_temp(self):
        # Send request to get temperature (command 0x04)
        self.i2c.writeto(self.addr, bytes([0x00, 0x04]))
        time.sleep(0.1)  # Delay for conversion
        self.i2c.readfrom_into(self.addr, self.temp)
        return 0.00001525878 * ((self.temp[0] & 0x3F) << 24 | self.temp[1] << 16 | self.temp[2] << 8 | self.temp[3])

    def get_moisture(self):
            # Send request to get moisture (command 0x0F)
            self.i2c.writeto(self.addr, bytes([0x0F, 0x10]))
            time.sleep(0.1)  # Delay for conversion
            self.i2c.readfrom_into(self.addr, self.moist)
            raw_moisture = (self.moist[0] << 8 | self.moist[1])
            # Convert raw moisture value to percentage
            moisture_percentage = ((raw_moisture - 200) / (2000 - 200)) * 100
            return (moisture_percentage)