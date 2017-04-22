#!/usr/bin/env python3
#-*- coding: utf-8 -*-
clist = [1,23,234,'fefefe']
#追加元素
clist.append('daheige');
clist.append('da');
clist.append('heige');
clist.append('dahei');
clist.append('dage');
print(clist)

# 在指定的位置插入元素
clist.insert(2,45)
#删除元素

del clist[3]
print(clist)

# 从末尾弹出一个元素
clist.pop()

print(clist)

#从指定的位置弹出
clist.pop(3)

#根据值删除(只删除第一个值)
clist.remove('daheige')

print(clist)

#排序
hglist = [1,22,3,4,-1]
hglist.sort()
print(hglist)

print(sorted(hglist)) #临时排序
print(hglist)

#倒序
hglist.reverse()
print(hglist)

#列表的长度
print(len(hglist))







