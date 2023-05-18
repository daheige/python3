#!/usr/bin/env python3
# set coding
# -*- coding: utf-8 -*-
print("大黑哥")

# 注释用#开头
x = 12
print(x)

y = 17
print(y / 3)  # 除以操作
print(y % 3)  # 取模操作 = 2
z = 5 ** 2  # 表示取得平方操作
print("current z = "+str(z))

s = "daheige\nabc"  # \操作表示转义操作符
print(s)

# 原始字符串不转义操作，以r开头
s2 = r"abc\nddd"  # 将输出abc\nddd
print(s2)

# 通过三个单引号的方式定义长字符串
help = """\
Usage: cli [OPTIONS]
        -H help
        -h host name
"""
print(help)

# 对字符串进行重复操作
s = 3 * "abc"
print(s)
