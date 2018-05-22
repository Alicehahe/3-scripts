#coding:utf-8
#!/usr/bin/python
from selenium import webdriver
import time

browser = webdriver.Firefox()

#访问百度首页
first_url = 'http://www.baidu.com'
print "now is %s",first_url
browser.get(first_url)

#访问新闻页面
second_url = 'http://news.baidu.com'
print "now access %s",second_url
browser.get(second_url)

print "now is back"
browser.back()
time.sleep(5)
print "now is forward"
browser.forward()
#print "浏览器最大化"
#browser.maximize_window()
#调节界面480 800界面大小
#browser.set_window_size(480,800)
time.sleep(5)
browser.quit()
