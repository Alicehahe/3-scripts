#coding:utf-8
#!/usr/bin/python
import urllib

#返回reponse对象
reponse = urllib.urlopen("http://placekitten.com/")
print reponse.getcode()
cat = reponse.read()

#图片是二进制的，所以二进制的方式写入
with open("cat.jpg","wb") as f:
    f.write(cat)
