# encoding utf-8
# filename: media.py
from urllib import request
import urllib
import json
from basic import Basic


class Media(object):
    def get(self, accessToken, mediaId):
        postUrl = "https://api.weixin.qq.com/cgi-bin/media/get?access_token=%s&media_id=%s" % (accessToken, mediaId)
        print(postUrl)
        urlResp = request.urlopen(postUrl)
        try:
            buffer = urlResp.read()   #components in binary
            with open (r"./mygodness.jpg","wb+") as f:
                f.write(buffer)
            print("get successful")
        except Exception as e:
            print(e)
if __name__ == "__main__":
    myMedia = Media()
    accessToken = Basic().get_access_token()
    print(accessToken)
    mediaId = "CSYiU9OyZw-XEZXv1H12FEubAn923agpJVmEk-bKxvyntSQP6NgaZA1g_0AOgS3S"
    myMedia.get(accessToken, mediaId)
    with open("temp.txt","a+")as f:
        content=accessToken+"\n"
        f.write(content)
        f.close()
