#!/usr/bin/env python3
#coding:utf-8

import json

# 读取json文件内容
with open("test.json") as fp:
    data = json.load(fp)

print(data)
print("read json success")
