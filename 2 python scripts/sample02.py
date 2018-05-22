#coding:utf-8
from selenium import webdriver
from time import sleep


driver = webdriver.Chrome()
driver.get('http://192.168.11.102:6091/app/#/')

ele = driver.find_element_by_id("login-username")
print ele.text



ele.quit()
