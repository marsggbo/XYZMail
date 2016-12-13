#!/usr/bin/python
import json,os
# #Function:Analyze json script
# #Json is a script can descript data structure as xml,
# #for detail, please refer to "http://json.org/json-zh.html".

# #Note:
# #1.Also, if you write json script from python,
# #you should use dump instead of load. pleaser refer to "help(json)".

#json file:
#The file content of temp.json is:
#{
# "name":"00_sample_case1",
# "description":"an example."
#}

def GetEmailText(filename):
    f = open(filename,'r',encoding='utf-8')
    s = f.read()
    f.close()
    return s

# a = GetEmailText('data/Confirm your account... Dojo A.html')
# a = GetEmailText('data/在Twitter 上关注BBC Sport,David Wi.html')
# print(len(a))
# print(type(a))
# print(a)
# def GetLoginInfo():
#     f = open("contacts.json",'r',encoding='utf-8')
#     s = json.load(f)
#     f.close()
#     return s

a = '''\n\n\n\n- 发送自XYZ邮箱 -\n-------- 转发的邮件 --------\n发件人: xsa \n日期:cds \n主题: xsa\n'''
my_formatText = a.split('-\n')
b = my_formatText[2].split('\n')
s = (my_formatText[0], my_formatText[1],b[0],b[1],b[2])
print(s)

def SaveLoginInfo(data):
    f = open("contacts.json","w",encoding='utf-8')
    f.write(json.dumps(data))
    f.close()

def GetJsonInfo(file):
    f = open(file,'r',encoding='utf-8')
    s = json.load(f)
    # print(s)
    f.close()
    return s
# test = GetJsonInfo('conf.json')
# print(test)
# a = GetLoginInfo()
# print(a)
# a = GetLoginInfo()
# print(a)
# a.pop('test')
# SaveLoginInfo(a)

# import os

# def iterbrowse(path):
#     for home, dirs, files in os.walk(path):
#         for filename in files:
#             yield os.path.join(home, filename)

# a = iterbrowse('data/')
# print(a)
# print(type(a))
# for fullname in iterbrowse("data/"):
#     print (fullname.split('data/')[1])


# import os
# files = []
# # root = "d:" + s + "ll" + s
# for i in os.listdir('data/'):
#     if os.path.isfile(os.path.join('data/',i)):
#         files.append(i)
# print(files)
# if 'test.html' in files:
# 	print('Yep')

# url = 'file:///' + os.path.abspath(os.path.join(os.path.dirname(__file__))) + r'\data\1.html'
# print(url)

# -*- coding: utf-8 -*-
# import sys, os
# print (os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))


# f = open("../data/241.html",'rb')
# my_email = f.read().decode()
# f.close()

# date = my_email.split("Date: ")[1].split("\n")[0]
# from_addr = my_email.split("From: ")[1].split("\n")[0].split("<")[0].replace(r'"','')
# subject = my_email.split("Subject: ")[1].split("\n")[0]
# emailInfo = date + '\n' + from_addr + '\n' + subject

# print(emailInfo)




# date = my_email.split("Date: ")[1]
# date2 = date.split("\n")[0]
# print(date2)
# print(date)
# print("*****************\n")
# from_addr = my_email.split("From: ")[1].split("To: ")[0]
# # print(from_addr)
# # print("*****************\n")
# subject = my_email.split("Subject: ")[1].split("MIME-Version: ")[0]
# # print(subject)
# # print("*****************\n")
# to_addr = my_email.split("To: ")[1].split("Subject: ")[0]
# # print(to_addr)
# # print("*****************\n")
# # print("Date:%s\nFrom:%s\nSubject:%s\nTo:%s\n"% (date,from_addr,subject,to_addr))


# email = date + '\n' + from_addr + '\n' + subject + '\n' + to_addr
# print(email)






# import poplib
# from email.parser import Parser

# email = "1435679023@qq.com"
# password = "19960229hexinABC"
# pop3_server = 'pop.qq.com'

