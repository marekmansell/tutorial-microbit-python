from microbit import uart, display, sleep, button_a, Image, temperature, pin16, pin0, pin12, pin8
import radio
from utime import ticks_diff, ticks_ms

BROADCAST_INTERVAL_MS = 2000

radio.config(group=42)
radio.on()

last_send_t = ticks_ms()


def move_forward():
    pin12.write_digital(1)
    pin8.write_digital(0)
    pin16.write_digital(0)
    pin0.write_digital(0)


def move_left():
    pin12.write_digital(1)
    pin8.write_digital(0)
    pin16.write_digital(0)
    pin0.write_digital(1)


def move_right():
    pin12.write_digital(1)
    pin8.write_digital(0)
    pin16.write_digital(1)
    pin0.write_digital(0)


def move_back():
    pin12.write_digital(0)
    pin8.write_digital(1)
    pin16.write_digital(0)
    pin0.write_digital(0)


def stop():
    pin12.write_digital(0)
    pin8.write_digital(0)
    pin16.write_digital(0)
    pin0.write_digital(0)


def func_a():
    display.scroll("A")


def func_b():
    display.scroll("B")


def func_c():
    display.scroll("C")


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


display.scroll("HUMMER")

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
