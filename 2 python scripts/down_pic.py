#coding:utf8
#!/usr/bin/python
import urllib
import re
url = "https://tieba.baidu.com/p/2365900464"

#下载页面
def getHtml(url):
    #返回一个page对象
    page = urllib.urlopen(url)
    #调用read方法
    html = page.read()
    return html

#分析上层返回的html，得到图片想要的结果
def getImage(html):
    #var = 0
    reg = r'src="(.*?\.jpg)" width'
    #complie是将正则编译，执行更快
    imgre = re.compile(reg)
    #找出和正则匹配的数据
    imglist = re.findall(imgre,html)
    x = 0
    for imgurl in imglist:
        urllib.urlretrieve(imgurl,"%s.jpg" % x)
        x += 1
    return imgurl
    
html = getHtml(url)
print getImage(html)
