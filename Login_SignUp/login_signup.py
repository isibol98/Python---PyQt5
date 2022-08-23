#!/usr/bin/env python3
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication as appli, QMainWindow as mainWin
from PyQt5.QtWidgets import QMessageBox, QAbstractButton
from PyQt5.QtGui import QIcon
import sys
from login_ui import Ui_login_app
from signup_ui import Ui_signup_app

#login/signup by isibol98

class LoginApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(LoginApp,self).__init__()
        self.login_ui = Ui_login_app()
        self.login_ui.setupUi(self)
        #self.setWindowIcon
        self.login_ui.password.setEchoMode(QtWidgets.QLineEdit.Password)

        self.login_ui.login_button.clicked.connect(self.login_func)

    def login_func(self):
        username = self.login_ui.username.text()
        password = self.login_ui.password.text()
        if username or password == "":
            result = QMessageBox.warning(self,"Error","Please Enter Username and Password.", QMessageBox.Ok | QMessageBox.Cancel)
            if result == QMessageBox.Ok:
                pass
            else:
                QtWidgets.qApp.quit()

        






def app():
    app = appli(sys.argv)
    win = LoginApp()
    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    app()

