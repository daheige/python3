name = input('please input your name:')
print(name)
age = input('how old are you:')
#异常处理
try:
    age = int(age)
    print(age)
except Exception as err:
    print('err age')

num = input('please input num:')
num = int(num)
if num % 2 == 0:
    print('this num is even')
else:
    print('this num is odd.')