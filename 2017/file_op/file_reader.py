#!/usr/bin/env python3
#coding:utf-8

with open("pi_dig.md") as file_obj:
    contents = file_obj.read()
    print("contents \n" + contents)

# 逐行读取数据
with open("pi_dig.md") as file_obj:
    for row in file_obj:
        print(row.rstrip())

# 将内容读取到一个列表中

with open("pi_dig.md") as file_obj:
    lines = file_obj.readlines()

for item in lines:
    print(item)

print("row count is", len(lines))

pi_str = ''
for item in lines:
    pi_str += item.strip()
print(pi_str)
