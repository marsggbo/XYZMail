# -*- coding: utf-8 -*-

"""
Module implementing WriteEmailDialog.
"""

from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import QDialog,QMessageBox

from Ui_writemail import Ui_WriteEmailDialog
from smtp import SendMail
from DealJsonFile import GetJsonInfo, SaveJsonInfo
import time

def GetEmailText(filename):
	f = open(filename,'r',encoding='utf-8')
	s = f.read()
	f.close()
	return s

class WriteEmailDialog(QDialog, Ui_WriteEmailDialog):

	# isForward用于判断是否是转发,默认不是转发,text是转发内容
	def __init__(self, parent=None,isForwad=False,ForwardInfo=None,url=None,isReply=False,replyInfo=None):
		super(WriteEmailDialog, self).__init__(parent)
		self.setupUi(self)
		self.emailInfo = GetJsonInfo('conf.json')
		self.email = SendMail()
		self.isForwad = isForwad
		self.isReply = isReply
		# self.info = info  # info是要转发的用户信息，用元组表示
		if self.isForwad:
			self.emailText = GetEmailText(url)
			self.formatText = '''\n\n\n\n- 发送自XYZ邮箱 -\n-------- 转发的邮件 --------\n发件人: "%s" %s\n日期: %s\n主题: %s\n'''%(ForwardInfo['email'],ForwardInfo['name'],ForwardInfo['time'],ForwardInfo['subject'])
			self.emailContent.setPlainText(self.formatText)

			# 将转发信息格式化
			str1 = self.formatText.split('-\n')
			str2 = str1[2].split('\n')
			str3 = (str1[0],str1[1],str2[0],str2[1],str2[2])
			self.formatText = '<div>%s<br>%s<br>%s<br>%s<br>%s<br><div></div><div style="clear:both;"></div>'% str3

		if self.isReply:
			self.emailText = GetEmailText(url)
			self.formatText = '''\n\n\n\n- 发送自XYZ邮箱 -\n-------- 转发的邮件 --------\n发件人: "%s" %s\n日期: %s\n主题: %s\n''' % (
				ForwardInfo['email'], ForwardInfo['name'], ForwardInfo['time'], ForwardInfo['subject'])
			self.emailContent.setPlainText(self.formatText)

			# 将转发信息格式化
			str1 = self.formatText.split('-\n')
			str2 = str1[2].split('\n')
			str3 = (str1[0], str1[1], str2[0], str2[1], str2[2])
			self.formatText = '<div>%s<br>%s<br>%s<br>%s<br>%s<br><div></div><div style="clear:both;"></div>' % str3
			self.receiverEdit.setText(replyInfo['reply_addr'])
			self.subjectEdit.setText(replyInfo['reply_subject'])

	@pyqtSlot()
	def on_send_clicked(self):
		try:
			print("send!")
			receivers = self.receiverEdit.text()
			subject = self.subjectEdit.text()
			receivers = receivers.split(',')
			for receiver in receivers:
				if receiver and subject:
					self.email.emailInfo["to_addr"] = receiver
					self.email.emailInfo["subject"] = subject
					self.email.emailInfo["plain"] = self.emailContent.toPlainText()
					if self.isForwad:
						my_addText = self.emailContent.toPlainText().split('- 发送自XYZ')[0] # 添加的转发信息
						if my_addText.strip():
							self.email.emailInfo["html"] = my_addText + '<br><br>' + self.formatText + self.emailText
						else:
							self.email.emailInfo['html'] = self.formatText + self.emailText
					else:
						self.email.emailInfo["html"] = self.emailContent.toPlainText()
					self.email.Send()
					alert = QMessageBox.warning(self, '发送邮件', u'发送成功！')
					self.close()
				else:
					alert = QMessageBox.warning(self,'发送邮件提示','请将信息填写完整!')
			
		except Exception as e:
			print(str(e))
			a = str(e)
			alert = QMessageBox.warning(self, '发送失败', u'出错啦')

	@pyqtSlot()
	def on_accessory_clicked(self):
		print("Fujian")
