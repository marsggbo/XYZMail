from DealJsonFile import GetJsonInfo, SaveJsonInfo
import threading,time,os,re
from multiprocessing import Process

class Search():
	def __init__(self):
		self.islock = True  # 锁住

	def run(self,userInfo=None,mode=None,keyword=None):
		self.userInfo = userInfo
		print(userInfo)
		print(mode)
		print(keyword)
		if mode == '主题':
			print('主题搜索')
			self.result = self.searchSubject(keyword)
			self.islock = False  # 解锁
		elif mode == '联系人':
			print('联系人搜索')
			self.result = self.searchName(keyword)
			self.islock = False  # 解锁
		elif mode == '时间':
			print('时间搜索')
			self.result = self.searchDate(keyword)
			self.islock = False  # 解锁
		elif mode == '邮件内容':
			print('邮件内容搜索')
			self.result = self.searchSubject(keyword)
			self.islock = False  # 解锁

	# 返回结果
	def getResult(self):
		# print("获取结果")
		while not self.islock:
			return self.result

	# 搜索主题
	def searchSubject(self,subject):
		dir = 'data/%s'%(self.userInfo['email'])
		contacts = GetJsonInfo('contacts.json')
		files = {}
		subject = subject.lower()
		if os.path.exists(dir):
			for file in os.listdir(dir):
				if os.path.isfile(os.path.join(dir, file)):
					if subject in file.lower():
						file = file.replace('.html','')
						if file in contacts:
							files[file] = contacts[file]
		return files

	# 搜索邮件内容
	def searchEmailContent(self,content):
		content = re.compile(content)
		dir = 'data/%s'%(self.userInfo['email'])
		contacts = GetJsonInfo('contacts.json')
		abDir = os.path.abspath(os.path.join(os.path.dirname(__file__))).replace('\\','/') + "/%s"%dir
		files = {}
		if os.path.exists(dir):
			for file in os.listdir(dir):
				if file[-4:] == 'html':
					fileDir = "%s/%s"%(abDir,file)
					with open(fileDir,'rb') as f:
						emailContent = f.read().decode('utf-8')
						if len(content.findall(emailContent))>0:
							files[file] = contacts[file]
		return files

	# 搜索邮件地址
	def searchEmailAddr(self,email):
		contacts = GetJsonInfo('contacts.json')
		files = {}
		temp = email.lower()
		for item in contacts:
			if temp in contacts[item]['fromAddr'].lower():
				files[item] = contacts[item]
		return files

	# 搜索联系人
	def searchName(self,name):
		contacts = GetJsonInfo('contacts.json')
		files = {}
		temp = name.lower()
		for item in contacts:
			if temp in contacts[item]['name'].lower():
				files[item] = contacts[item]
		return files

	# 搜索时间
	def searchDate(self,date):
		contacts = GetJsonInfo('contacts.json')
		files = {}
		temp = date.lower()
		for item in contacts:
			if temp in contacts[item]['date'].lower():
				files[item] = contacts[item]
		return files

if __name__ == "__main__":
	# test
	userInfo={'email':"1435679023@qq.com"}
	mode=['主题',"时间","联系人","邮件内容"]
	keyword="lear"

	# 搜索模块测试
	try:
		start = time.time()
		begin = time.time()
		test = Search()
		p1 = threading.Thread(target=test.run, args=[userInfo,mode[3],keyword])
		p1.start()
		p1.join()
		files1 = test.getResult()
		while files1==None:
			files1 = test.getResult()
		print("1",files1)
		print("耗时多线程1：",time.time()-begin)


		begin = time.time()
		test = Search()
		test.run(userInfo,mode[3],keyword)
		files2 = test.getResult()
		while files2==None:
			files2 = test.getResult()
		print("2",files2)
		print("耗时啥都不用2：",time.time()-begin)
		#
		print("总耗时:",time.time()-start)
	except Exception as e:
		print(str(e))



