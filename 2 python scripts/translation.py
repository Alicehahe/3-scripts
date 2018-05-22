#coding:utf-8
#!/usr/bin/python
import urllib
data = {}
data["appkey"] = "5c8c71f49e0c0825"
data["key"] = "5c8c71f49e0c0825"
data["q"] = "hello"
data["from"] = "AUTO"
data["to"] = "ATUO"
data["smartresult"] = 'dict'
data["doctype"] = 'json'
data["version"] = '2.1'
data["keyfrom"] = "fanyi.web"
data["typoResult"] = "true"
data["salt"] = "1501595720902"
data = urllib.urlencode(data)
print data


url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule&sessionFrom="
url = url + '?' +data
print urllib.urlopen(url).read()

 
    
