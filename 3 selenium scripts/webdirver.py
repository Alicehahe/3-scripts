#coding:utf-8
from selenium import webdriver
import time
browser = webdriver.Chrome()
browser.get("http://www.baidu.com")

print '浏览器最大化'
browser.maximize_window()
time.sleep(2)

print "调整浏览器比例为480,800"
browser.set_window_size(480,800)
time.sleep(2)

print "前进后退操作"
#访问百度首页
first_url = 'http://www.baidu.com'
print 'now access is %s' %(first_url)
browser.get(first_url)
time.sleep(5)

second_url = "http://news.baidu.com"
print "now is %s" %(second_url)
browser.get(second_url)
time.sleep(5)

print "back to %s" %(first_url)
browser.back()
time.sleep(5)

print "forward to %s" %(second_url)
browser.forward()
time.sleep(5)

browser.quit()

