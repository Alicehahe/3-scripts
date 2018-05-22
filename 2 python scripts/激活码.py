#coding:utf8
#!/usr/bin/python
#activation code
import random,string
def rand_str(num,length):
    #打开文件易只写的方式，文件如果不存在就创建
    f = open("rand.txt",'w')
    #外层决定生成多少个激活码
    for i in range(num):
        #生成a-z A-Z 0-9字符串
        cha = string.ascii_letters + string.digits
        #random.choice（）每个取一个随机数，后面循环几次，就生成几位数的随机数
        s = [ random.choice(cha) for i in range(length)]
        #格式化写进文件
        f.write('{0}\n'.format(''.join(s)))
    f.close()

if __name__ == '__main__':
    rand_str(200,8)
    
