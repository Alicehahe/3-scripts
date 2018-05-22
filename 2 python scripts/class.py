#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
#大数据分析平台
driver.get('http://192.168.1.183:6098/app/')

#最大化界面
#driver.maximize_window()

#登录平台,如果存在默认值，就删除默认值，传入新的参数就
driver.find_element_by_id("login-username").clear()
time.sleep(2)
driver.find_element_by_id("login-username").send_keys("root")
driver.find_element_by_id("login-password").clear()
time.sleep(2)
driver.find_element_by_id("login-password").send_keys("123")

#定位进入页面框
driver.find_element_by_tag_name("button").click()
#driver.find_element_by_tag_name("button").submit()


print '正在登录系统，请稍等...'
time.sleep(5)

#print "打开分析流目录"
#driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div/div/div[1]").click()
driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div/div/div[1]").click()
driver.find_element_by_xpath("/html/body/div[5]/div[3]/drawer-tree/div/div/div/div[2]/div[1]/div[1]/div/label/span").click()
driver.find_element_by_xpath("/html/body/div[5]/div[3]/drawer-tree/div/div/div/div[2]/div[1]/div[2]/div[4]/div[1]/div/label/span").click()
driver.find_element_by_xpath("/html/body/div[5]/div[3]/drawer-tree/div/div/div/div[2]/div[1]/div[2]/div[4]/div[2]/div[4]/div/div/label/span").click()
tmp = driver.find_element_by_class_name("outer drag-start")
ActionChains(driver).context_click(tmp).perform()

#driver.find_element_by_link_text("K线图").click()
#driver.find_element_by_xpath("//*[@id="jsPlumb_3_3"]/div/img").context_click()
#driver.find_element_by_class_name("right_a ng-binding").click()
#print '正在退出'
#driver.quit()
