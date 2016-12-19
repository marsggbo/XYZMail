# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""
import smtplib
from PyQt4 import QtCore,  QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
# from PyQt4.QtCore import pyqtSlot
# from PyQt4.QtGui import QDialog,QMessageBox

from Ui_login import Ui_Dialog
from DealJsonFile import GetJsonInfo, SaveJsonInfo
import time,  os

class Login(QDialog, Ui_Dialog):
	def __init__(self, parent=None):
		super(Login, self).__init__(parent)
		self.setupUi(self)
		self.setWindowFlags(Qt.FramelessWindowHint | Qt.Dialog)
		self.emailInfo = GetJsonInfo('conf.json')

		# 初始化
		if self.emailInfo["email"] and self.emailInfo["pwd"]:
			email = self.emailInfo["email"]
			pwd = self.emailInfo["pwd"]
			self.loginmail.setText(email)
			self.loginpwd.setText(pwd)
			self.loginsmtp.setText(self.emailInfo['smtp_server'])
			self.loginpop.setText(self.emailInfo['pop3_server'])


	# 无边框设计
	def mousePressEvent(self, event):
		if event.button() == Qt.LeftButton:
			self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
			QApplication.postEvent(self, QEvent(174))
			event.accept()
 
	def mouseMoveEvent(self, event):
		if event.buttons() == Qt.LeftButton:
			self.move(event.globalPos() - self.dragPosition)
			event.accept()

	@pyqtSlot()
	def on_login_clicked(self):
		# 登录
		self.run()

		self.emailInfo = GetJsonInfo('conf.json')
		if self.emailInfo['status'] == 0:
			alert = QMessageBox.warning(self, '登录失败', u'登录失败，请检查配置是否正确！')
			self.resize(500, 370)
		else:

			# 创建一个以邮件命名的文件夹，用于区分用户信息
			dir = '/data/%s'%(self.emailInfo['email'])
			# 获取当前文件的绝对路径
			abDir = os.path.abspath(os.path.join(os.path.dirname(__file__))).replace('\\','/')
			dir = ("%s/%s")%(abDir,dir)
			if not os.path.exists(dir):
				os.mkdir(dir)
				print("文件夹创建成功:%s"%dir)

			self.close()

	def run(self):
		# 获取登录信息
		self.emailInfo["email"] = self.loginmail.text()
		self.emailInfo["pwd"] = self.loginpwd.text()
		smtp_server = self.loginsmtp.text()
		pop3_server = self.loginpop.text()
		if smtp_server and pop3_server:
			self.emailInfo["smtp_server"] = smtp_server
			self.emailInfo["pop3_server"] = pop3_server
			self.emailInfo["status"] = 0
			SaveJsonInfo('conf.json', self.emailInfo)
		else:
			server = self.loginmail.text().split('@')[1].split('.com')[0]
			if server == 'foxmail':
				server = 'qq'
			smtp_server = 'smtp.%s.com' % server
			pop3_server = 'pop.%s.com' % server

			if 'hust' in server:
				smtp_server = 'mail.hust.edu.cn'
				pop3_server = 'mail.hust.edu.cn'

			self.emailInfo["smtp_server"] = smtp_server
			self.emailInfo["pop3_server"] = pop3_server
			self.emailInfo["status"] = 0
			SaveJsonInfo('conf.json', self.emailInfo)
			self.loginsmtp.setText(smtp_server)
			self.loginpop.setText(pop3_server)
		try:
			start = time.time()
			self.emailInfo = GetJsonInfo('conf.json')
			server = smtplib.SMTP_SSL(smtp_server, 465)
			server.set_debuglevel(1)
			print('\n***************************************\n\n')
			server.login(self.emailInfo["email"], self.emailInfo["pwd"])
			self.emailInfo["status"] = 1
			SaveJsonInfo('conf.json', self.emailInfo)
			end = time.time()
			print('耗时：' + str(end-start))

		except Exception as e:
			print(type(e))
			print(e)
			self.emailInfo["status"] = 0
			SaveJsonInfo('conf.json', self.emailInfo)

	@pyqtSlot()
	def on_loginSetting_clicked(self):
		self.resize(500, 370)

	@pyqtSlot()
	def on_loginClose_clicked(self):
		self.close()

	@pyqtSlot()
	def on_cancel_clicked(self):
		self.close()

	@pyqtSlot()
	def on_settingHide_clicked(self):
		self.resize(500,300)

if __name__ == '__main__':
	
	dir = 'data/%s'%("110@qq.com")
	# 获取当前文件的绝对路径
	abDir = os.path.abspath(os.path.join(os.path.dirname(__file__))).replace('\\','/')
	dir = ("%s/%s")%(abDir,dir)
	if not os.path.exists(dir):
		os.mkdir(dir)
		print("文件夹创建成功:%s"%dir)
