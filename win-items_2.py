#!/usr/bin/env python3
from PyQt5 import QtWidgets as widgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()

        self.setWindowTitle("First App")
        self.setGeometry(200,200,500,500)
        self.setWindowIcon(QIcon("icon.png")) 
        self.setToolTip("My first app")
        self.initUI()

    def initUI(self):
        self.label_name = widgets.QLabel(self)
        self.label_name.setText("Your name: ")
        self.label_name.move(30,35) #set location of text on window- lat,lon

        self.label_surname = widgets.QLabel(self)
        self.label_surname.setText("Your surname: ")
        self.label_surname.move(30,70)

        self.label_resut = widgets.QLabel(self)
        self.label_resut.resize(300,50)
        self.label_resut.move(150,150)

        self.txt_name = widgets.QLineEdit(self)
        self.txt_name.move(120,35)
        self.txt_name.resize(200,24)

        self.txt_surname = widgets.QLineEdit(self)
        self.txt_surname.move(120,75)
        self.txt_surname.resize(200,24)

        btn_save = widgets.QPushButton(self)
        btn_save.setText("Save")
        btn_save.move(120,120)
        btn_save.clicked.connect(self.clicked)

    def clicked(self): 
        self.label_resut.setText(f"Saved!\nName: {self.txt_name.text()}\nSurname: {self.txt_surname.text()}" )

def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()