# class ReceiveMail():
# 	def __init__(self, parent=None):
# 		self.emailInfo = {
# 		"email":"1435679023@qq.com",
# 		"pwd":"19960229hexinABC",
# 		"to_addr":"",
# 		"pop3_server":"pop.qq.com",
# 		"subject":"",
# 		"html":"",
# 		"plain":"",
# 		}
# 		self.index = 0

# 	def Receive(self):
# 		server = poplib.POP3_SSL(self.emailInfo["pop3_server"])
# 		server.set_debuglevel(1)
# 		print(server.getwelcome().decode('utf-8'))
# 		print("************************************\n\n")
# 		# 身份认证:
# 		server.user(self.emailInfo["email"])
# 		server.pass_(self.emailInfo["pwd"])

# 		# stat()返回邮件数量和占用空间:
# 		print('Messages: %s. Size: %s' % server.stat())
# 		print("1  ************************************\n\n")
# 		# list()返回所有邮件的编号:
# 		resp, mails, octets = server.list()
# 		# resp: 状态码
# 		# mails：邮件
# 		# 可以查看返回的列表类似[b'1 82923', b'2 2184', ...]
# 		# print("resp:%s\nmails:%s\nocters:%s\n"%(resp, mails, octets))
# 		# print(mails)
# 		# print("************************************\n\n")

# 		# 获取最新一封邮件, 注意索引号从1开始:
# 		self.index = len(mails)
# 		for i in range(self.index-9,self.index+1):
# 			msg_content = ''
# 			data = ''
# 			resp, lines, octets = server.retr(i)
# 			# print("resp:%s\nlines:%s\nocters:%s\n"%(resp, lines, octets))

# 			# lines存储了邮件的原始文本的每一行,
# 			# 可以获得整个邮件的原始文本:
# 			msg_content = b'\r\n'.join(lines).decode('utf-8')
# 			print(msg_content)
# 			print("2   ************************************\n\n")
# 			# # 稍后解析出邮件:
# 			msg = Parser().parsestr(msg_content)
# 			data = str(msg)
# 			print(data)
# 			print("3   ************************************\n\n")


# 			f = open('../data/%s.html'%i,'wb')
# 			f.write(data.encode('utf-8'))
# 			f.close()
# 			# 可以根据邮件索引号直接从服务器删除邮件:
# 			# server.dele(i)
# 			# 关闭连接:
# 		server.quit()
# 		return self.index

# test = ReceiveMail()
# test.Receive()




# for i in range(5,0,-1):
# 	print(i)


# import time, threading

# # 新线程执行的代码:
# def loop():
#     print('thread %s is running...' % threading.current_thread().name)
#     n = 0
#     while n < 5:
#         n = n + 1
#         print('thread %s >>> %s' % (threading.current_thread().name, n))
#         time.sleep(1)
#     print('thread %s ended.' % threading.current_thread().name)
#     return 123

# print('thread %s is running...' % threading.current_thread().name)
# t = threading.Thread(target=loop, name='LoopThread')
# t.start()
# print(type(t))
# print(t)
# t.join()
# print('thread %s ended.' % threading.current_thread().name)


# f = open('../data/content1.html','rb')
#
# content = f.read()
#
# f.close()

# print(content.decode('utf-8'))



