# prompt = 'Tell me a num'
# prompt += '\nEnter quit to end the program '
# flag = True
# while flag: #等于quit就退出,采用标记来处理循环终止
#     message = input(prompt)
#     if message != 'quit':
#         print(message)
#     else:
#         flag = False

num = 1
while num < 10:
    num += 1
    if num % 2 == 0:
        continue #终止本次，继续下一次
    print(num)


