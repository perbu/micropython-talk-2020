from machine import Pin
from time import sleep

led = Pin(2, Pin.OUT)

led.value(0)

while True:
    led.value(not led.value())
    sleep(1)


# pyboard —device /dev/cu.SLAB_USBtoUART hello.py
