# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
import smtplib
from PyQt4 import QtCore,  QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import time, threading, os,sys
from multiprocessing import Process

from Ui_main import Ui_MainWindow
from calender import calenderDialog
from writemail import WriteEmailDialog
from login import Login
from pop import ReceiveMail
from contacts import contacts
from DealJsonFile import GetJsonInfo, SaveJsonInfo

global page
global reveiveWay
page = 0
receiveWay = 0	# 0表示接收最新6封邮件，1表示接收更多邮件

class ReceiveEmail(QtCore.QThread):
	def __init__(self, parent=None):
		super(ReceiveEmail,self).__init__(parent)
		self.emailInfo = {}
		self.index = ReceiveMail().GetEmailNum()

	def run(self):
		global page
		global receiveWay
		if receiveWay == 1:
			if self.index > 6:
				my_index = self.index - page*6
				print(my_index)
			else:
				my_index = self.index
		elif receiveWay == 0:
			my_index = self.index

		my_pop3 = ReceiveMail().Receive(my_index)


class MainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self, parent=None):
		super(MainWindow, self).__init__(parent)
		self.setupUi(self)
		self.setWindowFlags(Qt.FramelessWindowHint | Qt.Dialog)
		self.emailInfo = GetJsonInfo('conf.json')
		# 邮件数量
		self.index = 0
		self.page = 0
		self.login = 0

		# 绑定QListWidget
		self.connect(self.emaillist, SIGNAL('itemClicked(QListWidgetItem *)'), self.itemClicked)

		# 搜索列表默认隐藏
		self.searchList.hide()

		# 登录上次账号
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
			print('耗时：' + str(end - start))
			self.mainUserName.setText(self.emailInfo['email'])
			self.mainlogin.setText('切换账号')
			self.login = 1

		except Exception as e:
			print(e)
			self.emailInfo["status"] = 0
			SaveJsonInfo('conf.json', self.emailInfo)


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

	# 转发
	@pyqtSlot()
	def on_mainForward_clicked(self):
		if self.login == 0:
			my_alert = QMessageBox.warning(self, '操作失败', u'请先登录您的账号！')
		else:
			my_subject = self.contEmailSubject.text()
			my_name = self.contName.text()
			my_email = self.contEmail.text()
			my_time = self.contEmailTime.text()
			my_info = {
				'subject':my_subject,
				'name':my_name,
				'email':my_email,
				'time':my_time
			}
			my_url = 'data/' + self.url.split('data/')[1]

			my_mainForward  = WriteEmailDialog(isForwad=True, info=my_info,url=my_url)
			my_mainForward.exec_()

	# 删除邮件
	@pyqtSlot()
	def on_delEmail_clicked(self):
		isDel = QMessageBox.information(self, '删除邮件', u'确定要删除该封邮件？', 'Yes', 'Cancel')
		if  self.item_enable_delete :
			if not isDel:
				my_subject = self.contEmailSubject.text()
				self.contacts = GetJsonInfo('contacts.json')
				self.contEmail.setText('')
				self.contEmailTime.setText('')
				self.contEmailSubject.setText('')
				self.contName.setText('')
				self.emailShow.setUrl(QtCore.QUrl("qrc:/souce/index.html"))
				self.contacts.pop(my_subject)
				self.emaillist.takeItem(self.emaillist.currentRow())
				self.item_enable_delete = False
				self.mainForward.hide()
				self.delEmail.hide()


	# 查询邮件
	@pyqtSlot()
	def on_mainSearch_clicked(self):
		self.contacts = GetJsonInfo('contacts.json')
		search_text = self.searchlineEdit.text()    # 获取搜索内容
		if search_text:
			# 联系人查找
			for item in self.contacts:
				if search_text == self.contacts[item]['fromAddr']:
					print('你找到信息如下')



	# 绑定邮件列表点击事件
	@pyqtSlot()
	def itemClicked(self):
		try:
			self.item_enable_delete = True  # 点击一个元素，可删除
			my_contacts = GetJsonInfo('contacts.json')
			my_currentItem = self.emaillist.currentItem()
			my_text = my_currentItem.text().split('\n')[1].split('\n')[0]
			self.url = 'file:///' + os.path.abspath(os.path.join(os.path.dirname(__file__))) + r'/data/%s.html'%my_text
			self.url = self.url.replace('\\','/')
			print(self.url)
			self.contName.setText(my_contacts[my_text]['name'])
			self.contEmail.setText(my_contacts[my_text]['fromAddr']) 
			self.contEmailTime.setText(my_contacts[my_text]['date'])
			self.contEmailSubject.setText(my_text)
			self.mainForward.show()
			self.delEmail.show()
			self.emailShow.setUrl(QtCore.QUrl(self.url))
		except Exception as e:
			print(str(e))

	# 将邮件摘要添加至列表
	def addQListWidgetItem(self):
		files = []
		for file in os.listdir('data/'):
			print(file)
			if os.path.isfile(os.path.join('data/',file)):
				files.append(file)
		print('****************************\n\n')
		my_contacts = GetJsonInfo('contacts.json')

		for subject in my_contacts:
			filename = subject + '.html'
			if filename in files:
				abstractContent = my_contacts[subject]['name'] +  '\n' + subject + '\n' + my_contacts[subject]['date'].split('+')[0]
				self.emaillist.addItem(abstractContent)

	# 接收邮件
	@pyqtSlot()
	def on_mainreceiveletter_clicked(self):
		if self.login == 0:
			my_alert = QMessageBox.warning(self, '操作失败', u'请先登录您的账号！')
		else:
			global receiveWay 
			receiveWay = 0
			self.ReceiveEmail = ReceiveEmail()
			self.ReceiveEmail.start()
			# time.sleep(3)
			self.emaillist.clear()
			self.addQListWidgetItem()

	@pyqtSlot()
	def on_moreemail_clicked(self):
		if self.login == 0:
			my_alert = QMessageBox.warning(self, '操作失败', u'请先登录您的账号！')
		else:
			global page
			page += 1
			print(page)

			global receiveWay
			receiveWay = 1
			self.ReceiveEmail = ReceiveEmail()
			self.ReceiveEmail.start()
			time.sleep(3)
			self.emaillist.clear()
			self.addQListWidgetItem()


	@pyqtSlot()
	def on_emailsort_clicked(self):
		if self.login == 0:
			my_alert = QMessageBox.warning(self, '操作失败', u'请先登录您的账号！')
		else:
			print("排序")

	@pyqtSlot()
	def on_addressbook_clicked(self):
		if self.login == 0:
			my_alert = QMessageBox.warning(self, '操作失败', u'请先登录您的账号！')
		else:
			my_contacts = contacts()
			my_contacts.exec_()

	@pyqtSlot()
	def on_mainlogin_clicked(self):
		my_login = Login()
		my_login.exec_()
		self.emailInfo = GetJsonInfo('conf.json')
		if self.emailInfo['status'] == 1:
			self.mainUserName.setText(self.emailInfo['email'])
			self.mainlogin.setText('切换账号')
			self.login = 1

	# 日历
	@pyqtSlot()
	def on_calender_clicked(self):
		my_calender = calenderDialog()
		my_calender.exec_()

	# 写信
	@pyqtSlot()
	def on_mainwriteletter_clicked(self):
		if self.login == 0:
			my_alert = QMessageBox.warning(self, '操作失败', u'请先登录您的账号！')
		else:
			my_writemail  = WriteEmailDialog()
			my_writemail.exec_()

	@pyqtSlot()
	def on_mainclose_clicked(self):
		self.close()

	@pyqtSlot()
	def on_mainmin_clicked(self):
		self.showMinimized()


if __name__ == "__main__":
	import sys
	app = QtGui.QApplication(sys.argv)
	app.addLibraryPath('./plugins')
	ui = MainWindow()
	ui.show()
	sys.exit(app.exec_())
