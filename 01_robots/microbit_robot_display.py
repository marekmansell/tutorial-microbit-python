from microbit import uart, display, sleep, button_a, Image, temperature
import radio
from utime import ticks_diff, ticks_ms

BROADCAST_INTERVAL_MS = 2000

radio.config(group=42)
radio.on()

display.show("R")

last_send_t = ticks_ms()

while True:

    incoming = radio.receive()
    if incoming == "forward":
        display.show(Image.ARROW_N)
    elif incoming == "left":
        display.show(Image.ARROW_W)
    elif incoming == "right":
        display.show(Image.ARROW_E)
    elif incoming == "back":
        display.show(Image.ARROW_S)
    elif incoming == "stop":
        display.show(Image.NO)
    elif incoming == "func_a":
        display.show("A")
    elif incoming == "func_b":
        display.show("B")
    elif incoming == "func_c":
        display.show("C")

    # Sends the temp every 2 seconds
    if ticks_diff(ticks_ms(), last_send_t) > BROADCAST_INTERVAL_MS:
        radio.send(str(temperature()))
        last_send_t = ticks_ms()

    # A short sleep helps everything run smoothly
    sleep(10)
