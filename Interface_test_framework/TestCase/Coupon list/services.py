#coding:utf-8
'''
function:获取用户绿色通道的券列表
Precondition：用户已经购买了绿色通道服务
write on：2019-02-19 by hanlu
Request method：Get
'''
import requests
import json

PATH = 'https://staging.hshield.com.cn'

def Get_User_GreenChannel_Ticket_list():
    url = PATH  + '/api/reserve/services'
    head = {
        'Authorization': 'bearer b12e2ddb-758e-4d5b-b1b4-d792619bc0a8'
    }
    res = requests.get(url=url,headers=head)
    return res

if __name__ == '__main__':
    result = Get_User_GreenChannel_Ticket_list()
    result_json = result.json()
    print('api status code is {}'.format(result.status_code))
    print('user tickets list is {}'.format(json.dumps(result_json,indent=2,ensure_ascii=False)))
