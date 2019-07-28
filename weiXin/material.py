# encoding utf-8
# filename: material.py
import urllib
from urllib import request
import json
from basic import Basic
import time

class Material(object):
    #upload picture and picture
    def add_news(self, accessToken, news):
        postUrl = "https://api.weixin.qq.com/cgi-bin/material/add_news?access_token=%s" % accessToken
        urlResp = request.urlopen(postUrl, news)
        print(urlResp.read())
    #query all url from weixin official plane ,offset 0 means first news in planet,count 20 means less than 20 article will expose
    def batch_get(self, accessToken, mediaType, offset=0, count=20):
        postUrl = "https://api.weixin.qq.com/cgi-bin/material/batchget_material?access_token=%s" % accessToken
        postData = "{ \"type\": \"%s\", \"offset\": %d, \"count\": %d }" % (mediaType, offset, count)
        try :
            urlResp = urllib.request.urlopen(postUrl, postData.encode())
        except Exception as e:
            print("___________________________________________")
            print (e)
        myFile=urlResp.read().decode("utf-8")
        cls_myFile=json.loads(myFile)
        print(cls_myFile["item"][0]["content"]["news_item"][0]["url"])
        cls_myFile_addr=(cls_myFile["item"][0]["content"]["news_item"][0]["url"])
        with open("article_addr.log","a+") as f:
            addrInfo="%s:\t%s\n"%(offset+1,cls_myFile_addr)
            f.write(addrInfo)
            f.close()

if __name__ =="__main__":
    myMaterial = Material()
    accessToken = Basic().get_access_token()
    news =(
    {
        "articles":
        [
            {
            "title": "监测成果展示",
            "thumb_media_id":"GaPzKNuTF8_BZn7MtCZzzmG6vy0JcZdgdopghQeRrgQ",
            "author": "mayuri",
            "digest": "",
            "show_cover_pic": 1,
            "content": "<p><img src=\"./pic.02\" /><br/><h1>监测成果</h1><br/>&nbsp&nbsp（1）在延安宝塔区气象局南侧斜坡上开展降雨入渗的原位监测工作，设置3-5个监测断面，每个断面设置3-8个监测点，每个监测点设置3-8个水分传感器，将这些传感器通过物联网技术进行组网形成一套完善的降入入渗现场监测网络。<br/>&nbsp&nbsp（2）在延安“黄土崩滑灾害—陕西延安野外基地”已有监测点中典型滑坡灾害点，补充土壤水分传感器。通过物联网技术将这些水分传感器，纳入降入入渗现场监测网络。<br/>&nbsp&nbsp（3）在延安宝塔区气象局南侧斜坡增加一套TLERT装置，监测降雨过程中土壤电阻率剖面变化，结合传感器数据揭示斜坡地带降雨入渗过程<br/><img src=\"./pic.03></p>",
            "content_source_url": "",
            }
        ]
    })
    #news is a dic components，you can change it by following contents:
    #news['articles'][0]['title'] = u"mayuri".encode('utf-8')
    #temp=json.dumps(news,ensure_ascii=False)  #json to change dic to a str
    #myMaterial.add_news(accessToken, temp.encode())
    #time.sleep(5)
    #accessToken = Basic().get_access_token()
    mediaType="news"
    myMaterial.batch_get(accessToken, mediaType)
