#!/usr/bin/env python3
#coding:utf-8

try:
    x = 1
    print(x / 0)
except ZeroDivisionError:  #错误类型
    print("zero error")
