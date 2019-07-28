#encoding utf-8
#filename:handle.py
import hashlib
import web
import reply
import receive
import text 
class Handle(object):
    def GET(self):
       try:			
            data = web.input()
            print(data)
            if len(data)==0:
                return "hello, this is mayuri's web view"
            signature = data.signature
            print(signature)
            timestamp = data.timestamp
            nonce = data.nonce
            echostr = data.echostr
            token ="baotashan"
            list = [token, timestamp, nonce]
            list.sort()
            sha1 = hashlib.sha1()
            sha1.update(list[0].encode("utf-8"))
            sha1.update(list[1].encode("utf-8"))
            sha1.update(list[2].encode("utf-8"))
            hashcode = sha1.hexdigest()
            if hashcode == signature:
                return echostr
            else:
                return ""
       except Exception as e:
            return e
    def POST(self):
        try:
            webData = web.data()
            print ("Handle Post webdata is %s "%webData)
            recMsg = receive.parse_xml(webData)
            if isinstance(recMsg, receive.Msg): 
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                if recMsg.MsgType == 'text':
                    reContent=recMsg.Content.decode('utf-8')
                    content="您好！点击 降雨资料可以获得延安是最近的降雨量！点击监测平台查看其他资料！"
                    replyMsg = reply.TextMsg(toUser, fromUser, content)
                    return replyMsg.send()
                elif recMsg.MsgType == 'image':
                    mediaid=recMsg.MediaId
                    replyMsg = reply.ImageMsg(toUser, fromUser,mediaid) 
                    return replyMsg.send()
            elif isinstance(recMsg,receive.EventMsg):
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                if recMsg.Event=="CLICK":
                    if recMsg.Eventkey =="mpGuide":
                        myText=text.Text()
                        content=myText.getWeather("yanan")
                        replyMsg = reply.TextMsg(toUser, fromUser, content)
                        return replyMsg.send()
        except Exception as Argment:
            print(Argment)
            print("___________________________________________")
            return Argment
            print("_"*40)

