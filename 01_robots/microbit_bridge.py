from microbit import uart, display, sleep, button_a
import radio

uart.init(baudrate=115200)
radio.config(group=42)
radio.on()

display.show("B")


def toggle_led(x, y):
    value = display.get_pixel(x, y)
    if not value:
        display.set_pixel(x, y, 9)  # Turn LED on
    else:
        display.set_pixel(x, y, 0)  # Turn LED off


while True:

    # Forward messages from UART to RADIO
    if uart.any():
        msg = uart.read()
        radio.send(msg)
        toggle_led(4, 4)

    # Forward messages from RADIO to UART
    incoming = radio.receive()
    if incoming is not None:
        uart.write(incoming + "\n")
        toggle_led(4, 0)

    # A short sleep helps everything run smoothly
    sleep(10)
