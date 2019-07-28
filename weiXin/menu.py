# encoding utf-8
# filename: menu.py
import urllib
from urllib import request
from basic import Basic
import json

class Menu(object):
    def __init__(self):
        pass
    def create(self, postData, accessToken):
        postUrl = "https://api.weixin.qq.com/cgi-bin/menu/create?access_token=%s" % accessToken
        if isinstance(postData,str):
            postData = postData.encode("utf-8")
        urlResp = urllib.request.urlopen(postUrl, postData)
        print(urlResp.read())

    def query(self, accessToken):
        postUrl = "https://api.weixin.qq.com/cgi-bin/menu/get?access_token=%s" % accessToken
        urlResp = urllib.request.urlopen(postUrl)
        print (urlResp.read())

    def delete(self, accessToken):
        postUrl = "https://api.weixin.qq.com/cgi-bin/menu/delete?access_token=%s" % accessToken
        urlResp = urllib.request.urlopen(postUrl)
        print (urlResp.read())

    #obtain self menu config 
    def get_current_selfmenu_info(self, accessToken):
        postUrl = "https://api.weixin.qq.com/cgi-bin/get_current_selfmenu_info?access_token=%s" % accessToken
        urlResp = urllib.request.urlopen(postUrl)
        print (urlResp.read())

if __name__ == '__main__':
    myMenu = Menu()
    postJson = """
    {
        "button":
        [
            {
                "type": "click",
                "name": "降雨资料",
                "key":  "mpGuide"
            },
            {
                "name": "监测平台",
                "sub_button":
                [
                    {
                        "type": "view",
                        "name": "宝塔山简介",
                        "url": "http://mp.weixin.qq.com/s?__biz=MzIxMDU3MDExOA==&mid=100000005&idx=1&sn=4df9a36339a6103f69b267d2d43a2058&chksm=1763dfec201456fa968dd964e383b2f468b49a721d213668e1397a816cbdacf889361e25066b#rd"
                    },
                    {
                        "type": "view",
                        "name": "监测内容",
                        "url":"http://mp.weixin.qq.com/s?__biz=MzIxMDU3MDExOA==&mid=100000019&idx=1&sn=2bcc9b73381fb84565fac05fa5b56fa0&chksm=1763dffa201456ec043bdaf97dc77b499155f1a08bbcb009bd3f56264f33e695e724f3b4a426#rd"
                    }
                ]
            }
				
          ]
    }
    """
    accessToken = Basic().get_access_token()
    #myMenu.delete(accessToken)
    myMenu.create(postJson,accessToken)
    #myMenu.query(accessToken)
