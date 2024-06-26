#logic for making rgb led flash with varying colours, the repeat count is passed as an argument

from machine import Pin
import time

LED_Pin_Red = Pin(19, Pin.OUT)
LED_Pin_Green = Pin(20, Pin.OUT)
LED_Pin_Blue = Pin(21, Pin.OUT)

def led_flash(repeat_count):
    for i in range(repeat_count):

        LED_Pin_Red.value(1)
        LED_Pin_Green.value(0)
        LED_Pin_Blue.value(0)
        time.sleep(0.2)
        
        LED_Pin_Red.value(0)
        LED_Pin_Green.value(1)
        LED_Pin_Blue.value(0)
        time.sleep(0.2)
        
        LED_Pin_Red.value(0)
        LED_Pin_Green.value(0)
        LED_Pin_Blue.value(1)
        time.sleep(0.2)
        
        LED_Pin_Red.value(1)
        LED_Pin_Green.value(0)
        LED_Pin_Blue.value(1)
        time.sleep(0.2)
        
        LED_Pin_Red.value(1)
        LED_Pin_Green.value(1)
        LED_Pin_Blue.value(0)
        time.sleep(0.2)
        
        LED_Pin_Red.value(0)
        LED_Pin_Green.value(1)
        LED_Pin_Blue.value(1)
        time.sleep(0.2)
        
        LED_Pin_Red.value(1)
        LED_Pin_Green.value(1)
        LED_Pin_Blue.value(1)
        time.sleep(0.2)

    
    LED_Pin_Red.value(0)
    LED_Pin_Green.value(0)
    LED_Pin_Blue.value(0)