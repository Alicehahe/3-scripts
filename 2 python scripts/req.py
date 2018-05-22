#coding:utf-8
#!/usr/bin/python

import requests

re = requests.get("http://bbs.chinaunix.net/")
print re.status_code
print re.encoding
#解决乱码问题
print re.apparent_encoding
#可以看到re是reponse类
print type(re) 
print re.text
