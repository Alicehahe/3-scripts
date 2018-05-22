#coding:utf-8
#!/usr/bin/python
import requests
url = "http://news.sina.com.cn/china/"
def getHtml(url):
    try:
        res= requests.get(url)
        print res.status_code
        res.encoding = res.apparent_encoding
        return res.text
    except:
        print "error"
        
print getHtml(url)

    
    
