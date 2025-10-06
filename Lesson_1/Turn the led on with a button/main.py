from machine import Pin

led = Pin(18, Pin.OUT)
button = Pin(13, Pin.IN, Pin.PULL_UP)

led.value(0)

while True:
    if button.value() == 0:  # Button is pressed
        led.value(1)
    else:                    # Button is released
        led.value(0)

