#!/usr/bin/python
import random
'''a=0
try:
    a
except NameError,e:
    print "exec over",e

print "it's ok"'''

'''try:
    if a:
except:
    print "catc error"'''

'''try:
    undef
except IOError,e:
    print "catch",e'''


num = random.randint(0,100)

while True:
    try:
        guess = int(raw_input("Enter a num (1~100:)"))
    except ValueError,e:
        print "please enter a right num:"
        continue
    if guess > num:
        print "big",guess
    elif guess < num:
        print "small",guess
    else:
        print "OK"
        break
    print "\n"
