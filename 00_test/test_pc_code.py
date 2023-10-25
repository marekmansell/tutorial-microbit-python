import serial

# Pripojenie sa k BBC micro:bit
port = '/dev/ttyACM0'  # treba pozrieť na PC po pripojení micro:bitu, na Linuxoch je vo formáte /dev/ttyACM0 a pod.
microbit_serial = serial.Serial(port, baudrate=115200)

microbit_serial.write("Ahoj".encode())

while True:
    if microbit_serial.in_waiting:
        msg = microbit_serial.read_until()
        print(msg.decode())
        break
