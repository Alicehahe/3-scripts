#coding:utf-8
from selenium import webdriver



#browser = webdriver.Chrome()
#browser.get("http://www.baidu.com")

#browser.find_element_by_id("kw").send_keys("selenium")
#browser.find_element_by_id("su").click()

#browser.quit()
import selenium
from selenium import webdriver
from time import sleep

username="hanlu"
pwd = 123
b = webdriver.Chrome()
b.get("http://192.168.11.102:6085/app/#")


b.find_element_by_id("login-username").send_keys(username)
b.find_element_by_id("login-password").send_keys(pwd)
b.find_element_by_css_selector("button[class:btn btn-primary login-btn]").click()
sleep(3)


b.quit()
