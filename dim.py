#元祖不可变
dimensions = (1,2,32)
print(dimensions)
# dimensions[0] = 1 #试图改变会报错
# for  in 遍历
for val in dimensions:
    print(val)

#可以定义同名变量
dimensions = (1,35)
print(dimensions)

#如果在整个程序生命周期内不变化，可以采用元组存放元素的值
