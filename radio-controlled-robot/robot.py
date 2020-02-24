import psutil
from shutil import copyfile
import sys
from PyQt5.QtWidgets import QWidget, QGridLayout, QApplication, QPushButton, QListWidget, QListWidgetItem
import serial


def foo():
    print("bar")


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.serial = None
        self.initUI()

    def connect_to_microbit(self, port, baud=115200):
        try:
            self.serial = serial.Serial(port)
            self.serial.baudrate = baud
            self.setWindowTitle("Robot - connected to {}".format(port))
            return True
        except:
            self.setWindowTitle("Robot - disconnected")
            return False

    def bit_send(self, msg):
        if self.serial:
            self.serial.write(msg.encode())

    def initUI(self):

        grid = QGridLayout()
        grid.setSpacing(10)

        forward_btn = QPushButton("forward")
        left_btn = QPushButton("left")
        right_btn = QPushButton("right")
        backward_btn = QPushButton("backward")
        open_btn = QPushButton("open")
        close_btn = QPushButton("close")

        forward_btn.clicked.connect(lambda: self.bit_send("forward"))
        left_btn.clicked.connect(lambda: self.bit_send("forward"))
        right_btn.clicked.connect(lambda: self.bit_send("forward"))
        backward_btn.clicked.connect(lambda: self.bit_send("forward"))
        open_btn.clicked.connect(lambda: self.bit_send("forward"))
        close_btn.clicked.connect(lambda: self.bit_send("forward"))

        grid.addWidget(forward_btn, 0, 1)
        grid.addWidget(left_btn, 1, 0)
        grid.addWidget(right_btn, 1, 2)
        grid.addWidget(backward_btn, 2, 1)
        grid.addWidget(open_btn, 3, 1)
        grid.addWidget(close_btn, 4, 1)

        tst = QListWidget()
        tst1 = QListWidgetItem("s")
        tst.addItem(tst1)
        grid.addWidget(tst, 5, 1)

        self.setLayout(grid)

        self.setGeometry(300, 300, 800, 500)
        self.setWindowTitle("Robot")

        self.connect_to_microbit("/dev/ttyACM0")

        self.show()


if __name__ == "__main__":

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
