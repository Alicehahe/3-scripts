#coding:utf-8
import selenium
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

url = 'http://192.168.11.102:6085/app/#/home'
count = 'hanlu'
pwd = '123'

def login_test():
    deep = webdriver.Chrome()
    deep.get(url)
    sleep(5)

    account = deep.find_element_by_id('login-username')
    account.clear()
    sleep(3)
    account.send_keys(count)

    apwd = deep.find_element_by_id('login-password')
    apwd.clear()
    sleep(3)
    apwd.send_keys(pwd)
    deep.find_element_by_css_selector('button[class="btn btn-primary login-btn"]').click()
    deep.find_element_by_css_selector('div[class="toolbtn flow"]').click()
    deep.find_element_by_name('search').send_keys('web') 
    deep.find_element_by_class_name('diradmin_srchcom').click()
    webtest = deep.find_element_by_css_selector('span[title="webtest"]')
    ActionChains(deep).context_click(webtest).perform()

if __name__ == '__main__':
    login_test()
    
