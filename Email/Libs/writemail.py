# -*- coding: utf-8 -*-

"""
Module implementing WriteEmailDialog.
"""
from PyQt4 import QtGui
from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import QDialog
from PyQt4.QtGui import QMessageBox
from email.mime.base import MIMEBase
from email.header import Header
from email import encoders
from email.encoders import encode_base64
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
	def __init__(self, parent=None,isForwad=False,ForwardInfo=None,url=None,\
	isReply=False,replyInfo=None):
		super(WriteEmailDialog, self).__init__(parent)
		self.setupUi(self)
		self.emailInfo = GetJsonInfo('conf.json')
		self.email = SendMail(From = self.emailInfo['email'],
						pwd = self.emailInfo['pwd'],
						smtp_server = self.emailInfo['smtp_server'])
		self.isForwad = isForwad
		self.isReply = isReply
		if self.isForwad:
			self.emailText = GetEmailText(url)
			self.formatText = '''\n\n\n\n- 发送自XYZ邮箱 -\n-------- 转发的邮件 --------\n发件人: "%s" %s\n日期: %s\n主题: %s\n'''\
			%(ForwardInfo['email'],
				ForwardInfo['name'],
				ForwardInfo['time'],
				ForwardInfo['subject'])
			self.emailContent.setPlainText(self.formatText)

			# 将转发信息格式化
			str1 = self.formatText.split('-\n')
			str2 = str1[2].split('\n')
			str3 = (str1[0]+'-',str1[1]+'-',str2[0],str2[1],str2[2])
			self.formatText = '<div>%s<br>%s<br>%s<br>%s<br>%s<br><div>\
			</div><div style="clear:both;"></div>'% str3

		if self.isReply:
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
					self.email.msg['To']= receiver
					self.email.msg['Subject'] = Header(subject, 'utf-8').encode()
					self.email.msg['plain'] = self.emailContent.toPlainText()
					if self.isForwad:
						my_addText = self.emailContent.toPlainText().split('- 发送自XYZ')[0] # 添加的转发信息
						if my_addText.strip():
							self.email.msg["html"] = my_addText + '<br><br>' + self.formatText + self.emailText
						else:
							self.email.msg['html'] = self.formatText + self.emailText
					else:
						self.email.msg["html"] = self.emailContent.toPlainText()
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
		options = QtGui.QFileDialog.Options()
		fileName = QtGui.QFileDialog.getOpenFileName(parent = self,
				caption = "please select your files",
				filter = "All Files (*);;Text Files (*.txt)", options = options)
		if fileName:
			with open(fileName, 'rb') as f:
				msg_attach = MIMEBase('application', 'octet-stream', filename = fileName)
				msg_attach.set_payload(f.read())
				encoders.encode_base64(msg_attach)
				f.close()
				msg_attach.add_header('Content-Disposition', 'attachment', filename = fileName)
				self.email.msg.attach(msg_attach)

