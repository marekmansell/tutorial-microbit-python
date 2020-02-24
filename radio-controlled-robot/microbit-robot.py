from microbit import uart
import radio

uart.init(baudrate=115200)
radio.on()

while True:
    msg = uart.read()
    if msg:
        # if msg is in format "!#SET-x-y"
        # set radio.config(x=y)
        if msg.startswith("!#SET-"):
            radio.config({msg.split('-')[1]: msg.split('-')[2]})
        # if not !#SET message, send message via radio
        else:
            radio.send(str(msg, 'UTF-8'))
