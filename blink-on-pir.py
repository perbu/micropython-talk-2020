from machine import Pin
from time import sleep
pir = Pin(23, Pin.IN)
led = Pin(2, Pin.OUT)


def handle_interrupt(pin):
    print('Movement detected.')
    led.on()
    sleep(1)
    led.off()

print('Setting up interrupt handler...')
pir.irq(trigger=Pin.IRQ_RISING, handler=handle_interrupt)

while True:
    sleep(1)