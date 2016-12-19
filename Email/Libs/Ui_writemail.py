# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\14356\Desktop\EmailSystem_搜索_转发_回复_12.15\Email\Libs\writemail.ui'
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

class Ui_WriteEmailDialog(object):
    def setupUi(self, WriteEmailDialog):
        WriteEmailDialog.setObjectName(_fromUtf8("WriteEmailDialog"))
        WriteEmailDialog.resize(720, 560)
        WriteEmailDialog.setStyleSheet(_fromUtf8(""))
        WriteEmailDialog.setSizeGripEnabled(True)
        self.head = QtGui.QGroupBox(WriteEmailDialog)
        self.head.setGeometry(QtCore.QRect(0, 0, 721, 50))
        self.head.setStyleSheet(_fromUtf8("QGroupBox{background-color: rgb(244, 244, 244);}\n"
"#send{border:none;background-color: rgb(244, 244, 244);}\n"
"#accessory{border:none;background-color: rgb(244, 244, 244);}\n"
"#send:hover{background-color: rgb(219,219,219);}\n"
"#accessory:hover{background-color: rgb(219,219,219);}\n"
""))
        self.head.setTitle(_fromUtf8(""))
        self.head.setObjectName(_fromUtf8("head"))
        self.send = QtGui.QPushButton(self.head)
        self.send.setGeometry(QtCore.QRect(30, 15, 60, 30))
        self.send.setStyleSheet(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/souce/souce/发送.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.send.setIcon(icon)
        self.send.setObjectName(_fromUtf8("send"))
        self.accessory = QtGui.QPushButton(self.head)
        self.accessory.setGeometry(QtCore.QRect(110, 15, 60, 30))
        self.accessory.setStyleSheet(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/souce/souce/附件.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.accessory.setIcon(icon1)
        self.accessory.setObjectName(_fromUtf8("accessory"))
        self.groupBox = QtGui.QGroupBox(WriteEmailDialog)
        self.groupBox.setGeometry(QtCore.QRect(0, 50, 720, 150))
        self.groupBox.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.subject = QtGui.QLabel(self.groupBox)
        self.subject.setGeometry(QtCore.QRect(40, 90, 60, 15))
        self.subject.setObjectName(_fromUtf8("subject"))
        self.subjectEdit = QtGui.QLineEdit(self.groupBox)
        self.subjectEdit.setGeometry(QtCore.QRect(100, 90, 271, 20))
        self.subjectEdit.setObjectName(_fromUtf8("subjectEdit"))
        self.receiver = QtGui.QLabel(self.groupBox)
        self.receiver.setGeometry(QtCore.QRect(40, 40, 60, 15))
        self.receiver.setObjectName(_fromUtf8("receiver"))
        self.receiverEdit = QtGui.QLineEdit(self.groupBox)
        self.receiverEdit.setGeometry(QtCore.QRect(100, 40, 271, 20))
        self.receiverEdit.setObjectName(_fromUtf8("receiverEdit"))
        self.emailContent = QtGui.QPlainTextEdit(WriteEmailDialog)
        self.emailContent.setGeometry(QtCore.QRect(0, 220, 720, 340))
        self.emailContent.setPlainText(_fromUtf8(""))
        self.emailContent.setObjectName(_fromUtf8("emailContent"))
        self.groupBox_2 = QtGui.QGroupBox(WriteEmailDialog)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 200, 720, 20))
        self.groupBox_2.setStyleSheet(_fromUtf8("background-color: rgb(244, 244, 244);"))
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.pushButton = QtGui.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(10, 0, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 0, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_3.setGeometry(QtCore.QRect(150, 0, 75, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))

        self.retranslateUi(WriteEmailDialog)
        QtCore.QMetaObject.connectSlotsByName(WriteEmailDialog)

    def retranslateUi(self, WriteEmailDialog):
        WriteEmailDialog.setWindowTitle(_translate("WriteEmailDialog", "Dialog", None))
        self.send.setText(_translate("WriteEmailDialog", "发送", None))
        self.accessory.setText(_translate("WriteEmailDialog", "附件", None))
        self.subject.setText(_translate("WriteEmailDialog", "主 题:", None))
        self.receiver.setText(_translate("WriteEmailDialog", "收件人:", None))
        self.pushButton.setText(_translate("WriteEmailDialog", "样式编辑", None))
        self.pushButton_2.setText(_translate("WriteEmailDialog", "样式编辑", None))
        self.pushButton_3.setText(_translate("WriteEmailDialog", "样式编辑", None))

import souce_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    WriteEmailDialog = QtGui.QDialog()
    ui = Ui_WriteEmailDialog()
    ui.setupUi(WriteEmailDialog)
    WriteEmailDialog.show()
    sys.exit(app.exec_())

