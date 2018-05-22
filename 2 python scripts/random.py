#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
num = int(raw_input("请输入一个整数数字:") )
def num_get(num):
    num2 = random.randint(1,10)
    while True:
        if num == num2:
            print "OK,is right"
            break
        else:
            print "again"
            num = int(raw_input("请输入一个整数数字:") )
    
num_get(num)
