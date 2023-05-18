# -*-coding:utf-8-*-

user = ["liangshu", "twowater"]
user.append("heige")

print(len(user))
print(user)

# 元组
# tuple 一旦初始化就不能修改
t = (1, 2, 3)
print(t)
print(t[0], t[1])

t = ()
print(t)

# 一个元素的元组
t = (1,)
print(t[0])

print(t[0])

# 如果元组中的元素是可变的类型，也是可以改变该元素
# tuple 所谓的“不变”是说,tuple 的每个元素,指向永远不变
list1 = [1, 2]
t = ('s', 'y', list1)

t[2].append(1)
t[2].append(3)

t2 = (1, 3, 4)
t3 = (11, 2, 3)
print(t2 + t3)  # 相加后就是一个新的元组
print(t2 * 3)  # 元组复制，重复几次

# for...in迭代
print("=====for in=====")
for x in t3:
    print(x)

print(cmp(t2, t3))  # t2<t3

print(len(t3))
print("====max===")
print(max(t2))

# 元组转换
list2 = [1, 2, 3]
print(tuple(list2))  # list--->tuple
