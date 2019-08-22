#coding:utf-8
'''
功能：将测试用例中请求数据封装成json文件
操作：将用例中请求数据写成字典的key值，json文件中将key值和value对应去读取
modules：json模块操作json文件
主要流程：
1.打开文件，获取具柄,并加载json文件
with open(file_path) as fp:
    data= json.load(fp)       #获得json文件数据
2.json文件内容以字典格式存放，以字典的key值读取
data[key]
'''
import json
'''
获得json文件具柄，打开文件
fp = open('/Users/qingjiao/Desktop/login.json')

#加载json文件
data = json.load(fp)

#通过key值打印出对应的value值
print(data['register'])'''

class Operation_Json:
    def __init__(self,file_path=None):
        if file_path:
            self.file_path = file_path
        else:
            self.file_path = '/Users/qingjiao/Desktop/login.json'
        #使用open()函数，需要手动配合写fp.close()函数，python中用with open() as fp:读取结束后会自动关闭文件
        with open(self.file_path) as fp:
            self.data = json.load(fp)

    #根据关键字获取对应value值
    def get_key_value(self,key):
        return self.data[key]


if __name__ =='__main__':
    opers = Operation_Json()
    print(opers.get_key_value('register'))