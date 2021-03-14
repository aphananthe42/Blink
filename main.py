from machine import Pin
from time    import sleep

led_onboard = Pin(25, Pin.OUT)

while True:
    for s in range(3):
        led_onboard.on()
        sleep(0.2)
        led_onboard.off()
        sleep(0.1)
    led_onboard.off()
    sleep(0.5)

    for o in range(3):
        led_onboard.on()
        sleep(1)
        led_onboard.off()
        sleep(0.1)
    led_onboard.off()
    sleep(0.5)

    for s in range(3):
        led_onboard.on()
        sleep(0.2)
        led_onboard.off()
        sleep(0.1)

    led_onboard.off()
    sleep(300.0)
    