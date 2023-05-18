# coding: utf-8
# set(list) #set集合
# 创建一个 set,需要提供一个 list 作为输入集合
set1 = set([1, 2, 3, 4])

print(set1)
set1.add(123)

print(set1)

# remove元素
print(set1.remove(123) == None)
# print(set1.remove(13))#报错

set2 = set("hello")
set3 = set("hello world")
print(set2)
print(set3)

# 交集相同部分
print(set2 & set3)

# a-b差集
print(set2 - set3)
print(set3-set2)  # 把相同部分排除掉，在set3中

# a和b一起的部分，并集
print("====set2 | set3==")
print(set2 | set3)

# 对list去除重复元素
list1 = [111, 222, 333, 444, 111, 222, 333, 444, 555, 666]
set4 = set(list1)
print(set4)

# 然后把set4转换为list
print(list(set4))
