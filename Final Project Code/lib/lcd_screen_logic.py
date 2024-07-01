
from machine import Pin, I2C
from pico_i2c_lcd import I2cLcd
from time import sleep_ms


# Setup for LCD Screen
I2C_ADDR = 0x27  # Decimal 39
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16
sda_lcd = Pin(2)
scl_lcd = Pin(3)
i2c_screen = I2C(1, sda=sda_lcd, scl=scl_lcd, freq=400000)
lcd = I2cLcd(i2c_screen, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)


# Here is the setup and logic to make the button toggle the LCD backlight 
    # Initial state of the backlight
backlight_state = True

    # Setup for the button input to turn the backlight on/off
push_button = Pin(18, Pin.IN, Pin.PULL_UP)

    # Debounce delay (in milliseconds) - commented out as I suspect using sleep_ms during a long sleep causes the code to break.
# debounce_delay = 200

    # Function to toggle LCD backlight
def toggle_backlight(pin):
    global backlight_state
    if pin.value() == 0:
        backlight_state = not backlight_state
        if backlight_state:
            lcd.backlight_on()
        else:
            lcd.backlight_off()
    # sleep_ms(debounce_delay)

    # Attach interrupt to the push button pin to toggle backlight
push_button.irq(trigger=Pin.IRQ_FALLING, handler=toggle_backlight)


# Create custom characters for LCD Screen, use https://maxpromer.github.io/LCD-Character-Creator/
thermometer = bytearray([0x04, 0x0A, 0x0A, 0x0A, 0x0A, 0x1B, 0x1F, 0x0E])
lcd.custom_char(0, thermometer)
waterdrop = bytearray([0x04, 0x04, 0x0E, 0x0E, 0x1F, 0x1F, 0x1F, 0x0E])
lcd.custom_char(1, waterdrop)
plant = bytearray([0x0E, 0x1B, 0x15, 0x1B, 0x0E, 0x04, 0x15, 0x0E])
lcd.custom_char(2, plant)
lightbulb = bytearray([0x0E, 0x11, 0x1F, 0x15, 0x11, 0x0E, 0x0E, 0x04])
lcd.custom_char(3, lightbulb)
sun = bytearray([0x04, 0x15, 0x0E, 0x1F, 0x1F, 0x0E, 0x15, 0x04])
lcd.custom_char(4, sun)
degree_symbol = bytearray([0x0E, 0x0A, 0x0E, 0x00, 0x00, 0x00, 0x00, 0x00])
lcd.custom_char(5, degree_symbol)
