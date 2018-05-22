#coding:utf8
#!/usr/bin/python
num = 0
def word_count(txt):
    #打开文件并且读取
    f = open(txt,'r').read()
    #将文本中逗号替换
    tmp = f.replace(',','')
    #以空格分隔开
    string = tmp.split(' ')
    return string

for i in word_count('eng.txt'):
    #print i
    num += 1
print("the all word num is:",num)
