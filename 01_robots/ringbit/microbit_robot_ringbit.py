from microbit import uart, display, sleep, button_a, Image, temperature, pin1, pin2, pin0
import radio
from utime import ticks_diff, ticks_ms
import neopixel
from random import randint
from ringbit import RINGBIT

BROADCAST_INTERVAL_MS = 2000

radio.config(group=42)
radio.on()

pin1.set_analog_period(20)
pin2.set_analog_period(20)

last_send_t = ticks_ms()
np = neopixel.NeoPixel(pin0, 8)
ring_bit = RINGBIT(pin1,pin2)


def move_forward():
    ring_bit.set_motors_speed(-100,-100)


def move_left():
    ring_bit.set_motors_speed(-100,100)


def move_right():
    ring_bit.set_motors_speed(100,-100)


def move_back():
    ring_bit.set_motors_speed(100,100)


def stop():
    ring_bit.set_motors_speed(0,0)


def func_a():
    for pixel_id in range(0, len(np)):
        red = randint(0, 60)
        green = randint(0, 60)
        blue = randint(0, 60)

        np[pixel_id] = (red, green, blue)
    np.show()


def func_b():
    for pixel_id in range(0, len(np)):
        np[pixel_id] = (255, 0, 255)
    np.show()


def func_c():
    for pixel_id in range(0, len(np)):
        np[pixel_id] = (0, 0, 0)
    np.show()


# SELF TEST
move_forward()
sleep(500)
stop()
sleep(500)

move_left()
sleep(500)
stop()
sleep(500)

move_right()
sleep(500)
stop()
sleep(500)

move_back()
sleep(500)
stop()


display.scroll("RINGBIT")

while True:

    incoming = radio.receive()
    if incoming == "forward":
        move_forward()
    elif incoming == "left":
        move_left()
    elif incoming == "right":
        move_right()
    elif incoming == "back":
        move_back()
    elif incoming == "stop":
        stop()
    elif incoming == "func_a":
        func_a()
    elif incoming == "func_b":
        func_b()
    elif incoming == "func_c":
        func_c()

    # Sends the temp every 2 seconds
    if ticks_diff(ticks_ms(), last_send_t) > BROADCAST_INTERVAL_MS:
        radio.send(str(temperature()))
        last_send_t = ticks_ms()

    # A short sleep helps everything run smoothly
    sleep(10)
