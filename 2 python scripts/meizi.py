#coding:utf-8
#!/usr/bin/python
import urllib
import os
import re

def get_page(url):
    #req.add_header('Uesr-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36')
    req = urllib.urlopen(url)
    html = req.read().decode('utf-8')
    return html
    

def find_image(url):
    pass
def save_image(folder,img_addrs):
    pass

def down_mm(folder='ooxx',page=30):
    #创建文件夹
    os.mkdir(folder)
    os.chdir(folder)
    url = "http://jandan.net/ooxx"
    page_num = int(get_page(url))

    for var in range(page):
        page_num -= i
        page_url = url + 'page' + str(page_num) + '#comments'
        img_addrs = find_iamge(page_url)
        save_image(img_addrs)

if __name__ == "__main":
    down_mm()
