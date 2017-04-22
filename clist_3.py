#切片
clist = ['ddd','sss','dagege','fefef']
print(clist[:3]) #clist[m:n] 从m位置开始截取，不包含n位置

#返回最后三个元素
print(clist[-3:])
for val in clist[-3:]:
    print(val)

print(clist)

#复制列表
my_list = clist[:]
print(my_list)
my_list.append("xiaowei")
print(clist)
print(my_list)

#两个列表都指向同一个内存地址，改变一个，另一个也会改变
hg_list = my_list #不是my_list的副本拷贝
print(my_list)
hg_list.append('daheige')
print(hg_list)
print(my_list)