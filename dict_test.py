#字典类似js中的对象 key/al类型
alien = {'color':'green','points':5}
print(alien)
# print(alien.color)#会报错，应该是中括号的方式访问
print(alien['color'])
print(alien['color']+str(alien['points'])) #需将数字转换为字符串
#追加key/val
alien['x_pos'] = 0
alien['y_pos'] = 25
print(alien)

#通过字面量方式创建字典
alien_0 = {}
alien_0['x'] = 1;alien_0['y'] = 2; #多条语句放在一行需要用;来分割
print(alien_0)

alien_0['x'] = 12 #修改字典中的值
print(alien_0)

# 删除key
del alien_0['x'] #彻底删除key/val
alien_0['z'] = 3
print(alien_0)

study_langs = {
    'jen':'python',
    'sar':'c',
    'edward':'ruby',
    'phil' :'python',
}
print(study_langs)

#遍历字典的key/val
for name,lang in study_langs.items(): #items()保存了key/val
    print(name+':'+lang)
print(study_langs.keys()) #所有的key

for name in study_langs.keys():
    print(name)
print('---------sorted key/val-----')
for name in sorted(study_langs.keys()):
    print(name)

# vals = study_langs.values()
# print(vals) #dict_values(['python', 'c', 'ruby', 'python'])

# 遍历所有的值
for lang in study_langs.values():
    print(lang)

#去掉值中的重复项
print('----------remove repate-------')
for lang in set(study_langs.values()): #采用集合方式
    print(lang)
