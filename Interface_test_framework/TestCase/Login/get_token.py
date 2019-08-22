#coding:utf-8
'''
function:用户登录获取token
Precondition：用户已经注册、
write on：2019-02-19 by hanlu
Request method：Post
'''
import requests
import json

globals()['PATH'] = 'https://staging.hshield.com.cn'


def Login_Get_User_Token(url,head,data):
    '用户登录需要url headers data参数传入'
    '''url = PATH + '/api/uaa/oauth/token'
    head = {
        'content-type':'application/x-www-form-urlencoded'
    }
    data = {
        'client_id': 'ua',
        'grant_type': 'onetime',
        'mobile': '17316326189',
        'token': '123456'
    }'''
    res = requests.post(url=url, headers=head, data=data)
    return res

'''if __name__ == '__main__':
    result = Login_Get_User_Token()
    '利用json函数格式化成字典格式，键值对方式取参'
    print('user login success,status_code is {}'.format(result.status_code))
    print('result.text type is {}'.format(type(result.text)))
    print('user login in success ,access_token is {}'.format(result.json()['access_token']))
    print('post url is {}'.format(result.url))'''