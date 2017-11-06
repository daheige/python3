#!/usr/bin/env python3
#-*- coding: utf-8 -*-
clist = [1, 23, 234, 'fefefe']
# 遍历列表,需缩进
for l in clist:
    print(l)

print('think you')

# 创建数字列表
numbers = list(range(1, 5))  # list()将结果转换为列表 range产生一个范围的值
print(numbers)

# 设置步长
even_nums = list(range(2, 10, 2))
print(even_nums)

squ = []
for val in range(1, 10):
    squ.append(val**2)

print(squ)
# 简写模式
squ_2 = [value**2 for value in range(1, 10)]  # 列表解析方式
print(squ_2)

# 最大值和最小值
print(min(squ_2))
print(max(squ_2))
