#coding: utf-8

def changeList(l):
    l.append(100)

l = [1,2,3,4]
changeList(l)
print(l)

l2 = [1,2,3,4]
changeList(l2)
changeList(l2)
changeList(l2)
print(l2)

def sum (num,num2):
    if not (isinstance(num,(int,float)) and isinstance(num2,(int,float))):
        raise TypeError('param error')
    else:
        return num +num2

print(sum(10,23.23))
# print(sum('ss',23.23))

#多个返回值，放在元组中
def div(num1,num2):
    a = num1 % num2
    b = num1 -a / num2
    return b,a

print(div(22,3))

#只有在形参表末尾的那些参数可以有默认参数值
def printUser(name,age,sex = 1):
    print('name is {}'.format(name))
    print("age is {}".format(age))
    print("sex is {}".format(sex))

printUser('heige',29)
# printUser('xiaoxiao',18,sex = 0)
printUser('xiaoxiao',18,0)

# 默认参数的值是不可变的对象,比如None、True、False、数字或字符串
# 如果你像上面的那样操作,当默认值在其他地
# 方被修改后你将会遇到各种麻烦

def printInfo(a,b = []):
    print(b)
    return b

res = printInfo(1)
res.append('error')
printInfo(2) #['error']

#如果不想要默认值
_no_value = object()
def printInfo2(a,b = _no_value):
    if b is _no_value:
        print('b 没有赋值')

    if b == 2:
        print(b)
    return;

printInfo2(1,2) #b必须传递

#关键字参数 不需要关心参数的顺序
printUser(name = 'daheige',sex = 12,age=29)
printUser(age = 12,sex = 0,name="xiaoxiao")

#不定长参数
# Python 提供了一种元组的方式来接受没有直接定义的参数。这种方式在参数前边加星号
# *如果在函数调用时没有指定参数,它就是一个空元组。我们也可以不向函数传递未命名的变量

# *hobby 是可变参数,且 hobby其实就是一个 tuple (元祖)
def printInfo3(name,age,*hobby):
    print('name: {}'.format(name))
    print('age: {}'.format(age))
    print('hobby: {}'.format(hobby))

printInfo3('daheige',29,'golang')
printInfo3('daheige',29)

#可变参数
# 可变长参数也支持关键参数,没有被定义的关键参数会被放到一个字典里。这种方式即是在参数前边加**

#**hobby 是关键字参数,且 hobby 就是一个 dict (字典)
def printUser2(name,age,**hobby):
    print('name is: {}'.format(name))
    print('age is {}'.format(age))
    print('hobby is {}'.format(hobby))

printUser2(name = 'daheige',age = 29,hobby = ("dd","ss")) #**hobby是一个字典
printUser2(name= "ss",age = 12,hobby = 12) #hobby: 12

# python 使用 lambda 来创建匿名函数,也就是不再使用 def 语句这样标准的形式定义一个函数

sum2 = lambda n,m: m+n
print(sum2(1,2))
