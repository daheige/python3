#coding: utf-8
for n in range(1,20):
    for i in range(2,n):
        if n % i == 0:
            j = n /i
            print('%d 是一个合数' % n)
            break
    else:
        print('%d 是一个质数' % n)

for i in range(1,10):
    for j in range(1,i+1):
        print('{} x {} = {} \t'.format (i,j,i*j))
