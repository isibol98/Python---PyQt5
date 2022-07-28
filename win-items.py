#!/usr/bin/env python3
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon
import sys

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()

    win.setWindowTitle("First App")  #window name
    win.setGeometry(200,200,500,500) #window settings
    win.setWindowIcon(QIcon("icon.png")) #add icon 
    win.setToolTip("My first app") #add tooltip

    label_name = QtWidgets.QLabel(win)
    label_name.setText("Your name: ")
    label_name.move(50,30) #set location of text on window- lat,lon

    label_surname = QtWidgets.QLabel(win)
    label_surname.setText("Your surname: ")
    label_surname.move(50,70)

    txt_name = QtWidgets.QLineEdit(win)
    txt_name.move(120,30)

    txt_surname = QtWidgets.QLineEdit(win)
    txt_surname.move(120,70)

    def clicked(self): 
        print(f"Saved!\nName: {txt_name.text()}\nSurname: {txt_surname.text()}" )

    btn_save = QtWidgets.QPushButton(win)
    btn_save.setText("Save")
    btn_save.move(120,120)
    btn_save.clicked.connect(clicked)

    win.show()
    sys.exit(app.exec_()) #add exit 

window()
