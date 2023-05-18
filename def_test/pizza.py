# 定义模块pizza
# 任意数量的参数
def make_piza(*topings):  # topings是在里面是一个元祖
    print('-------------topings--------')
    for name in topings:
        print('-'+name)


def make_pizza_2(size, *topings):
    print('make a '+str(size)+' length pizza')
    for name in topings:
        print('-'+name)
