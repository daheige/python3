name = "daheige"
if name.title() == 'Daheige':  # if语句没有()括起来
    print(1)
else:
    print(2)


clist = [1, 3, 4]
print(1 in clist)  # 检测是否在列表中
print(5 not in clist)  # 检测不再列表中

# python的布尔值Ture,False

age = 18
if age >= 18:
    print(1)
else:
    print(2)

# if...elif..else..if
age = 21
if age < 10:
    print(1)
elif age < 12:
    print(2)
elif age <= 18:
    print(3)
else:
    print('age > 18')
