#coding:utf-8
import os

def file_name(file_dir):
    L=[]
    S=[]
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.mp4':
                L.append(os.path.join(root, file))
    S ='\n'.join(L)
    return S

print(file_name('/Users/qingjiao/Downloads'))