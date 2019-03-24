#coding: utf-8
d = {} #字面量创建字典，其实就是map
d["a"] = 1
d["b"] = "dd"
print(d)

d["a"] = 123
print(d)

c = d
d["a"] = 32

#修改了d的话，c也会同步，以为c,d的指向相同
print(d)
print(c)

del d["a"] #删除map中的元素，和list删除方法del一样

d.clear() #清空字典
del d #删除字典

print(c) #c也被跟着清空了
#map的key必须是不可变的
#dict (字典)键必须不可变,可是键可以用数字,字符串或元组充当,但是就是不能使用列表

d = {
    "a":1,
    (1,2,3): 2,
}

print(d)
print(d.keys()) #打印所有的key

#查找和插入的时间随着元素的增加而增加
#占用空间小,浪费内存很少
print("===d len is===")
print(len(d))

#字典的字符串打印
print(str(d))

#返回变量的类型
print(type(d))
print(type("a"))
print(type(1))
print(type(23.09))
print(type([1,2]))

m = {
    "a":1,
    "b":23,
}

n = m.copy() #map浅复制
m["c"] = 234
print(n)
print(m)

print("====map values===")
print(m.values()) #values是一个列表
print(m.keys()) #keys也是一个list
print("====items===")
print(m.items()) #以列表返回可遍历的(键, 值) 元组数组

#遍历map
for x,y in m.items():
    print(x)
    print(y)

#利用zip生成字典
names = ['daheige','xiaoxiao']
ages =[12,28]
dict3 = dict(zip(names,ages))
print('===dict3===')
print(dict3)
