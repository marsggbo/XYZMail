# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
import smtplib
from PyQt4 import QtCore,  QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import time, os,sys

from Ui_main import Ui_MainWindow
from calender import calenderDialog
from writemail import WriteEmailDialog
from login import Login
from pop import ReceiveMail
from contacts import contacts
from DealJsonFile import GetJsonInfo, SaveJsonInfo
from search import Search

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
		# 邮件数量
		self.index = 0
		self.page = 0
		# 判断是否已经的登录邮箱,若已经登录才能进行后续操作
		self.login = 0

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
			self.emailInfo = {"pop3_server": "", "email": "", "pwd": "", "smtp_server": "", "status": 0}
			SaveJsonInfo('conf.json', self.emailInfo)

		self.emailInfo = GetJsonInfo('conf.json')
		self.attachList.hide()
		self.mainForward.hide()
		self.delEmail.hide()
		self.mainReply.hide()
		self.mainAttach.hide()

		# 绑定emailList
		self.connect(self.emaillist, SIGNAL('itemClicked(QListWidgetItem *)'), self.emailItemClicked)

		# 绑定attachList
		self.connect(self.attachList, SIGNAL('itemClicked(QListWidgetItem *)'), self.attachItemClicked)

		# 绑定searchList
		self.connect(self.searchList, SIGNAL('itemClicked(QListWidgetItem *)'), self.searchItemClicked)




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
			my_forwardInfo = {
				'subject':my_subject,
				'name':my_name,
				'email':my_email,
				'time':my_time
			}
			my_url = 'data/' + self.url.split('data/')[1]

			my_mainForward  = WriteEmailDialog(isForwad=True, ForwardInfo=my_forwardInfo,url=my_url)
			my_mainForward.exec_()

	# 回复邮件
	@pyqtSlot()
	def on_mainReply_clicked(self):
		my_subject = self.contEmailSubject.text()
		my_name = self.contName.text()
		my_email = self.contEmail.text()
		my_time = self.contEmailTime.text()
		my_forwardInfo = {
			'subject':my_subject,
			'name':my_name,
			'email':my_email,
			'time':my_time
		}
		my_url = 'data/' + self.url.split('data/')[1]
		reply_addr = self.contEmail.text()
		reply_subject = "Reply:" + self.contEmailSubject.text()
		my_replyInfo = {
			"reply_addr": reply_addr,
			"reply_subject": reply_subject
		}
		my_reply= WriteEmailDialog(isForwad=True, ForwardInfo=my_forwardInfo,url=my_url,isReply=True,replyInfo=my_replyInfo)
		my_reply.exec_()

	# 查看附件
	@pyqtSlot()
	def on_mainAttach_clicked(self):
		if self.mainAttach.text() == '查看附件':
			my_subject = self.contEmailSubject.text()
			dir = 'data/%s/%s' % (self.emailInfo['email'], my_subject)
			if os.path.exists(dir):
				self.attachList.clear()
				for file in os.listdir(dir):
					print(file)
					if os.path.isfile(os.path.join(dir, file)):
						self.attachList.addItem(file)
				self.attachList.show()
				self.mainAttach.setText('隐藏附件')
			else:
				my_alert = QMessageBox.warning(self, '操作失败', u'此邮件无附件')

		elif self.mainAttach.text() == "隐藏附件":
			self.attachList.hide()
			self.mainAttach.setText('查看附件')


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
		if self.searchMode.currentText() == '请选择':
			my_alert = QMessageBox.warning(self, '搜索失败', u'请选择一种搜索模式')
		else:
			keyword = self.searchlineEdit.text()    # 获取搜索关键字
			if keyword:
				self.userInfo = GetJsonInfo('conf.json')
				self.contacts = GetJsonInfo('contacts.json')
				self.emaillist.hide()
				self.sendedList.hide()
				self.searchList.show()
				begin = time.time()
				test = Search()
				test.run(self.userInfo, self.searchMode.currentText(), keyword)
				files = test.getResult()
				while files == None:
					files = test.getResult()
				print("2", files)
				self.searchList.clear()
				self.addQList(files,'searchList')
				print("耗时啥都不用2：", time.time() - begin)
			else:
				my_alert = QMessageBox.warning(self, '搜索失败', u'搜索内容不能为空！')


	# 将信息插入到列表
	def addQList(self,files,way):
		for subject in files:
			abstractContent = files[subject]['date'] + '\n' + subject + '\n' + files[subject]['name']
			if way == 'searchList':
				self.searchList.addItem(abstractContent)
			elif way == 'sendedList':
				self.sendedList.addItem(abstractContent)



	# 选择搜索模式
	@pyqtSlot(str)
	def on_searchMode_currentIndexChanged(self, p0):
		self.Mode = self.searchMode.currentText()
		print(self.Mode)
		if self.Mode == '请选择':
			self.searchlineEdit.setPlaceholderText('请选择一种搜索模式')
		elif self.Mode == '主题':
			self.searchlineEdit.setPlaceholderText('请输入要搜索的主题')
		elif self.Mode == '时间':
			self.searchlineEdit.setPlaceholderText('搜索时间格式为xxxx-xx-xx')
		elif self.Mode == '联系人':
			self.searchlineEdit.setPlaceholderText('请输入要搜索的联系人地址')
		elif self.Mode == '邮件内容':
			self.searchlineEdit.setPlaceholderText('请输入要搜索的邮件内容')

	# 查看附件
	@pyqtSlot()
	def attachItemClicked(self):
		dir = 'data/%s/%s'%(self.emailInfo['email'],self.contEmailSubject.text())
		my_currentItem = self.attachList.currentItem()
		attachName = my_currentItem.text()
		# 获取当前文件的绝对路径
		abDir = os.path.abspath(os.path.join(os.path.dirname(__file__))).replace('\\','/')
		dir = ("%s/%s/%s")%(abDir,dir,attachName)
		print(dir)
		try:
			os.startfile(dir)
		except Exception as e:
			my_alert = QMessageBox.warning(self, '操作失败', u'此邮件丢失')

	# 搜索列表点击触发显示邮件
	@pyqtSlot()
	def searchItemClicked(self):
		try:
			my_contacts = GetJsonInfo('contacts.json')
			my_currentItem = self.searchList.currentItem()
			my_text = my_currentItem.text().split('\n')[1].split('\n')[0]
			self.url = 'file:///' + os.path.abspath(os.path.join(os.path.dirname(__file__))) + r'/data/%s/%s.html'%(self.emailInfo['email'],my_text)
			self.url = self.url.replace('\\','/')
			print(self.url)
			self.contName.setText(my_contacts[my_text]['name'])
			self.contEmail.setText(my_contacts[my_text]['fromAddr'])
			self.contEmailTime.setText(my_contacts[my_text]['date'])
			self.contEmailSubject.setText(my_text)
			self.mainForward.show()
			self.delEmail.show()
			self.mainReply.show()
			self.mainAttach.show()
			self.emailShow.setUrl(QtCore.QUrl(self.url))
			self.attachList.hide()
		except Exception as e:
			print(str(e))
		print("search")


	# 绑定emaillist邮件列表点击事件
	@pyqtSlot()
	def emailItemClicked(self):
		try:
			self.item_enable_delete = True  # 点击一个元素，可删除
			my_contacts = GetJsonInfo('contacts.json')
			my_currentItem = self.emaillist.currentItem()
			my_text = my_currentItem.text().split('\n')[1].split('\n')[0]
			# dir = "data/%s"%self.emailInfo['email']
			self.url = 'file:///' + os.path.abspath(os.path.join(os.path.dirname(__file__))) + r'/data/%s/%s.html'%(self.emailInfo['email'],my_text)
			self.url = self.url.replace('\\','/')
			print(self.url)
			self.contName.setText(my_contacts[my_text]['name'])
			self.contEmail.setText(my_contacts[my_text]['fromAddr']) 
			self.contEmailTime.setText(my_contacts[my_text]['date'])
			self.contEmailSubject.setText(my_text)
			self.mainForward.show()
			self.delEmail.show()
			self.mainReply.show()
			self.mainAttach.show()
			self.emailShow.setUrl(QtCore.QUrl(self.url))
			self.attachList.hide()
		except Exception as e:
			print(str(e))

	# 将邮件摘要添加至收件箱列表
	def addQListWidgetItem(self):
		dir = 'data/%s'%self.emailInfo['email']
		files = []
		for file in os.listdir(dir):
			print(file)
			if os.path.isfile(os.path.join(dir,file)):
				files.append(file)
		print('****************************\n\n')
		my_contacts = GetJsonInfo('contacts.json')

		for subject in my_contacts:
			filename = subject + '.html'
			if filename in files:
				abstractContent = my_contacts[subject]['date'] +  '\n' + subject + '\n' + my_contacts[subject]['name']
				self.emaillist.addItem(abstractContent)

	# 接收邮件
	@pyqtSlot()
	def on_mainreceiveletter_clicked(self):
		if self.login == 0:
			my_alert = QMessageBox.warning(self, '操作失败', u'请先登录您的账号！')
		else:
			self.searchList.hide()
			self.sendedList.hide()
			self.emaillist.show()
			global receiveWay 
			receiveWay = 0
			self.ReceiveEmail = ReceiveEmail()
			self.ReceiveEmail.start()
			# time.sleep(3)
			self.emaillist.clear()
			self.addQListWidgetItem()

	# 接收更多邮件
	@pyqtSlot()
	def on_moreemail_clicked(self):
		if self.login == 0:
			my_alert = QMessageBox.warning(self, '操作失败', u'请先登录您的账号！')
		else:
			self.searchList.hide()
			self.sendedList.hide()
			self.emaillist.show()
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

	# 邮件列表排序
	@pyqtSlot()
	def on_emailsort_clicked(self):
		if self.login == 0:
			my_alert = QMessageBox.warning(self, '操作失败', u'请先登录您的账号！')
		else:
			print("排序")

	# 显示联系人界面
	@pyqtSlot()
	def on_addressbook_clicked(self):
		if self.login == 0:
			my_alert = QMessageBox.warning(self, '操作失败', u'请先登录您的账号！')
		else:
			my_contacts = contacts()
			my_contacts.exec_()

	# 登录
	@pyqtSlot()
	def on_mainlogin_clicked(self):
		self.hide()
		my_login = Login()
		my_login.exec_()
		self.emailInfo = GetJsonInfo('conf.json')
		if self.emailInfo['status'] == 1:
			self.mainUserName.setText(self.emailInfo['email'])
			self.mainlogin.setText('切换账号')
			self.emaillist.clear()
			self.login = 1
			self.show()

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

	# 已发送邮件箱
	@pyqtSlot()
	def on_sendedBox_clicked(self):
		if self.login == 0:
			my_alert = QMessageBox.warning(self, '操作失败', u'请先登录您的账号！')
		else:
			self.emaillist.hide()
			self.searchList.hide()
			self.sendedList.show()

	# 收件箱
	@pyqtSlot()
	def on_receivedBox_clicked(self):
		if self.login == 0:
			my_alert = QMessageBox.warning(self, '操作失败', u'请先登录您的账号！')
		else:
			self.searchList.hide()
			self.sendedList.hide()
			self.emaillist.show()

	# 关闭
	@pyqtSlot()
	def on_mainclose_clicked(self):
		self.close()

	# 最小化
	@pyqtSlot()
	def on_mainmin_clicked(self):
		self.showMinimized()

	# 关于
	@pyqtSlot()
	def on_about_clicked(self):
		aboutButton = QMessageBox.aboutQt(self,  'AboutQt')

if __name__ == "__main__":
	import sys
	app = QtGui.QApplication(sys.argv)
	app.addLibraryPath('./plugins')
	ui = MainWindow()
	ui.show()
	sys.exit(app.exec_())
