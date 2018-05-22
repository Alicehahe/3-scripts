#!/usr/bin/env python  
#coding: utf-8
  
import urllib2  
import re  
import json  
  
class Youdao:  
    def __init__(self):  
        self.url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule&sessionFrom='  
        self.key = '5c8c71f49e0c0825' #有道API key  
        #self.keyfrom = 'nicomochina' #有道keyfrom
        self.keyfrom = 'fanyi.web'
        
    def get_translation(self,words):  
        url = self.url + '?keyfrom=' + self.keyfrom + '&key='+self.key + '&type=data&doctype=json&version=2.1&q=' + words  
        result = urllib2.urlopen(url).read()
        json_result = json.loads(result)
        print json_result
        #json_result = json_result["translation"]  
        #for i in json_result:  
        #    print i  
  
youdao = Youdao()  
while True:
    msg=raw_input('请输入单词\句子（输入quit结束）:')  
    if msg == 'quit':  
        break  
    youdao.get_translation(msg)  
