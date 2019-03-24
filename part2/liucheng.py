# coding: utf-8
res = 59
if res >= 60:
    print('及格')
else:
    print('不及格')

n = 6
if n:
    print('hello python')

m = 123
if m < 5:
    print('m < 5')
elif m < 10:
    print('n < 10')
else:
    print('n >=10')

#and
if m >=10 and n < 200:
    print('hi')

#or
if m >= 1000 or n < 200:
    print('n < 200')

count = 1
sum = 0
while count <= 100:
    sum = sum +count
    count = count +1

print(sum)

sum2 = 0
count = 1

while True:
    sum2 += count
    count+=1
    if sum2 > 100:
        break

print(sum2)

c = 1
s = 0
while c <= 1000:

    if c % 2 == 0:
        print(c)
        c = c+1 #这里需要加上，否则就陷入死循环
        continue
    else:
        s += c
        c = c+1

print(s)

#while---else
#while ... else 在循环条件为 false时执行 else 语句块
c = 0
while c < 5:
    print(c)
    c = c+1
else:
    print("====while else===")
    print(c)

#for x in y
for x in range(1,10):
    print("x={}".format(x))


