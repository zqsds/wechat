#encoding:utf-8
import itchat
from itchat.content import TEXT
from itchat.content import *
import sys
import time
import re

import os
msg_information = {}
face_bug = None

'''
    @todo 收到发送人的消息
'''
@itchat.msg_register(TEXT)
def simple_reply(msg):
    itchat.send(u'已经收到了文本消息，消息内容为%s'%msg['Text'],toUserName=msg['FromUserName'])
    print(msg)

'''
    @todo 转发收到的消息至图灵机器人
'''

'''
    @todo 图灵机器人的返回的消息转发给发来人的
'''

if __name__ == '__main__':
    itchat.auto_login(hotReload=True,enableCmdQR=2)
    itchat.run()