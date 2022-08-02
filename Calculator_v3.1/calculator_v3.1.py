#!/usr/bin/env python3
from PyQt5 import QtWidgets as widgets
from PyQt5.QtWidgets import QApplication as appli, QMainWindow as mainWin, QMessageBox as msgBox
from PyQt5.QtGui import QIcon
import sys
from calculator_ui import Ui_MainWindow as MainWin

#calculator by isibol98

class CalculatorApp(widgets.QMainWindow):
    def __init__(self):
        super(CalculatorApp,self).__init__()
        self.ui = MainWin()
        self.msg = msgBox()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon("calculator_icon.png"))
        self.ui.btn_0.clicked.connect(self.calculate)
        self.ui.btn_1.clicked.connect(self.calculate)
        self.ui.btn_2.clicked.connect(self.calculate)
        self.ui.btn_3.clicked.connect(self.calculate)
        self.ui.btn_4.clicked.connect(self.calculate)
        self.ui.btn_5.clicked.connect(self.calculate)
        self.ui.btn_6.clicked.connect(self.calculate)
        self.ui.btn_7.clicked.connect(self.calculate)
        self.ui.btn_8.clicked.connect(self.calculate)
        self.ui.btn_9.clicked.connect(self.calculate)
        self.ui.btn_plus.clicked.connect(self.calculate)
        self.ui.btn_mins.clicked.connect(self.calculate)
        self.ui.btn_mul.clicked.connect(self.calculate)
        self.ui.btn_div.clicked.connect(self.calculate)
        self.ui.btn_clear.clicked.connect(self.clear_)
        self.ui.btn_dot.clicked.connect(self.calculate)
        self.ui.btn_del.clicked.connect(self.del_)
        self.ui.btn_per.clicked.connect(self.equal_)

    def calculate(self):
        sender = self.sender().text()
        text = self.ui.label_enter.text()
        self.ui.label_enter.setText(text + sender)


    def clear_(self):
        self.ui.label_enter.setText("")
 
    def del_(self):
        text = self.ui.label_enter.text()
        self.ui.label_enter.setText(text[:len(text)-1])

    def equal_(self):
        equation = self.ui.label_enter.text()
        try:
            ans = eval(equation)
            self.ui.label_enter.setText(str(ans))
        
        except:
            self.msg.setWindowTitle("Error!")
            self.msg.setText("Please enter numbers.")


def app():
    app = appli(sys.argv)
    win = CalculatorApp()
    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    app()