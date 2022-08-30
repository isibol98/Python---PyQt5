#!/usr/bin/env python3
from tabnanny import check
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox, QAbstractButton 
import sys
from login_ui import Ui_login_app
from signup_ui import Ui_signup_app
from connect import myclient

#login/signup by isibol98
#this is for education purpose. Make sure you keep safely user data in database.

class LoginApp(QtWidgets.QMainWindow): 
    def __init__(self):
        super(LoginApp,self).__init__()
        self.login_ui = Ui_login_app()
        self.widget = widget
        self.mydb = myclient["login-app"]
        self.mycollection = self.mydb["users"]
        self.login_ui.setupUi(self)
        #self.setWindowIcon
        self.login_ui.password.setEchoMode(QtWidgets.QLineEdit.Password)

        self.login_ui.login_button.clicked.connect(self.login_func)
        self.login_ui.signup_button.clicked.connect(self.goto_signup)

    def login_func(self):
        username = self.login_ui.username.text()
        password = self.login_ui.password.text()

        if "".__eq__(username) or "".__eq__(password): #check username&password is blank or not
            QMessageBox.warning(self,"Error","Please Enter Username and Password.", QMessageBox.Ok)
        else:
            self.database_check(username,password)

    def database_check(self,username,password):
        check = self.mycollection.count_documents({"username":username})
        if check >= 1: #check username is exist in database
            for i in self.mycollection.find({"username":username}):
                if i["password"] == password: #check password
                    QMessageBox.warning(self,"Logged In",f"Welcome {username}!", QMessageBox.Ok)
                else: 
                    QMessageBox.warning(self,"Error","Wrong password!", QMessageBox.Ok)
        else:
            QMessageBox.warning(self,"Error","Username is not valid.", QMessageBox.Ok)

    def goto_signup(self):
        signup = SignupApp()
        self.widget.addWidget(signup)
        self.widget.setCurrentIndex(widget.currentIndex()+1)

class SignupApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(SignupApp,self).__init__()
        self.signup_ui = Ui_signup_app()
        self.mydb = myclient["login-app"]
        self.mycollection = self.mydb["users"]
        self.signup_ui.setupUi(self)
        self.signup_ui.password_new.setEchoMode(QtWidgets.QLineEdit.Password)
        self.signup_ui.password_confirm.setEchoMode(QtWidgets.QLineEdit.Password)
        
        self.signup_ui.sign_up_button.clicked.connect(self.signup_func)

    def signup_func(self):
        username = self.signup_ui.username_new.text()
        password = self.signup_ui.password_new.text()
        password_confirm = self.signup_ui.password_confirm.text()
        if username != "":
            if password == password_confirm and password != "":
                password = self.signup_ui.password_confirm.text()
                new_user = {"username":username,"password":password}

                try:
                    self.mycollection.insert_one(new_user)      
                    QMessageBox.warning(self,"Success!","Successfully created account.", QMessageBox.Ok)
                    login = LoginApp()
                    widget.addWidget(login)
                    widget.setCurrentIndex(widget.currentIndex()+1)
                except:
                    print("Error.")

            else:
                result = QMessageBox.warning(self,"Password is invalid", "Password has not matched. Please confirm password again.", QMessageBox.Ok | QMessageBox.Cancel)
                if result == QMessageBox.Ok:
                    pass
                else:
                    QtWidgets.qApp.quit()
        else:
            result = QMessageBox.warning(self,"Username is invalid", "Please Enter an Username!", QMessageBox.Ok | QMessageBox.Cancel)
            if result == QMessageBox.Ok:
                pass
            else:
                QtWidgets.qApp.quit()


if __name__ == "__main__":
    app = QApplication(sys.argv) 
    widget = QtWidgets.QStackedWidget()
    mainwindow = LoginApp()
    widget.addWidget(mainwindow)
    widget.setFixedWidth(440)
    widget.setFixedHeight(460)   
    widget.show()
    sys.exit(app.exec_())
    

