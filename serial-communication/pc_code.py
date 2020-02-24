# UNTESTED!!! Just a draft which has not been actually tested!
import serial


port = 'COM11' # treba pozrieť na PC po pripojení micro:bitu, na Linuxoch je voformáte /dev/ttyACM0 a pod.
microbit_serial = serial.Serial(port, baudrate=115200)


def send_to_microbit(serial, msg):
	serial.write(msg.encode())

def read_from_microbit(serial):
	msg = serial.read()
	return msg.decode()

send_to_microbit(microbit_serial, "Hello World!")
print(read_from_microbit(microbit_serial))