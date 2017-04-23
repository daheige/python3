clist = ['dd','ss','sssass']
while clist:
    cur_val = clist.pop() #每次弹出一个元素
    print(cur_val)

#从列表中删除特定值
pets = ['dog','cat','dog','sss','sfa']
while 'dog' in pets:
    pets.remove('dog')

print(pets)