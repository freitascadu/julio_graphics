"""
Esse modulo especifica a classe Ponto

"""


class Ponto:

    def __init__(self, x = 0, y = 0):
        self.__x = x
        self.__y = y


    @property
    def x(self):
        return self.__x


    @property
    def y(self):
        return self.__y


    @x.setter
    def x(self, new_x):
        self.__x = new_x


    @y.setter
    def y(self, new_y):
        self.__y = new_y


