#!/usr/bin/env python3
# coding:utf8

# 元组，不可变
dim = (1, 2, 3)

print(dim)
print(dim[0])

# dim[0] = 1 会报错

for item in dim:
    print(item)

# 可以重新定义元组
dim = (1, 23, 34, 98)
print(dim)

for i in dim:
    if i != 34:
        print("this value is ne 34")
    else:
        print("this is 34")
else:
    print(111)

x = 13
if x < 3:
    print("x < 3")
elif x < 12:
    print("x < 12")
else:
    print("x >= 12")
