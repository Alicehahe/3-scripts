#coding:utf-8
import requests
import bs4
from bs4 import BeautifulSoup

header = {'User-Agent': 'Mozilla/5.0'}
kv = {
        "query":"测试工程师",
        "scity":"101020100",
        "position":"100301",
        "industry":""
    }
url = 'https://www.zhipin.com/job_detail/'
job_name=[]
job_salary=[]
job_detail=[]
def get_one_page(url=url,params=kv,headers=header):
    #获取html文档
    respone = requests.get(url=url,params=kv,headers=header)
    try:
        if respone.status_code == 200:\
            return respone.text
    except:
        #返回请求url的headers
        print('error')

def Extract_Date(html):
    #提取数据
    soup = BeautifulSoup(html, 'html.parser')
    #print(soup.prettify())
    print('{:<10}\t{:<12}\t\t{:<15}\t\t{:<10}'.format('城市', '岗位名称', '薪资范围','岗位详情'))
    for div in soup.find_all('div',class_='info-primary'):
        if isinstance(div,bs4.element.Tag):
            name = div.find('div',class_='job-title')
            job_name = name.string
            job_salary = div.find('span').string
            job_detail = div.find('p').text
            job_address = job_detail[3:]
            city = job_detail[0:2]
            print('{:<10}\t{:<12}\t\t{:<15}\t\t{:<10}'.format(city,job_name,job_salary,job_address))




            #job_salary= div('span'))

def main():
    city = None
    html = get_one_page()
    Extract_Date(html)


if __name__ == '__main__':
    main()