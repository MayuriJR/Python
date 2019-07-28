# encoding utf-8
# filename: basic.py
import urllib
from urllib import request
import time
import json
class Basic:    
	def __init__(self):        
		self.__accessToken = "23_7JjE3UFo8SxmZ23PbmLE7pc0PdtCujQ1dXvRyuNbYhBw7JTRLKULQg7EHTZRmBtmNF1FwDmSNcR0BOyIooSrY9YWiaWKdiXvOJfvFa3SD_sb2YhRV-37R_ZE3yJdOlkkoEDVcIPXpS-wo_bGANWiACAIVE"
		self.__leftTime = 0    
	def __real_get_access_token(self):        
		appId = "wx845a5772c5d1c93d"        
		appSecret = "132c318d74ca580884ea31edcdfb225c"
		postUrl = ("https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s" % (appId, appSecret))        
		urlResp = request.urlopen(postUrl)        
		urlResp = json.loads(urlResp.read())                
		self.__accessToken = urlResp['access_token']        
		self.__leftTime = urlResp['expires_in']    
	def get_access_token(self):        
		if self.__leftTime < 10:            
			self.__real_get_access_token()        
			return self.__accessToken    
	def run(self):        
		while(True):            
			if self.__leftTime > 10:                
				time.sleep(2)                
				self.__leftTime -= 2            
			else:                
				self.__real_get_access_token()
if __name__=="__main__":
	testBasic=Basic()
	accessToken=testBasic.get_access_token()
