#coding:utf-8
import os
print(os.getcwd())

with open('teacher_course.txt',encoding='utf8') as f,open('teacher.txt',encoding='utf8') as f1,open('student.txt') as f2:
    print(f1.read())
