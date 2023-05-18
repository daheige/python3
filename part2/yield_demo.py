# coding:utf-8
# 在 Python 中,这种一边循环一边计算
# 的机制,称为生成器:generator
# 函数是顺序执行,遇到 return 语句或者最后
# 一行函数语句就返回。而变成 generator 的函数,在每次调用 next() 的时候执行,遇到 yield
# 语句返回,再次执行时从上次返回的 yield 语句处继续执行。

def odd():
    print('step1')
    yield (1)
    print('step2')
    yield (2)


o = odd()
print(next(o))
print(next(o))

# 通过迭代器实现反向打印


class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1


print('=====reversed range(1,13)')
for x in reversed(Countdown(12)):
    print(x)

# 倒序
print('===倒序===')
for x in Countdown(12):
    print(x)

# 同时迭代多个序列zip
# 其实 zip(a, b) 会生成一个可返回元组 (x, y) 的迭代器,其中 x 来自 a,y 来自 b。 一旦其
# 中某个序列到底结尾,迭代宣告结束。 因此迭代长度跟参数中最短序列长度一致。注意理解这句话
# 喔,也就是说如果 a , b 的长度不一致的话,以最短的为标准,遍历完后就结束
# zip()是可以接受多于两个的序列的参数,不仅仅是两个
names = ['daheige', 'xiaoxiao', 'xiaoming']
ages = [12, 15, 35]
for name, age in zip(names, ages):
    print(name, age)
