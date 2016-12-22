# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
import smtplib
from PyQt4 import QtCore,  QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import time, os,sys,threading
from email.parser import BytesParser

from Ui_main import Ui_MainWindow
from calender import calenderDialog
from writemail import WriteEmailDialog
from login import Login
from pop import ReceiveMail
from contacts import contacts
from DealJsonFile import GetJsonInfo, SaveJsonInfo
from locker import  decrypt
from search import Search

# 主界面类
class MainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self, parent=None):
		super(MainWindow, self).__init__(parent)
		self.setupUi(self)
		self.setWindowFlags(Qt.FramelessWindowHint | Qt.Dialog)
		# 邮件数量
		self.index = 0
		self.page = 0
		self.receiveWay = 0
		# 判断是否已经的登录邮箱,若已经登录才能进行后续操作
		self.login = 0

		# 下面变量用于记录已经添加到列表中的值，从而避免重复添加
		# 已接收邮件记录变量
		self.isReceived = {}
		# 已删除邮件记录变量
		self.isDeleted = {}
		# 草稿箱记录变量
		self.isDraft = {}
		# 已发送邮件记录变量
		self.isSent = {}

		# 登录上次账号
		try:
			start = time.time()
			self.emailInfo = GetJsonInfo('conf.json')
			server = smtplib.SMTP_SSL(self.emailInfo["smtp_server"], 465)
			server.set_debuglevel(1)
			print('\n***************************************\n\n')
			password = decrypt(self.emailInfo["pwd"])
			server.login(self.emailInfo["email"], password)
			self.emailInfo["status"] = 1
			SaveJsonInfo('conf.json', self.emailInfo)

			end = time.time()
			print('耗时：' + str(end - start))
			self.mainUserName.setText(self.emailInfo['email'])
			self.mainlogin.setText('切换')
			self.login = 1

			# 获取当前文件的绝对路径
			abDir = os.path.abspath(os.path.join(os.path.dirname(__file__))).replace('\\','/')
			dir = "%s/data/%s/"%(abDir,self.emailInfo['email'])
			self.receiveJsonName = dir + "receive.json"
			self.sendJsonName = dir + "send.json"
			self.deleteJsonName = dir + "delete.json"
			self.draftJsonName = dir + "draft.json"
			p1 = threading.Thread(target=self.addQList(GetJsonInfo(self.receiveJsonName), 'emaillist'))
			p1.start()

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
		self.bufferGif.hide()

		# 绑定emailList
		self.connect(self.emaillist, SIGNAL('itemClicked(QListWidgetItem *)'), self.emailItemClicked)

		# 绑定attachList
		self.connect(self.attachList, SIGNAL('itemClicked(QListWidgetItem *)'), self.attachItemClicked)

		# 绑定searchList
		self.connect(self.searchList, SIGNAL('itemClicked(QListWidgetItem *)'), self.searchItemClicked)

		# 绑定deleteList
		self.connect(self.deleteList, SIGNAL('itemClicked(QListWidgetItem *)'), self.deleteItemClicked)

		# 绑定draftList
		self.connect(self.draftList, SIGNAL('itemClicked(QListWidgetItem *)'), self.draftItemClicked)

		# 绑定sentList
		self.connect(self.sentList, SIGNAL('itemClicked(QListWidgetItem *)'), self.sentItemClicked)

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
			abDir = os.path.abspath(os.path.join(os.path.dirname(__file__))).replace('\\', '/')
			dir = "%s/data/%s/" % (abDir, self.emailInfo['email'])
			my_url = dir + my_subject + '.html'

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

		abDir = os.path.abspath(os.path.join(os.path.dirname(__file__))).replace('\\', '/')
		dir = "%s/data/%s/" % (abDir, self.emailInfo['email'])
		my_url = dir + my_subject + '.html'
		# my_url = 'data/' + self.url.split('data/')[1]
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
				# 获取主题名
				my_subject = self.contEmailSubject.text()
				self.receive = GetJsonInfo(self.receiveJsonName)
				self.delete = GetJsonInfo(self.deleteJsonName)

				# 将删除邮件存至delete.json文件中
				temp = {
					my_subject:self.receive[my_subject]
				}
				print(temp)
				self.delete.update(temp)

				# 将邮件从receive.json中去除
				self.receive.pop(my_subject)

				# 数据回写
				SaveJsonInfo(self.receiveJsonName,self.receive)
				SaveJsonInfo(self.deleteJsonName,self.delete)

				self.contEmail.setText('')
				self.contEmailTime.setText('')
				self.contEmailSubject.setText('')
				self.contName.setText('')
				self.emailShow.setUrl(QtCore.QUrl("qrc:/souce/index.html"))

				self.emaillist.takeItem(self.emaillist.currentRow())
				self.item_enable_delete = False
				self.mainForward.hide()
				self.delEmail.hide()
				self.addQList(self.delete,'deleteList')


	# 查询邮件
	@pyqtSlot()
	def on_mainSearch_clicked(self):
		if self.searchMode.currentText() == '请选择':
			my_alert = QMessageBox.warning(self, '搜索失败', u'请选择一种搜索模式')
		else:
			keyword = self.searchlineEdit.text()    # 获取搜索关键字
			if keyword:
				self.userInfo = GetJsonInfo('conf.json')
				self.receive = GetJsonInfo(self.receiveJsonName)
				self.emaillist.hide()
				self.sentList.hide()
				self.searchList.show()
				begin = time.time()
				test = Search()
				test.run(self.userInfo, self.searchMode.currentText(), keyword)
				files = test.getResult()
				while files == None:
					files = test.getResult()
				print("2", files)
				self.searchList.clear()
				if len(files) > 0:
					self.addQList(files,'searchList')
				else:
					self.addQList({"搜索结果为空":{"date":"","subject":"搜索结果为空","name":""}},'searchList')
				print("耗时啥都不用2：", time.time() - begin)
			else:
				my_alert = QMessageBox.warning(self, '搜索失败', u'搜索内容不能为空！')


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

	# 垃圾箱列表点击触发显示邮件
	@pyqtSlot()
	def deleteItemClicked(self):
		try:
			self.item_enable_delete = True  # 点击一个元素，可删除
			my_delete = GetJsonInfo(self.deleteJsonName)
			my_currentItem = self.deleteList.currentItem()
			my_text = my_currentItem.text().split('\n')[1].split('\n')[0]

			url = 'file:///' + os.path.abspath(
				os.path.join(os.path.dirname(__file__))) + r'/data/%s/%s.html' % (
			self.emailInfo['email'], my_text)
			url = url.replace('\\', '/')
			print(url)

			self.contName.setText(my_delete[my_text]['name'])
			self.contEmail.setText(my_delete[my_text]['fromAddr'])
			self.contEmailTime.setText(my_delete[my_text]['date'])
			self.contEmailSubject.setText(my_text)
			self.mainForward.hide()
			self.delEmail.hide()
			self.mainReply.hide()
			self.mainAttach.show()
			self.attachList.hide()
			self.emailShow.setUrl(QtCore.QUrl(url))
		except Exception as e:
			print(str(e))
		print("delete")

	# 发件箱列表点击触发显示邮件
	@pyqtSlot()
	def sentItemClicked(self):
		try:
			self.item_enable_delete = True  # 点击一个元素，可删除
			my_sent = GetJsonInfo(self.sendJsonName)
			my_currentItem = self.sentList.currentItem()
			my_text = my_currentItem.text().split('\n')[1].split('\n')[0]

			url = 'file:///' + os.path.abspath(
				os.path.join(os.path.dirname(__file__))) + r'/data/%s/%s.html' % (
			self.emailInfo['email'], my_text)
			url = url.replace('\\', '/')
			print(url)

			self.contName.setText(my_sent[my_text]['name'])
			self.contEmail.setText(my_sent[my_text]['fromAddr'])
			self.contEmailTime.setText(my_sent[my_text]['date'])
			self.contEmailSubject.setText(my_text)
			self.mainForward.hide()
			self.delEmail.hide()
			self.mainReply.hide()
			self.mainAttach.show()
			self.emailShow.setUrl(QtCore.QUrl(url))
			self.attachList.hide()
		except Exception as e:
			print(str(e))
		print("sent")

	# 草稿箱列表点击触发显示邮件
	@pyqtSlot()
	def draftItemClicked(self):
		try:
			self.item_enable_delete = True  # 点击一个元素，可删除
			my_draft = GetJsonInfo(self.draftJsonName)
			my_currentItem = self.draftList.currentItem()
			my_text = my_currentItem.text().split('\n')[1].split('\n')[0]

			url = 'file:///' + os.path.abspath(
				os.path.join(os.path.dirname(__file__))) + r'/data/%s/%s.html' % (
			self.emailInfo['email'], my_text)
			url = url.replace('\\', '/')
			print(url)

			self.contName.setText(my_draft[my_text]['name'])
			self.contEmail.setText(my_draft[my_text]['fromAddr'])
			self.contEmailTime.setText(my_draft[my_text]['date'])
			self.contEmailSubject.setText(my_text)
			self.mainForward.hide()
			self.delEmail.hide()
			self.mainReply.hide()
			self.mainAttach.show()
			self.emailShow.setUrl(QtCore.QUrl(url))
			self.attachList.hide()
		except Exception as e:
			print(str(e))
		print("sent")

	# 搜索列表点击触发显示邮件
	@pyqtSlot()
	def searchItemClicked(self):
		try:
			self.item_enable_delete = True  # 点击一个元素，可删除
			my_receive = GetJsonInfo(self.receiveJsonName)
			my_currentItem = self.searchList.currentItem()
			my_text = my_currentItem.text().split('\n')[1].split('\n')[0]

			url = 'file:///' + os.path.abspath(os.path.join(os.path.dirname(__file__))) + r'/data/%s/%s.html'%(self.emailInfo['email'],my_text)
			url = url.replace('\\','/')
			print(url)

			self.contName.setText(my_receive[my_text]['name'])
			self.contEmail.setText(my_receive[my_text]['fromAddr'])
			self.contEmailTime.setText(my_receive[my_text]['date'])
			self.contEmailSubject.setText(my_text)
			self.mainForward.show()
			self.delEmail.show()
			self.mainReply.show()
			self.mainAttach.show()
			self.emailShow.setUrl(QtCore.QUrl(url))
			self.attachList.hide()
		except Exception as e:
			print(str(e))
		print("search")


	# 绑定emaillist邮件列表点击事件
	@pyqtSlot()
	def emailItemClicked(self):
		try:
			self.item_enable_delete = True  # 点击一个元素，可删除
			my_receive = GetJsonInfo(self.receiveJsonName)
			my_currentItem = self.emaillist.currentItem()
			my_text = my_currentItem.text().split('\n')[1].split('\n')[0]
			# dir = "data/%s"%self.emailInfo['email']
			url = 'file:///' + os.path.abspath(os.path.join(os.path.dirname(__file__))) + r'/data/%s/%s.html'%(self.emailInfo['email'],my_text)
			url = url.replace('\\','/')
			print(url)
			self.contName.setText(my_receive[my_text]['name'])
			self.contEmail.setText(my_receive[my_text]['fromAddr']) 
			self.contEmailTime.setText(my_receive[my_text]['date'])
			self.contEmailSubject.setText(my_text)
			self.mainForward.show()
			self.delEmail.show()
			self.mainReply.show()
			self.mainAttach.show()
			self.emailShow.setUrl(QtCore.QUrl(url))
			self.attachList.hide()
		except Exception as e:
			print(str(e))

	# 将信息插入到列表
	def addQList(self,files,way):
		if way == 'searchList':
			for subject in files:
				abstractContent = files[subject]['date'] + '\n' + subject + '\n' + files[subject]['name']
				self.searchList.addItem(abstractContent)
		elif way == 'sentList':
			for subject in files:
				if subject not in self.isSent:
					self.isSent.update({subject:files[subject]})
					abstractContent = files[subject]['date'] + '\n' + subject + '\n' + files[subject]['name']
					self.sentList.addItem(abstractContent)
		elif way == 'emaillist':
			for subject in files:
				if subject not in self.isReceived:
					self.isReceived.update({subject:files[subject]})
					abstractContent = files[subject]['date'] + '\n' + subject + '\n' + files[subject]['name']
					self.emaillist.addItem(abstractContent)
		elif way == 'deleteList':
			for subject in files:
				if subject not in self.isDeleted:
					self.isDeleted.update({subject:files[subject]})
					abstractContent = files[subject]['date'] + '\n' + subject + '\n' + files[subject]['name']
					self.deleteList.addItem(abstractContent)
		elif way == 'draftList':
			for subject in files:
				if subject not in self.isDraft:
					self.isDraft.update({subject:files[subject]})
					abstractContent = files[subject]['date'] + '\n' + subject + '\n' + files[subject]['name']
					self.draftList.addItem(abstractContent)

	# 接收邮件
	def runReceive(self):
		myPop = ReceiveMail()
		self.popServer = myPop.connect()
		self.emailNum = myPop.GetEmailNum()
		# 循环解析邮件
		for i in range(self.emailNum,0,-1):
			resp, lines, octets = self.popServer.retr(i)
			msg_content = b'\r\n'.join(lines)

			# 稍后解析出邮件:
			msg = BytesParser().parsebytes(msg_content)
			try:
				# 解析邮件基本信息
				currentEmailInfo = myPop.parseEmailInfo(msg)
				for item in currentEmailInfo:
					# 判断邮件是否已经添加到列表
					if item not in self.isReceived:
						self.isReceived.update(currentEmailInfo)
						# 解析邮件内容
						myPop.parseEmailContent(msg)
						self.addQList(currentEmailInfo,'emaillist')
			except Exception as e:
				print(str(e))

		myPop.quit()

	# 接收最新邮件
	@pyqtSlot()
	def on_mainreceiveletter_clicked(self):
		if self.login == 0:
			my_alert = QMessageBox.warning(self, '操作失败', u'请先登录您的账号！')
		else:
			self.searchList.hide()
			self.sentList.hide()
			self.emaillist.show()

			self.receiveWay = 0
			p = threading.Thread(target=self.runReceive)
			p.start()

			self.bufferGif.show()
			movie = QMovie("qrc:/souce/缓冲1.gif")
			self.bufferGif.setMovie(movie)
			movie.start()
			time.sleep(2)
			self.bufferGif.hide()

	# 选择邮件列表排序对象
	@pyqtSlot(str)
	def on_itemSortMode_currentIndexChanged(self, p0):
		mode = self.itemSortMode.currentText()
		print(mode)
		if mode == '按时间排序':
			print("时间")
		elif mode == "按主题排序":
			print("主题")
		elif mode == "按联系人排序":
			print("联系人")

	# 邮件列表排列顺序
	@pyqtSlot(str)
	def on_itemSortOrder_currentIndexChanged(self,p0):
		order = self.itemSortOrder.currentText()
		if order == "升序":
			self.emaillist.sortItems(Qt.AscendingOrder)
			self.searchList.sortItems(Qt.AscendingOrder)
			self.sentList.sortItems(Qt.AscendingOrder)
		elif order == "降序":
			self.emaillist.sortItems(Qt.DescendingOrder)
			self.searchList.sortItems(Qt.DescendingOrder)
			self.sentList.sortItems(Qt.DescendingOrder)


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
			# 获取当前文件的绝对路径
			abDir = os.path.abspath(os.path.join(os.path.dirname(__file__))).replace('\\','/')
			dir = "%s/data/%s/"%(abDir,self.emailInfo['email'])
			self.receiveJsonName = dir + "receive.json"
			self.sendJsonName = dir + "send.json"
			self.deleteJsonName = dir + "delete.json"
			self.draftJsonName = dir + "draft.json"
			p1 = threading.Thread(target=self.addQList(GetJsonInfo(self.receiveJsonName), 'emaillist'))
			p1.start()


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

	# 已发送邮件箱显示按钮
	@pyqtSlot()
	def on_sentBox_clicked(self):
		if self.login == 0:
			my_alert = QMessageBox.warning(self, '操作失败', u'请先登录您的账号！')
		else:
			self.emaillist.hide()
			self.searchList.hide()
			self.deleteList.hide()
			self.draftList.hide()
			sendJson = GetJsonInfo(self.sendJsonName)
			self.addQList(sendJson,'sentList')
			self.sentList.show()

	# 垃圾箱显示按钮
	@pyqtSlot()
	def on_deleteBox_clicked(self):
		if self.login == 0:
			my_alert = QMessageBox.warning(self, '操作失败', u'请先登录您的账号！')
		else:
			self.emaillist.hide()
			self.searchList.hide()
			self.draftList.hide()
			self.sentList.hide()
			deleteJson = GetJsonInfo(self.deleteJsonName)
			self.addQList(deleteJson,'deleteList')
			self.deleteList.show()

	# 草稿箱显示按钮
	@pyqtSlot()
	def on_draftBox_clicked(self):
		if self.login == 0:
			my_alert = QMessageBox.warning(self, '操作失败', u'请先登录您的账号！')
		else:
			self.emaillist.hide()
			self.searchList.hide()
			self.sentList.hide()
			self.deleteList.hide()
			draftJson = GetJsonInfo(self.draftJsonName)
			self.addQList(draftJson,'draftList')
			self.draftList.show()

	# 收件箱显示按钮
	@pyqtSlot()
	def on_receivedBox_clicked(self):
		if self.login == 0:
			my_alert = QMessageBox.warning(self, '操作失败', u'请先登录您的账号！')
		else:
			self.searchList.hide()
			self.sentList.hide()
			self.deleteList.hide()
			self.draftList.hide()
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
