import sys
from PyQt5.QtWidgets import *

'''
app = QApplication(sys.argv)
label = QLabel("Hello PyQt")
label.show()
app.exec_()

app = QApplication(sys.argv)
label = QPushButton("Quit")
label.show()
app.exec_()
'''


class Parent:
    house = "yong-san"

    def __init__(self):
        self.money = 10000


class Child1(Parent):
    def __init__(self):
        super().__init__()
        pass


class Child2(Parent):
    def __init__(self):
        pass


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyStock")
        self.setGeometry(300, 300, 400, 400)

        btn1 = QPushButton("Click me", self)
        btn1.move(20, 20)
        btn1.clicked.connect(self.btn1_clicked)

    def btn1_clicked(self):
        QMessageBox.about(self, "message", "clicked")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()
