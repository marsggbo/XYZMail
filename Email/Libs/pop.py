import poplib
import json
import time, threading
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr, parsedate
from DealJsonFile import GetJsonInfo, SaveJsonInfo
import os
import chardet



class ReceiveMail():
	def __init__(self, parent=None):
		self.emailInfo = GetJsonInfo('conf.json')
		self.index = 0

	# 获取邮件数量
	def GetEmailNum(self):
		# 建立连接
		self.server = poplib.POP3_SSL(self.emailInfo["pop3_server"])
		print(type(self.server))
		# 身份认证:
		self.server.user(self.emailInfo["email"])
		self.server.pass_(self.emailInfo["pwd"])

		# list()返回所有邮件的编号:
		# resp: 状态码
		# mails：邮件
		# 可以查看返回的列表类似[b'1 82923', b'2 2184', ...]
		resp, mails, octets = self.server.list()

		# 获取邮件数量, 注意索引号从1开始:
		self.index = len(mails)
		return self.index

	def Receive(self,index):
		self.server = poplib.POP3_SSL(self.emailInfo["pop3_server"])
		# 身份认证:
		self.server.user(self.emailInfo["email"])
		self.server.pass_(self.emailInfo["pwd"])
		if index > 6:
			for i in range(index,index-6,-1):
				msg_content = ''
				resp, lines, octets = self.server.retr(i)

				# lines存储了邮件的原始文本的每一行,
				# 可以获得整个邮件的原始文本:
				# 获取邮件编码格式
				for i,item in enumerate(lines):
					if "charset" in str(item):
						try:
							self.charset = str(item).split('charset')[1].split("=")[1]
							print('邮件编码格式1为：'+self.charset)
							break
						except Exception as e:
							print(str(e))
							with open('log.txt','rb') as f:
								f.write(item)
				if "utf" in self.charset.lower():
					self.charset = "utf-8"
					print('邮件编码格式2为：'+self.charset)
				msg_content = b'\r\n'.join(lines).decode(self.charset)

				# # 稍后解析出邮件:
				msg = Parser().parsestr(msg_content)
				self.print_info(msg)

				# 可以根据邮件索引号直接从服务器删除邮件:
				# server.dele(i)
				# 关闭连接:
		else:
			for i in range(index,0,-1):
				msg_content = ''
				resp, lines, octets = self.server.retr(i)

				# lines存储了邮件的原始文本的每一行,
				# 可以获得整个邮件的原始文本:
				# 获取邮件编码格式
				for i,item in enumerate(lines):
					if "charset=" in str(item):
						self.charset = str(item).split('charset')[1].split("=")[1]
						print('邮件编码格式为：'+self.charset)
						break
				if "utf" in self.charset.lower():
					self.charset = "utf-8"
					print('邮件编码格式2为：'+self.charset)
				msg_content = b'\r\n'.join(lines).decode(self.charset)

				# # 稍后解析出邮件:
				msg = Parser().parsestr(msg_content)
				self.print_info(msg)
		self.server.quit()


	def guess_charset(self,msg):
		charset = msg.get_charset()
		if charset is None:
			content_type = msg.get('Content-Type', '').lower()
			pos = content_type.find('charset=')
			if pos >= 0:
				charset = content_type[pos + 8:].strip()
		return charset


	def decode_str(self,s):
		value, charset = decode_header(s)[0]
		if charset:
			value = value.decode(charset)
		return value


	def print_info(self,msg, indent=0):
		if indent == 0:
			global subject
			my_info = {}
			my_emailInfos = {}

			subject = msg.get('Subject', '')
			if subject:
				subject = self.decode_str(subject)
				my_info['subject'] = subject

			fromAddr = msg.get('From', '')
			if fromAddr:
				hdr, addr = parseaddr(fromAddr)
				name = self.decode_str(hdr)
				my_info["name"] = name
				my_info["fromAddr"] = addr

			date = msg.get('Date', '')
			if date:
				date = self.decode_str(date)
				date = parsedate(date)
				date = list(date)
				for i in range(len(date)):
					if len(str(date[i])) == 1:
						date[i] = '0' + str(date[i])
				date = str(date[0]) + '.' + str(date[1]) + '.' + str(date[2]) + ' ' + str(date[3]) + ':' + str(
					date[4]) + ':' + str(date[5])
				my_info['date'] = date

			if len(subject) > 30:
				my_emailInfos[subject[:30]] = my_info
			else:
				my_emailInfos[subject] = my_info

			my_oringinInfo = GetJsonInfo('contacts.json')
			my_oringinInfo.update(my_emailInfos)
			SaveJsonInfo('contacts.json', my_oringinInfo)
			# my_oringinInfo = GetJsonInfo('%s.json')%self.emailInfo['email']
			# my_oringinInfo.update(my_emailInfos)
			# SaveJsonInfo('%s.json', my_oringinInfo)%self.emailInfo['email']

		if (msg.is_multipart()):
			pass
			parts = msg.get_payload()
			for n, part in enumerate(parts):
				# print('%s--------------------' % ('  ' * indent))
				self.print_info(part, indent + 1)

		else:
			content_type = msg.get_content_type()
			if content_type == 'text/plain' or content_type == 'text/html':
				content = msg.get_payload(decode=True)
				charset = self.guess_charset(msg)
				# print(charset)
				if charset:
					print("解码咯，编码为："+charset)
					try:
						content = content.decode('utf-8')
					except Exception as e:
						print(str(e))
						content = content.decode(charset)

				content = '<meta charset="utf-8">' + content + '<meta charset="utf-8">'

				# 保存为文件形式
				if len(subject) > 30:
					emailname = subject[:30]
				else:
					emailname = subject

				# 用户存储目录，用于存储邮件html文件
				dir = "data/%s" % self.emailInfo['email']

				if not os.path.exists(dir):
					os.makedirs(dir)
					dir = dir + "/%s.html" % emailname
					with open(dir, 'wb') as f:
						f.write(content.encode('utf-8'))
				else:
					dir = dir + "/%s.html" % emailname
					with open(dir, 'wb') as f:
						f.write(content.encode('utf-8'))


			else:
				dir = "data/%s" % self.emailInfo['email']
				if len(subject) > 30:
					emailname = subject[:30]
				else:
					emailname = subject
				# 若含有附件,则以邮件名创建附件文件夹
				sonDir = dir + "/%s"%emailname
				print('有附件啦')
				filename = msg.get_filename()
				if filename:
					# h = email.Header.Header(filename)
					dh = decode_header(filename)
					fname = dh[0][0]

					# print(fname)
					# print(type(fname))

					charset = chardet.detect(fname)['encoding']
					fname = fname.decode(charset)
					# print(fname)
					# print(type(fname))
					# fname = fname.replace('/', '_')

					data = msg.get_payload(decode=True)

					if not os.path.exists(sonDir):
						os.makedirs(sonDir)
						sonDir = sonDir + "/%s" % fname
						with open(sonDir, 'wb') as f:
							f.write(data)
					else:
						sonDir = sonDir + "/%s" % fname
						with open(sonDir, 'wb') as f:
							f.write(data)
				else:
					print("附件没名字？？")