# 处理邮件
 
        # # self.index = ReceiveMail.Receive(self)
        # # print("总邮件数:%d"%self.index)

        # if self.index > 6:
        #     # my_DecodeMail.DecodeMail()
        #     for i in range(self.index,self.index-6,-1):
        #         f = open("../data/%s.html"%str(i),'rb')
        #         my_email = f.read().decode()
        #         f.close()
        #         date = my_email.split("Date: ")[1].split("\n")[0]
        #         from_addr = my_email.split("From: ")[1].split("\n")[0].split("<")[0].replace(r'"','')
        #         subject = my_email.split("Subject: ")[1].split("\n")[0]
        #         emailInfo = date + '\n' + from_addr + '\n' + subject

        #         self.emaillist.addItem(emailInfo)
        # else:
        #     for i in range(self.index+1,0,-1):
        #         f = open("../data/%s.html"%str(i),'rb')
        #         my_email = f.read().decode()
        #         f.close()
        #         date = my_email.split("Date: ")[1].split("\n")[0]
        #         from_addr = my_email.split("From: ")[1].split("\n")[0].split("<")[0].replace(r'"','')
        #         subject = my_email.split("Subject: ")[1].split("\n")[0]
        #         emailInfo = date + '\n' + from_addr + '\n' + subject
        #         self.emaillist.addItem(emailInfo)

a = {}
# a = {
# 	'n1':{
# 		'name':'n1',
# 		'sex':'woman'
# 	},
# 	'marsggbo': {
# 		'name': 'marsggbo',
# 		'sex': 'man'
# 	}
# }
# b = {
# 	'mars':{
# 		'name':'mars',
# 		'sex':'man'
# 	},
# 	'marsggbo':{
# 		'name':'marsggbo',
# 		'sex':'man'
# 	}
# }
# c = {
# 	'mars123':{
# 		'name':'mars123',
# 		'sex':'man'
# 	},
# 	'marsggbo2':{
# 		'name':'marsggbo2',
# 		'sex':'man'
# 	},
# 	'n1':{
# 		'name':'n1',
# 		'sex':'man'
# 	}
# }
# print("更新前")
# print(a)
#
# a.update(b)
# a.update(c)
#
# print("更新后")
# print(a)

#
# a = "你怎么会在这了？这里是华中科技大学啊亲啊！！！(⊙o⊙)哦"
# print(len(a))
# if len(a) > 20:
# 	b = a[:20]
# 	print(len(b))
# 	print(b)
# else:
# 	print(a)
# print(a)
# b = {}
# print(type(b))
# print(b)
# if b == {}:
# 	print('啥都么有')
# for i in b:
# 	if i:
# 		print('有东西 '+i+":"+b[i])
# 	else:
# 		print('空的')

# from PyQt4 import QtCore,QtGui
# from PyQt4.QtCore import *  
# from PyQt4.QtGui import *  
# # from PyQt4.QtWidgets import *
# import time
# '''
# 信号传参类型
# pyqtSignal()                                #无参数信号
# pyqtSignal(int)                             # 一个参数(整数)的信号 
# pyqtSignal([int],[str]                     # 一个参数(整数或者字符串)重载版本的信号
# pyqtSignal(int,str)                         #二个参数(整数,字符串)的信号 
# pyqtSignal([int,int],[int,str])           #二个参数([整数,整数]或者[整数,字符串])重载版本
# '''
# class Mythread(QThread):
#     #定义信号,定义参数为str类型 
#     _signal=pyqtSignal(str)   
#     def __init__(self):
#         super(Mythread,self).__init__() 
#     def run(self):  
#         for i in range(2000000):
#             #发出信号
#             self._signal.emit('当前循环值为:%s'%i) 
#             #让程序休眠
#             time.sleep(0.5)   
# if __name__ == '__main__':
#     app = QApplication([])
#     dlg = QDialog()
#     dlg.resize(400, 300)
#     dlg.setWindowTitle("自定义按钮测试")
#     dlgLayout = QVBoxLayout()
#     dlgLayout.setContentsMargins(40, 40, 40, 40)
#     btn=QPushButton('测试按钮')
#     dlgLayout.addWidget(btn)
#     dlgLayout.addStretch(40)
#     dlg.setLayout(dlgLayout)
#     dlg.show()
    
    
#     def chuli(s):
#         dlg.setWindowTitle(s)
#         btn.setText(s)
#     #创建线程
#     thread=Mythread()
#     #注册信号处理函数
#     thread._signal.connect(chuli)
#     #启动线程
#     thread.start()
#     dlg.exec_()
#     app.exit()