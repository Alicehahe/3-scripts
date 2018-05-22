#coding:utf-8
from selenium import webdriver
broswer = webdriver.Chrome()
c = broswer.get('http://192.168.11.102:6088/app/#/')
broswer.maximize_window()
broswer.find_element_by_id('login-username').send_kyes('hanlu')

