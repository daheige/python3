#!/usr/bin/env python3
#coding:utf-8
"""类的声明"""


class Dog():
    """声明类的时候可以给默认值"""

    def __init__(self, name, age, sex=1):
        """初始化"""
        self.name = name
        self.age = age
        self.sex = sex

    def say(self, word):
        print("this dog is" + self.name + " and age is " + str(self.age),
              " word is " + word)
        print("this sex is", self.sex)


# 实例化
my_dog = Dog("haha", 1, 2)
my_dog.say("fefe")
print(my_dog.name)
my_dog.name = "xiaoming"
my_dog.say("sss")


#类的继承和重写方法
class EleDog(Dog):
    def __init__(self, name, age, sex, year=2017):
        super().__init__(name, age, sex)
        self.year = year

    def getName(self):
        print("sub dog name is" + self.name)

    def say(self):
        print("sub name is " + self.name, "year is " + str(self.year))


sub_dog = EleDog("maomao", 12, 3, 2018)
sub_dog.say()
