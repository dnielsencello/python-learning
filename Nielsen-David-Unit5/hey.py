# David Nielsen
# CS1400 - I01
# Assigment ??
class A:
    def __init__(self):
        self.x = 1
        self.__y = 2

    def getY(self):
        return self.__y


a = A()
print(a.__y)