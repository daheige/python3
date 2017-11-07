def greet_user(username='daheige'):
    print('------------welcome to here---------')
    print(username.title())


greet_user()
greet_user('hehe')


# 函数返回值
def get_name(username='daheige'):
    return username.title()


print(get_name('heige'))


def build_name(first_name='heige', last_name='da'):
    return {'first': first_name, 'last': last_name}


print(build_name('zw', 'da'))


# 参数是一个列表
def get_users(users):
    for name in users:
        print('hello ' + name.title())


get_users(['heige', 'maoge'])


# 任意数量的参数
def make_piza(*topings):  # topings是在里面是一个元祖
    print('-------------topings--------')
    for name in topings:
        print('-' + name)


make_piza('cake', 'egg', 'dog')


def make_pizza_2(size, *topings):
    print('make a ' + str(size) + ' length pizza')
    for name in topings:
        print('-' + name)


make_pizza_2(12, 'ddd', 'egg', 'mao')

print("success")
