# coding:utf-8
import re

print(1)

print(122)
x = 12
x, y = 1, 2
print(x)
print(y)

print(1)
print("heige")

# 这是一个注释
print(y)

# 多行注释
"""
fefefe
"""

print(123)


def add(a, b):
    """求和"""
    return a + b


print(add(1, 2))

MAX_OVERFLOW = 100
print(MAX_OVERFLOW)

a = "abcedf heige"

print("是否包含 heige {0}".format(a.index("heige") > -1))  # True
all = re.findall("heige", a)
if len(all) > 0:
    print("a 包含 heige")
else:
    print("a not contain heige")

# 找到所有的小写字母
re_findall = re.findall('[a-z]', a)

print(re_findall)


a = "python*android*java*golang"

sub1 = re.sub("\*", "&", a)  # 返回替换之后的字符串
print(sub1)

# 通过指定函数作为正则re的回调


def convert(val):
    group = val.group()
    if group == "*":
        return "&"
    elif group == "-":
        return "|"


sub3 = re.sub('[\*-]', convert, a)
print(sub3)

# 匹配a-z
x = re.match('[a-z]', a, 1)
print(x.group(0))

a = 'abc<img src="https://s-media-cache-ak0.pinimg.com/originals/a8/c4/9e/a8c49ef606e0e1f3ee39a7b219b5c05e.jpg">'

ser = re.search('<img src="(.*)">', a)

print(ser.group(0))

print(ser.groups())  # 以元组的形式返回
y = ser.group(0)
print(y)

print("abc")

b = 122

if b == 0:
    print("yes")
else:
    print("no")

num = 1
num2 = 0xff
print(num, num2)

s = 'hello heige\'sss'
print(s)

b = r'\-\t-/---'  # 表示这是一个 raw 字符串,
# 里面的字符就不需要转义了

print(b)

# boolean
c = True

print(c)

c = False

print("c的值{}".format(c))

d = None  # 空值

d = 12
print(d)

x = 123
print(hex(x))  # 转换为16进制

x = 123.23
print(x)

print(x == 123.23)  # True

y = '12'
print(int(y))  # 转换为整数

# 多个变量赋值
a, b, c = 1, 2, 3
print(a, b, c)

print(a)
print(b)
print(c)
