#coding:utf-8
import requests
import bs4
from bs4 import BeautifulSoup

def getHtmlText(url):
    #获取html文档
    try:
        res = requests.get(url)
        res.raise_for_status()
        res.encoding=res.apparent_encoding
        return res.text
    except:
        return 'error'

def fillUnivList(ulist,html):
    #提取网页内容 找到合适的数据结构
    soup = BeautifulSoup(html,'html.parser')
    for tr in soup.find('tbody').children:
        try:
            if isinstance(tr,bs4.element.Tag):
                tds = tr('td')
                ulist.append([tds[0].string,tds[1].string,tds[3].string])
        except AttributeError:
            return 'error'

def printUnivList(ulist,num):
    #利用数据结构展示并输出
    print("{:<10}\t{:<6}\t\t{:<15}".format("排名","学校","总分"))
    for i in range(num):
        u = ulist[i]
        print("{:<10}\t{:<6}\t{:<10}".format(u[0], u[1], u[2]))

def main():
    uinfo=[]
    url = 'http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html'
    html = getHtmlText(url)
    fillUnivList(uinfo,html)
    printUnivList(uinfo,100)   #print first 20 school


if __name__ == '__main__':
    main()