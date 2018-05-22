#coding:utf-8

from selenium import  webdriver
from time import sleep
#Chrome可以填写chromedriver的地址(r'E;/test/'),默认放在python2.7里
driver = webdriver.Chrome()
driver.get('http://121866.com')

web_elemnt = driver.find_element_by_class_name('content2')
web_elemnt.click()
sleep(3)

login_name = driver.find_element_by_id('username')
login_name.clear()
login_name.send_keys('12345698')

login_passwd = driver.find_element_by_id('password')
login_passwd.clear()
login_passwd.send_keys('123456')

button = driver.find_element_by_id('btn_sign')
button.click()
#我的浏览器加载该元素较慢，需要加上等待时间，等其加载出来，才能定位
sleep(5)
usrname = driver.find_element_by_id('username').text
print usrname

sleep(2)
#判断用户名是否正确
if '123' in usrname:
    print 'login success'
else:
    print 'login error'

sleep(5)
print 'waiting,is closing... '
driver.quit()
