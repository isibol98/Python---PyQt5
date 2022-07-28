#!/usr/bin/env python3
from PyQt5 import QtWidgets as widgets
from PyQt5.QtWidgets import QApplication as appli, QMainWindow as mainWin
from PyQt5.QtGui import QIcon
import sys

#calculator by isibol98

class MainForm(mainWin):
    def __init__(self):
        super(MainForm, self).__init__()

        self.setWindowTitle("Calculator by isibol98")
        self.setGeometry(200,200,500,500)
        self.setWindowIcon(QIcon("calculator_icon.png"))
        self.initUI()

    def initUI(self):
        self.lbl_number1 = widgets.QLabel(self)
        self.lbl_number1.setText("Number 1: ")
        self.lbl_number1.move(50,30)

        self.txt_number1 = widgets.QLineEdit(self)
        self.txt_number1.move(150,30)
        self.txt_number1.resize(150,24)

        self.lbl_number2 = widgets.QLabel(self)
        self.lbl_number2.setText("Number 1: ")
        self.lbl_number2.move(50,80)

        self.txt_number2 = widgets.QLineEdit(self)
        self.txt_number2.move(150,80)
        self.txt_number2.resize(150,24)

        self.btn_plus = widgets.QPushButton(self)
        self.btn_plus.setText("+")
        self.btn_plus.move(150,130)
        self.btn_plus.clicked.connect(self.calculate)

        self.btn_minus = widgets.QPushButton(self)
        self.btn_minus.setText("-")
        self.btn_minus.move(150,170)
        self.btn_minus.clicked.connect(self.calculate)

        self.btn_mul = widgets.QPushButton(self)
        self.btn_mul.setText("*")
        self.btn_mul.move(150,210)
        self.btn_mul.clicked.connect(self.calculate)

        self.btn_div = widgets.QPushButton(self)
        self.btn_div.setText("/")
        self.btn_div.move(150,250)
        self.btn_div.clicked.connect(self.calculate)

        self.lbl_res = widgets.QLabel(self)
        self.lbl_res.setText("Result: ")
        self.lbl_res.move(150,290)
        self.lbl_res.resize(150,24)

    def calculate(self):
        sender = self.sender().text()
        try:
            if sender == "+":
                result = int(self.txt_number1.text()) + int(self.txt_number2.text())
            elif sender == "-":
                result = int(self.txt_number1.text()) - int(self.txt_number2.text())
            elif sender == "*":
                result = int(self.txt_number1.text()) * int(self.txt_number2.text())
            elif sender == "/":
                result = int(self.txt_number1.text()) / int(self.txt_number2.text())
        except: #prevent shut down window
            result = "Please enter numbers"
        finally:
            self.lbl_res.setText(f"Result: {result}")


def app():
    app = appli(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    app()