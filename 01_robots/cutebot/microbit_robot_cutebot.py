from microbit import uart, display, sleep, button_a, Image, temperature, pin1, pin2, pin0
import radio
from utime import ticks_diff, ticks_ms
import neopixel
from random import randint
from cutebot import CUTEBOT, left, right

BROADCAST_INTERVAL_MS = 2000

radio.config(group=42)
radio.on()

pin1.set_analog_period(20)
pin2.set_analog_period(20)

last_send_t = ticks_ms()
cb = CUTEBOT()


def move_forward():
    cb.set_motors_speed(100,100)


def move_left():
    cb.set_motors_speed(-100, 100)


def move_right():
    cb.set_motors_speed(100, -100)


def move_back():
    cb.set_motors_speed(-100, -100)


def stop():
    cb.set_motors_speed(0,0)


def func_a():
    cb.set_car_light(left, 255, 0, 0)
    cb.set_car_light(right, 255, 0, 0)


def func_b():
    cb.set_car_light(left, 255, 255, 255)
    cb.set_car_light(right, 255, 255, 255)


def func_c():
    cb.set_car_light(left, 0, 0, 0)
    cb.set_car_light(right, 0, 0, 0)


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


display.scroll("CUTEBOT")

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
