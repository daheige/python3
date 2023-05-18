# coding: utf-8

# 切片slice定义
list1 = ["a", "b", "c"]

print(list1)

# 添加list元素
list1.append('d')
print(list1)

print(list1[0])  # 访问第一个元素
# [m:n]截取列表中的部分元素
print(list1[:-2])
print(list1[0:2])  # index 0-2之间的元素，不包含2

list1[1] = "heige"
print(list1)

list1.append("golang")
list1.append("dd")
print(list1)

list1.append(["d", "ss"])

print(list1)  # ['a', 'heige', 'c', 'd', 'golang', 'dd', ['d', 'ss']]

# 删除元素
del list1[0]
print(list1)

list2 = [1, 2, 3]
print(list2 + [2, 3])  # list相加

print(len(list2))

print(2 in list2)  # 判断元素是否在列表中

# 迭代打印
print("===for----in====")
for x in list1:
    print(x)

# max
print(max(list2))
print("===min===")
print(min(list2))

# 元素出现的次数
cnt = list2.count(2)
print(cnt)

print(list2.count(13))

# 一次性追加多个元素
list2.extend([1, 2, 3])
print("list2")
print(list2)

# 某个元素出现的次数
print(list2.index(3))

list2.insert(1, 200)  # 在index位置插入元素

print(list2)

# 移除列表中最后一个元素
print(list2.pop())
print(len(list2))

# 对列表反转
list1.reverse()
print(list1)  # [['d', 'ss'], 'dd', 'golang', 'd', 'c', 'heige']


list3 = [1, 3, 23, 12, 32, 5, 6, 2, 15]
list3.sort()  # 升序
print(list3)  # [1, 2, 3, 5, 6, 12, 15, 23, 32]


# list转换
t = (1, 2, 3)
print(list(t))
