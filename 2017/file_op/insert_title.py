#!/usr/bin/env python3
#coding:utf-8
#在文件的开始位置插入字符串

with open("file_test.md", 'r+') as fp:
    #将内容暂存
    tmp = fp.read()
    fp.seek(0)  #将文件头移动到文件开始位置
    fp.write("haha\n" + tmp)

print("write sucess")
