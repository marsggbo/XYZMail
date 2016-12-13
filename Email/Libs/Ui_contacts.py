# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\14356\Desktop\EmailSystem\Email\Libs\contacts.ui'
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

class Ui_contacts(object):
    def setupUi(self, contacts):
        contacts.setObjectName(_fromUtf8("contacts"))
        contacts.resize(1000, 600)
        contacts.setMinimumSize(QtCore.QSize(1000, 600))
        contacts.setMaximumSize(QtCore.QSize(1000, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/souce/souce/登录.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        contacts.setWindowIcon(icon)
        contacts.setSizeGripEnabled(True)
        self.contactsBack = QtGui.QWidget(contacts)
        self.contactsBack.setGeometry(QtCore.QRect(0, 0, 1000, 600))
        self.contactsBack.setMinimumSize(QtCore.QSize(1000, 600))
        self.contactsBack.setMaximumSize(QtCore.QSize(1000, 600))
        self.contactsBack.setStyleSheet(_fromUtf8("background-color:white;"))
        self.contactsBack.setObjectName(_fromUtf8("contactsBack"))
        self.label_7 = QtGui.QLabel(self.contactsBack)
        self.label_7.setGeometry(QtCore.QRect(450, 5, 100, 40))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.contClose = QtGui.QPushButton(self.contactsBack)
        self.contClose.setGeometry(QtCore.QRect(950, 20, 20, 20))
        self.contClose.setStyleSheet(_fromUtf8("#contClose{\n"
"    background-color:tomato;\n"
"    border-radius:10px;}\n"
"#contClose:hover{border-image: url(:/souce/souce/关闭1.png);}\n"
""))
        self.contClose.setText(_fromUtf8(""))
        self.contClose.setObjectName(_fromUtf8("contClose"))
        self.contMin = QtGui.QPushButton(self.contactsBack)
        self.contMin.setGeometry(QtCore.QRect(920, 20, 20, 20))
        self.contMin.setToolTip(_fromUtf8(""))
        self.contMin.setStyleSheet(_fromUtf8("#contMin{\n"
"background-color:rgb(255,224,81);\n"
"    border-radius:10px;}\n"
"#contMin:hover{\n"
"    border-image: url(:/souce/souce/最小化.png);\n"
"}\n"
""))
        self.contMin.setText(_fromUtf8(""))
        self.contMin.setObjectName(_fromUtf8("contMin"))
        self.contactsBox = QtGui.QWidget(contacts)
        self.contactsBox.setGeometry(QtCore.QRect(0, 50, 1000, 550))
        self.contactsBox.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
""))
        self.contactsBox.setObjectName(_fromUtf8("contactsBox"))
        self.contactUser = QtGui.QWidget(self.contactsBox)
        self.contactUser.setGeometry(QtCore.QRect(0, 0, 160, 550))
        self.contactUser.setStyleSheet(_fromUtf8("background-color: rgb(243,243,243);\n"
""))
        self.contactUser.setObjectName(_fromUtf8("contactUser"))
        self.contUserLogo = QtGui.QLabel(self.contactUser)
        self.contUserLogo.setGeometry(QtCore.QRect(50, 50, 60, 60))
        self.contUserLogo.setStyleSheet(_fromUtf8("border-image: url(:/souce/souce/登录.png);"))
        self.contUserLogo.setText(_fromUtf8(""))
        self.contUserLogo.setObjectName(_fromUtf8("contUserLogo"))
        self.contUserMail = QtGui.QLabel(self.contactUser)
        self.contUserMail.setGeometry(QtCore.QRect(0, 120, 160, 20))
        self.contUserMail.setStyleSheet(_fromUtf8("#contUserMail{\n"
"    text-align:center;\n"
"}"))
        self.contUserMail.setAlignment(QtCore.Qt.AlignCenter)
        self.contUserMail.setObjectName(_fromUtf8("contUserMail"))
        self.contactINfo = QtGui.QWidget(self.contactsBox)
        self.contactINfo.setGeometry(QtCore.QRect(400, 0, 600, 550))
        self.contactINfo.setStyleSheet(_fromUtf8("background-color: rgb(219,219,219);"))
        self.contactINfo.setObjectName(_fromUtf8("contactINfo"))
        self.contInfoTop = QtGui.QGroupBox(self.contactINfo)
        self.contInfoTop.setGeometry(QtCore.QRect(10, 10, 581, 160))
        self.contInfoTop.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.contInfoTop.setTitle(_fromUtf8(""))
        self.contInfoTop.setObjectName(_fromUtf8("contInfoTop"))
        self.contLogo = QtGui.QLabel(self.contInfoTop)
        self.contLogo.setGeometry(QtCore.QRect(40, 30, 91, 91))
        self.contLogo.setStyleSheet(_fromUtf8("border-image: url(:/souce/souce/登录.png);"))
        self.contLogo.setText(_fromUtf8(""))
        self.contLogo.setObjectName(_fromUtf8("contLogo"))
        self.contName = QtGui.QLabel(self.contInfoTop)
        self.contName.setGeometry(QtCore.QRect(160, 40, 131, 20))
        self.contName.setObjectName(_fromUtf8("contName"))
        self.contEmail = QtGui.QLabel(self.contInfoTop)
        self.contEmail.setGeometry(QtCore.QRect(160, 80, 130, 20))
        self.contEmail.setObjectName(_fromUtf8("contEmail"))
        self.contWriteLetter = QtGui.QPushButton(self.contInfoTop)
        self.contWriteLetter.setGeometry(QtCore.QRect(460, 100, 100, 30))
        self.contWriteLetter.setStyleSheet(_fromUtf8("#contWriteLetter{\n"
"    border:none;\n"
"    font-size:14px;\n"
"    background-color:rgb(219,219,219);\n"
"}\n"
"#contWriteLetter:hover{\n"
"background-color: rgb(26, 227, 159);\n"
"}"))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/souce/souce/发送.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.contWriteLetter.setIcon(icon1)
        self.contWriteLetter.setObjectName(_fromUtf8("contWriteLetter"))
        self.delContact = QtGui.QPushButton(self.contInfoTop)
        self.delContact.setGeometry(QtCore.QRect(460, 40, 100, 30))
        self.delContact.setStyleSheet(_fromUtf8("#delContact{\n"
"    border:none;\n"
"    font-size:14px;\n"
"    background-color: rgb(219,219,219);\n"
"}\n"
"#delContact:hover{\n"
"background-color:tomato;\n"
"color:white;\n"
"}"))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/souce/souce/关闭1.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delContact.setIcon(icon2)
        self.delContact.setObjectName(_fromUtf8("delContact"))
        self.contInfoBottom = QtGui.QGroupBox(self.contactINfo)
        self.contInfoBottom.setGeometry(QtCore.QRect(10, 179, 581, 361))
        self.contInfoBottom.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.contInfoBottom.setTitle(_fromUtf8(""))
        self.contInfoBottom.setObjectName(_fromUtf8("contInfoBottom"))
        self.label = QtGui.QLabel(self.contInfoBottom)
        self.label.setGeometry(QtCore.QRect(20, 20, 71, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.contInfoBottom)
        self.label_2.setGeometry(QtCore.QRect(60, 70, 54, 12))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.contInfoBottom)
        self.label_3.setGeometry(QtCore.QRect(60, 100, 54, 12))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.contInfoBottom)
        self.label_4.setGeometry(QtCore.QRect(20, 150, 71, 31))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.contInfoBottom)
        self.label_5.setGeometry(QtCore.QRect(60, 190, 54, 12))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.contInfoBottom)
        self.label_6.setGeometry(QtCore.QRect(60, 220, 54, 12))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.contRemarkName = QtGui.QLineEdit(self.contInfoBottom)
        self.contRemarkName.setGeometry(QtCore.QRect(120, 69, 241, 21))
        self.contRemarkName.setObjectName(_fromUtf8("contRemarkName"))
        self.contPhone = QtGui.QLineEdit(self.contInfoBottom)
        self.contPhone.setGeometry(QtCore.QRect(120, 100, 241, 21))
        self.contPhone.setObjectName(_fromUtf8("contPhone"))
        self.contQQ = QtGui.QLineEdit(self.contInfoBottom)
        self.contQQ.setGeometry(QtCore.QRect(120, 190, 241, 21))
        self.contQQ.setObjectName(_fromUtf8("contQQ"))
        self.contWechat = QtGui.QLineEdit(self.contInfoBottom)
        self.contWechat.setGeometry(QtCore.QRect(120, 220, 241, 21))
        self.contWechat.setObjectName(_fromUtf8("contWechat"))
        self.contCancel = QtGui.QPushButton(self.contInfoBottom)
        self.contCancel.setGeometry(QtCore.QRect(270, 312, 90, 30))
        self.contCancel.setStyleSheet(_fromUtf8("#contCancel{\n"
"    border:none;\n"
"    font-size:14px;\n"
"color:white;\n"
"    background-color: rgb(29, 171, 123);\n"
"}\n"
"#contCancel:hover{\n"
"background-color: rgb(26, 227, 159);\n"
"}"))
        self.contCancel.setObjectName(_fromUtf8("contCancel"))
        self.contSave = QtGui.QPushButton(self.contInfoBottom)
        self.contSave.setGeometry(QtCore.QRect(120, 312, 90, 30))
        self.contSave.setStyleSheet(_fromUtf8("#contSave{\n"
"    border:none;\n"
"    font-size:14px;\n"
"color:white;\n"
"    background-color: rgb(29, 171, 123);\n"
"}\n"
"#contSave:hover{\n"
"background-color: rgb(26, 227, 159);\n"
"}"))
        self.contSave.setObjectName(_fromUtf8("contSave"))
        self.contactsList = QtGui.QListWidget(self.contactsBox)
        self.contactsList.setGeometry(QtCore.QRect(159, 0, 241, 550))
        self.contactsList.setFrameShape(QtGui.QFrame.StyledPanel)
        self.contactsList.setLineWidth(1)
        self.contactsList.setIconSize(QtCore.QSize(200, 50))
        self.contactsList.setGridSize(QtCore.QSize(200, 65))
        self.contactsList.setViewMode(QtGui.QListView.ListMode)
        self.contactsList.setModelColumn(0)
        self.contactsList.setWordWrap(False)
        self.contactsList.setObjectName(_fromUtf8("contactsList"))

        self.retranslateUi(contacts)
        QtCore.QMetaObject.connectSlotsByName(contacts)

    def retranslateUi(self, contacts):
        contacts.setWindowTitle(_translate("contacts", "联系人", None))
        self.label_7.setText(_translate("contacts", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">通讯录</span></p></body></html>", None))
        self.contUserMail.setText(_translate("contacts", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">用户账号</span></p></body></html>", None))
        self.contName.setText(_translate("contacts", "用户名", None))
        self.contEmail.setText(_translate("contacts", "邮箱", None))
        self.contWriteLetter.setText(_translate("contacts", "写信", None))
        self.delContact.setText(_translate("contacts", "删除联系人", None))
        self.label.setText(_translate("contacts", "基本信息", None))
        self.label_2.setText(_translate("contacts", "备注：", None))
        self.label_3.setText(_translate("contacts", "联系电话:", None))
        self.label_4.setText(_translate("contacts", "社交信息", None))
        self.label_5.setText(_translate("contacts", "QQ:", None))
        self.label_6.setText(_translate("contacts", "WeChat:", None))
        self.contCancel.setText(_translate("contacts", "取消", None))
        self.contSave.setText(_translate("contacts", "保存", None))

import souce_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    contacts = QtGui.QDialog()
    ui = Ui_contacts()
    ui.setupUi(contacts)
    contacts.show()
    sys.exit(app.exec_())

