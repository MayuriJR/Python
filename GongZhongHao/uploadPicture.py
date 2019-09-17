#encoding utf-8
import os 
import time
from basic import Basic
class Upload_other_modes(object):
	def __init__(self,name,accessToken):
		self.name=name
		self.accessToken=accessToken
	def uploadPicture(self):
		try:
			command="curl \"https://api.weixin.qq.com/cgi-bin/material/add_material?access_token=%s&type=image\" -F media=@%s -F  description=\'{\"title\":\"VIDEO_TITLE\", \"introduction\":\"INTRODUCTION\"}\'"%(self.accessToken,self.name)
			reMsg=os.popen(command)  # use systeem operation to upload the models to the weixin service 
			mediaMsg=reMsg.read()
			print(mediaMsg)
			with open("Media_pricture.log","a+")as f:
				f.write("%s:\t%s\n\n"%(self.name,mediaMsg))
				f.close()
		except Exception as e:
			print(e)
if __name__=="__main__":
	model_name="pic_02.jpg"
	accessToken = Basic().get_access_token()
	myload=Upload_other_modes(model_name,accessToken)
	myload.uploadPicture()
