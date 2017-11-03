res = {}
flag = True
while flag:
    name = input('what is your name: ')
    othername = input('age: ')
    res[name] = othername
    repate = input('would you like othername(yes/no):')
    if repate == 'no':
        flag = False

print('---------------result----------------')
print(res)
