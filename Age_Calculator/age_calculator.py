#!/usr/bin/env python3
from PyQt5 import QtWidgets as widgets
from PyQt5.QtWidgets import QApplication as appli, QMainWindow
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QDate, QTime, QDateTime
import sys
from age_calculator_ui import Ui_MainWindow as MainWin

class AgeCalculatorApp(widgets.QMainWindow):
    def __init__(self):
        super(AgeCalculatorApp,self).__init__()
        self.ui = MainWin()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon("calculator_icon.png"))
        self.ui.calculate_age_current.clicked.connect(self.calculate_current)
        self.ui.calculate_age_dates.clicked.connect(self.calculate_dates)


    def calculate_current(self):
        start = self.ui.first.date()
        now = QDate.currentDate()
        result = start.daysTo(now)
        year = result//365
        months = (result%365)//30
        days = (result%365)%30
        
        QMessageBox.warning(self,"Result",f"{year} Year {months} Month(s) {days} Day(s)", QMessageBox.Ok)

    def calculate_dates(self):
        start = self.ui.first.date()
        end = self.ui.last.date()
        result = start.daysTo(end)
        year = result//365
        months = (result%365)//30
        days = (result%365)%30
        
        QMessageBox.warning(self,"Result",f"{year} Year {months} Month(s) {days} Day(s)", QMessageBox.Ok)





def app():
    app = appli(sys.argv)
    win = AgeCalculatorApp()
    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    app()
