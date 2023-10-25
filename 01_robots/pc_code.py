import tkinter
import serial

# Vytvorenie Tkinter okna
root = tkinter.Tk()
root.geometry('800x800')
root.title('BBC micro:bit Robot')

# Pripojenie sa k BBC micro:bit
port = '/dev/ttyACM0'  # treba pozrieť na PC po pripojení micro:bitu, na Linuxoch je vo formáte /dev/ttyACM0 a pod.
microbit_serial = serial.Serial(port, baudrate=115200)


def send_to_microbit(msg):
    microbit_serial.write(msg.encode())
    print(f"Sending: {msg}")


def read_from_microbit():
    msg = None

    if microbit_serial.in_waiting:
        msg = microbit_serial.read_until().decode()
        formatted_msg = f"Teplota: {msg}"
        info.config(text=formatted_msg)
        print(f"Receiving: {msg}")

    root.after(1000, read_from_microbit)


info = tkinter.Label(root, text="Žiadne meranie teploty.")

btn_forward = tkinter.Button(root, text="Vpred")
btn_forward.bind("<ButtonPress>", lambda event: send_to_microbit("forward"))
btn_forward.bind("<ButtonRelease>", lambda event: send_to_microbit("stop"))

btn_left = tkinter.Button(root, text="Vľavo")
btn_left.bind("<ButtonPress>", lambda event: send_to_microbit("left"))
btn_left.bind("<ButtonRelease>", lambda event: send_to_microbit("stop"))

btn_right = tkinter.Button(root, text="Vpravo")
btn_right.bind("<ButtonPress>", lambda event: send_to_microbit("right"))
btn_right.bind("<ButtonRelease>", lambda event: send_to_microbit("stop"))

btn_back = tkinter.Button(root, text="Vzad")
btn_back.bind("<ButtonPress>", lambda event: send_to_microbit("back"))
btn_back.bind("<ButtonRelease>", lambda event: send_to_microbit("stop"))

btn_func_a = tkinter.Button(root, text="Funkcia A", command=lambda: send_to_microbit("func_a"))
btn_func_b = tkinter.Button(root, text="Funkcia B", command=lambda: send_to_microbit("func_b"))
btn_func_c = tkinter.Button(root, text="Funkcia C", command=lambda: send_to_microbit("func_c"))

btn_forward.grid(row=0, column=1)
btn_left.grid(row=1, column=0)
btn_right.grid(row=1, column=2)
btn_back.grid(row=2, column=1)

btn_func_a.grid(row=4, column=0)
btn_func_b.grid(row=4, column=1)
btn_func_c.grid(row=4, column=2)

info.grid(row=3, column=0, columnspan=3)

root.after(1000, read_from_microbit)

root.mainloop()
