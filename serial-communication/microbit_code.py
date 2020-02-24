# UNTESTED!!! Just a draft which has not been actually tested!
from microbit import uart, display, sleep, button_a

uart.init(baudrate=115200)

while True:
    msg = uart.read()
    if msg:
        display.scroll(msg)
    if button_a.is_pressed():
        uart.write("Button A pressed")
    else:
        sleep(10)