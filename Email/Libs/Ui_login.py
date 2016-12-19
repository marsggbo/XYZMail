# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\14356\Desktop\EmailSystem_搜索_转发_回复_12.15\Email\Libs\login.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(500, 300)
        Dialog.setMinimumSize(QtCore.QSize(500, 300))
        Dialog.setMaximumSize(QtCore.QSize(500, 370))
        Dialog.setStyleSheet(_fromUtf8("*{\n"
"font: 9pt \"Microsoft YaHei UI\";\n"
"font-weight:bold;\n"
"}\n"
"#login,#cancel,#loginSetting{\n"
"background-color: rgb(0, 109, 182);\n"
"border:none;\n"
"border-radius:13px;\n"
"color:white;\n"
"}\n"
"#loginSetting:hover{\n"
"background-color: rgb(0,134,229);\n"
"}\n"
"#login:hover{\n"
"background-color: rgb(0,134,229);\n"
"}\n"
"#cancel:hover{\n"
"background-color: rgb(0,134,229);\n"
"}\n"
""))
        Dialog.setSizeGripEnabled(True)
        self.cancel = QtGui.QPushButton(Dialog)
        self.cancel.setGeometry(QtCore.QRect(290, 210, 100, 26))
        self.cancel.setObjectName(_fromUtf8("cancel"))
        self.loginClose = QtGui.QPushButton(Dialog)
        self.loginClose.setGeometry(QtCore.QRect(470, 0, 31, 31))
        self.loginClose.setStyleSheet(_fromUtf8("#loginClose{border-image: url(:/souce/souce/关闭1_2.png);}\n"
"#loginClose:hover{border-image: url(:/souce/souce/关闭1_1.png);}"))
        self.loginClose.setText(_fromUtf8(""))
        self.loginClose.setObjectName(_fromUtf8("loginClose"))
        self.loginmail = QtGui.QLineEdit(Dialog)
        self.loginmail.setGeometry(QtCore.QRect(160, 120, 230, 25))
        self.loginmail.setObjectName(_fromUtf8("loginmail"))
        self.settingBox = QtGui.QGroupBox(Dialog)
        self.settingBox.setGeometry(QtCore.QRect(0, 300, 501, 71))
        self.settingBox.setStyleSheet(_fromUtf8(""))
        self.settingBox.setTitle(_fromUtf8(""))
        self.settingBox.setObjectName(_fromUtf8("settingBox"))
        self.loginsmtp = QtGui.QLineEdit(self.settingBox)
        self.loginsmtp.setGeometry(QtCore.QRect(160, 0, 230, 25))
        self.loginsmtp.setObjectName(_fromUtf8("loginsmtp"))
        self.label_3 = QtGui.QLabel(self.settingBox)
        self.label_3.setGeometry(QtCore.QRect(80, 0, 61, 25))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.loginpop = QtGui.QLineEdit(self.settingBox)
        self.loginpop.setGeometry(QtCore.QRect(160, 40, 230, 25))
        self.loginpop.setObjectName(_fromUtf8("loginpop"))
        self.label_4 = QtGui.QLabel(self.settingBox)
        self.label_4.setGeometry(QtCore.QRect(80, 40, 71, 25))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.settingHide = QtGui.QPushButton(self.settingBox)
        self.settingHide.setGeometry(QtCore.QRect(480, 0, 21, 21))
        self.settingHide.setStyleSheet(_fromUtf8("#settingHide{\n"
"border-image: url(:/souce/souce/收起.png);\n"
"}\n"
"#settingHide:hover{\n"
"background-color: rgb(203, 203, 203);\n"
"}"))
        self.settingHide.setText(_fromUtf8(""))
        self.settingHide.setObjectName(_fromUtf8("settingHide"))
        self.loginpwd = QtGui.QLineEdit(Dialog)
        self.loginpwd.setGeometry(QtCore.QRect(160, 160, 230, 25))
        self.loginpwd.setText(_fromUtf8(""))
        self.loginpwd.setEchoMode(QtGui.QLineEdit.Password)
        self.loginpwd.setObjectName(_fromUtf8("loginpwd"))
        self.loginSetting = QtGui.QPushButton(Dialog)
        self.loginSetting.setGeometry(QtCore.QRect(160, 250, 230, 30))
        self.loginSetting.setObjectName(_fromUtf8("loginSetting"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(110, 120, 50, 25))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(110, 160, 50, 25))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.logoName = QtGui.QLabel(Dialog)
        self.logoName.setGeometry(QtCore.QRect(195, 50, 151, 51))
        self.logoName.setStyleSheet(_fromUtf8("#logoName{\n"
"font: 25px \"Helvetica\";\n"
"font-weight:bold;\n"
"color:rgb(0,134,229)\n"
"\n"
"}\n"
""))
        self.logoName.setTextFormat(QtCore.Qt.RichText)
        self.logoName.setAlignment(QtCore.Qt.AlignCenter)
        self.logoName.setObjectName(_fromUtf8("logoName"))
        self.loginlogo = QtGui.QLabel(Dialog)
        self.loginlogo.setGeometry(QtCore.QRect(240, 5, 50, 50))
        self.loginlogo.setStyleSheet(_fromUtf8("border-image: url(:/souce/souce/邮箱logo_colorful.png);"))
        self.loginlogo.setText(_fromUtf8(""))
        self.loginlogo.setAlignment(QtCore.Qt.AlignCenter)
        self.loginlogo.setObjectName(_fromUtf8("loginlogo"))
        self.login = QtGui.QPushButton(Dialog)
        self.login.setGeometry(QtCore.QRect(160, 210, 100, 26))
        self.login.setObjectName(_fromUtf8("login"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.loginmail, self.loginpwd)
        Dialog.setTabOrder(self.loginpwd, self.login)
        Dialog.setTabOrder(self.login, self.cancel)
        Dialog.setTabOrder(self.cancel, self.loginSetting)
        Dialog.setTabOrder(self.loginSetting, self.loginsmtp)
        Dialog.setTabOrder(self.loginsmtp, self.loginpop)
        Dialog.setTabOrder(self.loginpop, self.loginClose)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.cancel.setText(_translate("Dialog", "取消", None))
        self.loginmail.setPlaceholderText(_translate("Dialog", "输入邮箱账号", None))
        self.loginsmtp.setPlaceholderText(_translate("Dialog", "请配置smtp服务器", None))
        self.label_3.setText(_translate("Dialog", "SMTP配置:", None))
        self.loginpop.setPlaceholderText(_translate("Dialog", "请配置pop3服务器", None))
        self.label_4.setText(_translate("Dialog", "POP3配置:", None))
        self.loginpwd.setPlaceholderText(_translate("Dialog", "输入邮箱密码", None))
        self.loginSetting.setText(_translate("Dialog", "手动配置", None))
        self.label.setText(_translate("Dialog", "账号:", None))
        self.label_2.setText(_translate("Dialog", "密码:", None))
        self.logoName.setText(_translate("Dialog", "M@RS Mail", None))
        self.login.setText(_translate("Dialog", "登录", None))

import souce_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

