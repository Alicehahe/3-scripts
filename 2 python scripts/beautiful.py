#coding:utf-8
#!/usr/bin/python

import bs4 

soup = BeautifulSoup(demo,"html.parser")
print soup.head
print soup.head.contents
