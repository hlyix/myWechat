import hashlib
import web
import receive
import reply
import deal
import tool_mysql_apply
import json

class Handle(object):
    def GET(self):
        try:
            data = web.input()
            if len(data) == 0:
                return "hello, this is handle view"
            signature = data.signature
            timestamp = data.timestamp
            nonce = data.nonce
            echostr = data.echostr
            token = "hnu2019" #请按照公众平台官网\基本配置中信息填写
            list = [token, timestamp, nonce]
            list.sort()
            str_list1 = ''.join(list)
            print(str_list1)
            sha1 = hashlib.sha1()
            sha1.update(str_list1.encode('utf-8'))
            hashcode = sha1.hexdigest()
            print("handle/GET func: hashcode, signature: ", hashcode, signature)
            if hashcode == signature:
                return echostr
            else:
                return ""
        except Exception as Argument:
            return Argument

    def POST(self):#被动回复
     try:
        webData = web.data()#type(webData)=bytes
        # print("Handle Post webdata is ", webData)#打印xml字节流
        recMsg = receive.parse_xml(webData) #type(recMsg)=【receive.TextMsg】or【receive.ImageMsg】or【NoneType】
        if isinstance(recMsg, receive.Msg):#type(recMsg)不为NoneType
            toUser = recMsg.FromUserName
            fromUser = recMsg.ToUserName
            createTime=recMsg.CreateTime
            if recMsg.MsgType == 'text':
                content = deal.dealTxt(toUser,createTime,recMsg.Content)
            elif recMsg.MsgType == 'image':
                content = "已收到图片"
            elif recMsg.MsgType == 'video':
                content = "已收到视频"
            elif recMsg.MsgType == 'voice':
                content = "已收到语音"
            elif recMsg.MsgType == 'link':
                content = "已收到链接"
            elif recMsg.MsgType == 'location':
                longitude=str(webData).split('<Location_Y>')[1].split('</Location_Y>')[0]
                latitude=str(webData).split('<Location_X>')[1].split('</Location_X>')[0]
                print(longitude,latitude)
                tool_mysql_apply.updateUser('longitude', longitude, 'wcid', toUser)
                tool_mysql_apply.updateUser('latitude', latitude, 'wcid', toUser)
                content = "已更新您的位置"
            else:
                content = recMsg.MsgType
            replyMsg = reply.TextMsg(toUser, fromUser, content)
            # test 打印用户特征 (影响速度)
            usrdf = tool_mysql_apply.getUser(toUser)
            if (usrdf.__len__() > 0):
                userdt = eval(usrdf.ix[0][3])
                print(json.dumps(userdt, sort_keys=False, indent=4, ensure_ascii=False))
            return replyMsg.send()
        else:#type(recMsg)为NoneType
            print("NoneType")
            return "success"
     except Exception as e:
            print('e-->', e)
            return e
