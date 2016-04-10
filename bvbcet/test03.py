from __future__ import print_function, division
import math

class Line:
    def __init__(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        return

    def __str__(self):
        s = 'Line( %f, %f, %f, %f)' % (self.__x1, self.__y1, self.__x2, self.__y2)
        return s

    def length(self):
        dx = self.__x2 - self.__x1
        dy = self.__y2 - self.__y1
        return math.sqrt(dx**2 + dy**2)

    def area(self):
        return 0.0

class Circle:
    def __init__(self, x, y, radius):
        self.__x = x
        self.__y = y
        self.__r = radius
        return

    def __str__(self):
        s = 'Circle(Centre at %f, %f, Radius %f)' % (self.__x, self.__y, self.__r)
        return s

    def length(self):
        pass

    def area(self):
        pass

L1 = Line(0, 0, 3, 4)
print(type(L1))
#print(L1.__x1, L1.__y1, L1.__x2, L1.__y2)
L1.x1 = 100.0
#print(L1.__x1, L1.__y1, L1.__x2, L1.__y2)
print(L1)
print(L1.length())
print(L1.area())

C1 = Circle(0, 0, 5)
print(C1)