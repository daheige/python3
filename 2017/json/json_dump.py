#!/usr/bin/env python3
#coding:utf-8

import json

data = {'username': 'heige', 'job': 'php', 'nickname': '黑哥'}
with open("test.json", "w") as fp:
    json.dump(data, fp)

print("write success")
