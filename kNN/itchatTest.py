#encoding:utf-8
import itchat
import requests
from itchat.content import TEXT
from itchat.content import *
import sys
import time
import re

import os
msg_information = {}
face_bug = None

#自动把各种聊天内容发给微软小冰isXiaobingChat的小程序（附带图灵机器人和小冰聊天isTuling）
isTuling,isXiaobingChat= True ,True
def get_response(msg):
    Url = "http://www.tuling123.com/openapi/api"
    data = {
        'key'  :  '603b728dce3340e4b0ac7f8cee17cb80', #这个key可以直接拿来用，随便用，无所谓，放心公开
        'info'  : msg,
        'userid' : 'pth-robot',
    }
    try:
        r = requests.post(Url,data=data).json()
        print("r1--------------")
        print(r)
        print("r2--------------------")
        return r.get('text')
    except:
        return


@itchat.msg_register(TEXT)
def tuling_reply(msg):
    reply = get_response(msg['Text'])
    return reply or 'I received: ' + msg.get('Text')

# 微信好友发来的内容isFriendChat=True, 群聊发来的内容isGroupChat=True, 公众号发来的内容isMpChat=False
isFriendChat, isGroupChat , isMpChat=True,False,True



@itchat.msg_register(TEXT,isFriendChat=isFriendChat, isGroupChat=isGroupChat, isMpChat=isMpChat)
def reply_msg(msg):
    itchat.send(tuling_reply(msg),toUserName=msg['FromUserName'])




if __name__ == '__main__':
    itchat.auto_login(hotReload=True,enableCmdQR=2)
    itchat.run()