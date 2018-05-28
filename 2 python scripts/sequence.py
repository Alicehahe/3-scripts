#coding:utf-8
s=input('输入你的想要去除首尾空格的字符串:')

'''begin=0 #开始搜索空格
end=-1  #结尾搜索空格
print(len(string))

def temp(string):
 #   len(string)
    for i in range(len(string)):
     print(i)
        if string[0:i+1] == ' ':
            continue
        else:

         i+=1
'''

def trim(s):
    while s[:1] == ' ':
        print(s)
        s = s[1:]
    while s[-1:] == ' ':
        s = s[:-1]

    return s,len(s)
print(trim(s))


