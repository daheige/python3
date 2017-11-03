number = 1
while number < 5:
    print(number)
    # number++ #py中没有num++运算符号
    number += 1
    # number = number+1
prompt = 'Tell me a num'
prompt += '\nEnter quit to end the program '
message = ''
while message != 'quit':  # 等于quit就退出
    message = input(prompt)
    message != 'quit' and print(message)  # python中与操作符号是and
