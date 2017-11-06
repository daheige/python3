class Car:
    def __init__(self, name, size, color):
        self.name = name
        self.size = size
        self.color = color

    def resetSize(self, size):
        self.size = size + 1

    def getDesc(self):
        print("this car name is" + self.name, "Car color is " + self.name,
              'size is ' + str(self.size))


class Batt():
    def __init(self, name, r):
        self.name = name
        self.r = r

    def get_range(self):
        print("this r is", self.r)
