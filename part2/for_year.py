# coding: utf-8
year = int(input('请输入一个数字'))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('{0} 是闰年'.format(year))
else:
    print('{}不是一个闰年'.format(year))
