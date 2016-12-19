# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\14356\Desktop\EmailSystem_搜索_转发_回复_12.15\Email\Libs\calender.ui'
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

class Ui_calenderDialog(object):
    def setupUi(self, calenderDialog):
        calenderDialog.setObjectName(_fromUtf8("calenderDialog"))
        calenderDialog.resize(450, 450)
        calenderDialog.setMaximumSize(QtCore.QSize(450, 450))
        calenderDialog.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        calenderDialog.setStyleSheet(_fromUtf8("#calenderDialog{background-color:white;}\n"
"\n"
"#calenderclose{border-radius:15px;border:none;background-color: rgb(0,120,215);}\n"
"\n"
"#calenderclose:hover{background-color: #ccc;}"))
        calenderDialog.setSizeGripEnabled(True)
        self.calendarWidget = QtGui.QCalendarWidget(calenderDialog)
        self.calendarWidget.setGeometry(QtCore.QRect(20, 0, 400, 400))
        self.calendarWidget.setObjectName(_fromUtf8("calendarWidget"))
        self.calenderclose = QtGui.QPushButton(calenderDialog)
        self.calenderclose.setGeometry(QtCore.QRect(160, 400, 121, 41))
        self.calenderclose.setStyleSheet(_fromUtf8(""))
        self.calenderclose.setObjectName(_fromUtf8("calenderclose"))

        self.retranslateUi(calenderDialog)
        QtCore.QMetaObject.connectSlotsByName(calenderDialog)

    def retranslateUi(self, calenderDialog):
        calenderDialog.setWindowTitle(_translate("calenderDialog", "Calender", None))
        self.calenderclose.setText(_translate("calenderDialog", "关闭", None))

import souce_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    calenderDialog = QtGui.QDialog()
    ui = Ui_calenderDialog()
    ui.setupUi(calenderDialog)
    calenderDialog.show()
    sys.exit(app.exec_())

