# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signup.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_signup_app(object):
    def setupUi(self, login_app):
        login_app.setObjectName("login_app")
        login_app.resize(420, 500)
        login_app.setStyleSheet("background-color: rgb(54, 54, 54);")
        self.first_label2 = QtWidgets.QLabel(login_app)
        self.first_label2.setGeometry(QtCore.QRect(150, 40, 141, 51))
        self.first_label2.setStyleSheet("color:rgb(255, 255, 255);\n"
"font-size:28pt;\n"
"")
        self.first_label2.setObjectName("first_label2")
        self.usename_labe_new = QtWidgets.QLabel(login_app)
        self.usename_labe_new.setGeometry(QtCore.QRect(50, 140, 81, 31))
        self.usename_labe_new.setStyleSheet("color:rgb(85, 255, 255); font-size:12pt\n"
"")
        self.usename_labe_new.setObjectName("usename_labe_new")
        self.username_new = QtWidgets.QLineEdit(login_app)
        self.username_new.setGeometry(QtCore.QRect(140, 140, 231, 31))
        self.username_new.setStyleSheet("color:rgbrgb(255, 255, 255)")
        self.username_new.setObjectName("username_new")
        self.psw_lbl_new = QtWidgets.QLabel(login_app)
        self.psw_lbl_new.setGeometry(QtCore.QRect(50, 200, 81, 31))
        self.psw_lbl_new.setStyleSheet("color:rgb(85, 255, 255); font-size:12pt\n"
"")
        self.psw_lbl_new.setObjectName("psw_lbl_new")
        self.password_new = QtWidgets.QLineEdit(login_app)
        self.password_new.setGeometry(QtCore.QRect(140, 200, 231, 31))
        self.password_new.setStyleSheet("color:rgbrgb(255, 255, 255)")
        self.password_new.setObjectName("password_new")
        self.sign_up_button = QtWidgets.QPushButton(login_app)
        self.sign_up_button.setGeometry(QtCore.QRect(260, 310, 111, 31))
        self.sign_up_button.setStyleSheet("background-color:rgb(167, 167, 167); font-size:14pt; color:rgb(85, 255, 255)")
        self.sign_up_button.setObjectName("sign_up_button")
        self.password_confirm = QtWidgets.QLineEdit(login_app)
        self.password_confirm.setGeometry(QtCore.QRect(140, 260, 231, 31))
        self.password_confirm.setStyleSheet("color:rgbrgb(255, 255, 255)")
        self.password_confirm.setObjectName("password_confirm")
        self.confirm_psw_lbl = QtWidgets.QLabel(login_app)
        self.confirm_psw_lbl.setGeometry(QtCore.QRect(20, 260, 111, 31))
        self.confirm_psw_lbl.setStyleSheet("color:rgb(85, 255, 255); font-size:10pt\n"
"")
        self.confirm_psw_lbl.setObjectName("confirm_psw_lbl")

        self.retranslateUi(login_app)
        QtCore.QMetaObject.connectSlotsByName(login_app)

    def retranslateUi(self, login_app):
        _translate = QtCore.QCoreApplication.translate
        login_app.setWindowTitle(_translate("login_app", "Login by isibol98"))
        self.first_label2.setText(_translate("login_app", "Sign Up"))
        self.usename_labe_new.setText(_translate("login_app", "Username:"))
        self.psw_lbl_new.setText(_translate("login_app", "Password:"))
        self.sign_up_button.setText(_translate("login_app", "Sign Up"))
        self.confirm_psw_lbl.setText(_translate("login_app", "Confirm Password:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    login_app = QtWidgets.QDialog()
    ui = Ui_signup_app()
    ui.setupUi(login_app)
    login_app.show()
    sys.exit(app.exec_())
