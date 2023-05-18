# coding: utf-8
dict1 = {
    "name": "daheige",
    "age": 29,
}

# 迭代key
for k in dict1:
    print(k)

for v in dict1.values():
    print(v)

for k, v in dict1.items():
    print(k, v)

# 迭代器有两个基本的方法:iter() 和 next(),且字符串,列表或元组对象都可用于创建迭代器,迭
# 代器对象可以使用常规 for 语句进行遍历,也可以使用 next() 函数来遍历
# 只能往前不后退

str1 = 'hello'
iter1 = iter(str1)

list1 = [1, 2, 3, 4, 5]
iter2 = iter(list1)

for x in iter1:
    print(x)

for x in iter2:
    print('===x===')
    print(x)

t1 = (1, 2, 3, 4)
iter3 = iter(t1)

print('====next iter3===')
# next() 函数遍历迭代器
while True:
    try:
        print(next(iter3))
    except StopIteration:
        break

print(list(range(1, 20)))

# 利用range迭代打印九九乘法表
print('\n'.join([' '.join('%dx%d=%2d' % (x, y, x*y)
      for x in range(1, y+1)) for y in range(1, 10)]))

# lsit 生成式的语法为:
# 1. [expr for iter_var in iterable]
# 2. [expr for iter_var in iterable if cond_expr]

list2 = [x * x for x in range(1, 10)]
print(list2)

# for后面有if
print([x * x for x in range(1, 10) if x % 2 == 0])

list3 = [(x+1, y + x) for x in range(1, 5) for y in range(1, 9)]
print(list3)
