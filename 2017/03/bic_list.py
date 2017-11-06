#!/usr/bin/env python3
#-*- coding:utf8 -*-

bic = ['fe', 'tcan', 'readline']

print(bic)
print(bic[0])
print("第一个元素是", bic[0])

# 遍历列表
for item in bic:
    print("this value is " + item.title())

print("think you!")

for i in range(1, 5):
    print(i)

# 创建数字列表

num_list = list(range(1, 4))
print(num_list)

num2 = list(range(0, 10, 2))

print(num2)

sq = []

for i in range(1, 11):
    sq.append(i**2)  # 乘方

print(sq)

print("列表sq 最大的一个元素是" + str(max(sq)))
print("列表sq 最小的一个元素是" + str(min(sq)))
print("对列表求和", sum(sq))

# 列表解析

sq_list = [value**2 for value in range(1, 11)]
print(sq_list)

# 切片

sq_list_2 = sq_list[1:5]

print(sq_list_2)

for i in sq_list[0:6]:
    print(i)
