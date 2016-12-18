#!/usr/bin/python
# -*- coding: utf-8 -*-

import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class SendMail():
	def __init__(self, parent=None, From = None, pwd = None, smtp_server = None):
		self.msg = MIMEMultipart('alternative')
		self.msg['From'] = From
		self.pwd = pwd
		self.smtp_server = smtp_server
		
	def Send(self):
		try:
			self.msg.attach(MIMEText(self.msg['plain'], 'plain', 'utf-8'))
			self.msg.attach(MIMEText(self.msg['html'], 'html', 'utf-8'))

			server = smtplib.SMTP_SSL(self.smtp_server,465)
			# server.starttls()
			server.set_debuglevel(1)
			server.login(self.msg['From'],self.pwd)
			server.sendmail(self.msg['From'],self.msg['To'],self.msg.as_string())
			server.quit()

		except Exception as e:
			raise e

			
			