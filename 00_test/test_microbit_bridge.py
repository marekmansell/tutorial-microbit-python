from microbit import uart, display, sleep, button_a
import radio

uart.init(baudrate=115200)

display.show("B")

while True:

    if uart.any():
        msg = uart.read()
        uart.write(msg + " Svet!\n")
        display.scroll(msg)

    # A short sleep helps everything run smoothly
    sleep(10)
