# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""
import smtplib
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import QDialog,QMessageBox

from Ui_login import Ui_Dialog
from DealJsonFile import GetJsonInfo, SaveJsonInfo
import time, threading, os

# class LoginEmail(QtCore.QThread):
# 	def __init__(self, parent=None):
# 		super(LoginEmail,self).__init__(parent)
# 		self.emailInfo = {}
#
# 	def run(self):
# 		try:
# 			start = time.time()
# 			self.emailInfo = GetJsonInfo('conf.json')
# 			server = smtplib.SMTP_SSL(self.emailInfo["smtp_server"], 465)
# 			server.set_debuglevel(1)
# 			print('\n***************************************\n\n')
# 			server.login(self.emailInfo["email"], self.emailInfo["pwd"])
# 			self.emailInfo["status"] = 1
# 			SaveJsonInfo('conf.json', self.emailInfo)
# 			end = time.time()
# 			print('耗时：' + str(end-start))
#
# 		except Exception as e:
# 			print(type(e))
# 			print(e)
# 			self.emailInfo["status"] = 0
# 			SaveJsonInfo('conf.json', self.emailInfo)

class LoginEmail():
	def __init__(self):
		self.emailInfo = {}

	def run(self):
		try:
			start = time.time()
			self.emailInfo = GetJsonInfo('conf.json')
			server = smtplib.SMTP_SSL(self.emailInfo["smtp_server"], 465)
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

class Login(QDialog, Ui_Dialog):
	def __init__(self, parent=None):
		super(Login, self).__init__(parent)
		self.setupUi(self)
		self.emailInfo = GetJsonInfo('conf.json')

		# 初始化
		if self.emailInfo["email"] and self.emailInfo["pwd"]:
			email = self.emailInfo["email"]
			pwd = self.emailInfo["pwd"]
			self.loginmail.setText(email)
			self.loginpwd.setText(pwd)
			self.loginsmtp.setText(self.emailInfo['smtp_server'])
			self.loginpop.setText(self.emailInfo['pop3_server'])

	@pyqtSlot()
	def on_login_clicked(self):
		# 获取登录信息
		self.emailInfo["email"] = self.loginmail.text()
		self.emailInfo["pwd"] = self.loginpwd.text()
		self.emailInfo["smtp_server"] = self.loginsmtp.text()
		self.emailInfo["pop3_server"] = self.loginpop.text()
		self.emailInfo["status"] = 0
		SaveJsonInfo('conf.json', self.emailInfo)


		self.LoginEmail = LoginEmail()
		self.LoginEmail.run()

		self.emailInfo = GetJsonInfo('conf.json')
		if self.emailInfo['status'] == 0:
			alert = QMessageBox.warning(self, '登录失败', u'您的配置信息有误，请重新输入！')
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


	@pyqtSlot()
	def on_cancel_clicked(self):
		self.close()

if __name__ == '__main__':
	
	dir = 'data/%s'%("110@qq.com")
	# 获取当前文件的绝对路径
	abDir = os.path.abspath(os.path.join(os.path.dirname(__file__))).replace('\\','/')
	dir = ("%s/%s")%(abDir,dir)
	if not os.path.exists(dir):
		os.mkdir(dir)
		print("文件夹创建成功:%s"%dir)
