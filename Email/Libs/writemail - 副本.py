# -*- coding: utf-8 -*-

"""
Module implementing WriteEmailDialog.
"""

from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import QDialog

from Ui_writemail import Ui_WriteEmailDialog
from smtp import SendMail

class WriteEmailDialog(QDialog, Ui_WriteEmailDialog):
    
    def __init__(self, parent=None):
        super(WriteEmailDialog, self).__init__(parent)
        self.setupUi(self)
        self.email = SendMail()
    
    @pyqtSlot()
    def on_send_clicked(self):
        print("send!")
        receiver = self.receiverEdit.text()
        subject = self.subjectEdit.text()
        self.email.emailInfo["to_addr"] = receiver
        self.email.emailInfo["subject"] = subject
        self.email.emailInfo["plain"] = self.emailContent.toPlainText()
        self.email.emailInfo["html"] = self.emailContent.toPlainText()
        self.email.Send()

    @pyqtSlot()
    def on_accessory_clicked(self):
        print("Fujian")
