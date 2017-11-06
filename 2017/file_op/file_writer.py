#!/usr/bin/env python3
#coding:utf8

with open("file_test.md", 'w') as fp:
    fp.write("ok,大黑哥\n")
    fp.write("sssok\n")
    fp.write("1233\n")

# 追加内容a
with open("pi_dig.md", 'a') as fp:
    fp.write("ok,大黑哥\n")
    fp.write("sssok\n")
    fp.write("1233\n")

print("success")
