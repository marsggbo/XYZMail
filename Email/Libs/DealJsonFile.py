import json
import os


# def GetJsonInfo(file):
# 	if not os.path.exists(file):
# 		with open(file,'w',encoding='utf-8') as f:
# 			f.write('{}')
# 			s = {}
# 	else:
# 		with open(file,'r',encoding='utf-8') as f:
# 			s = json.load(f)
# 	return s
#
# def SaveJsonInfo(file,data):
# 	with open(file,'w',encoding='utf-8') as f:
# 		f.write(json.dumps(data))

#import json


def GetJsonInfo(file):
	f = open(file,'r',encoding='utf-8')
	s = json.load(f)
	f.close()
	return s

def SaveJsonInfo(file,data):
	f = open(file,"w",encoding='utf-8')
	f.write(json.dumps(data))
	f.close()