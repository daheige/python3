#!/usr/bin/env python3
# coding:utf8

ali = {
    'x': 'fefefe',
    'age': 23,
    'name': 'sss'
}

# ali.items()迭代每项
for key, val in ali.items():
    print("this key is " + key, 'this value is ' + str(val))

for key in ali.keys():
    print("key is " + key)

for val in ali.values():
    print(val)

for k in sorted(ali.keys()):
    print("this sorted key is", k)
