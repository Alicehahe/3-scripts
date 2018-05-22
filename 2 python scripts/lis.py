#coding:utf-8
#!/usr/bin/python
from pypinyin import lazy_pinyin
char=0
lis = [u'全文', u'入院记录', u'首次病程', u'日常病程', u'上级医师查房记录', u'术前小结']
a = lazy_pinyin(lis)
print a


