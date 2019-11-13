"""
Esse modulo especifica a classe Reta a partir da classe Ponto
"""

from ponto import Ponto

class Reta(Ponto):

    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        self.__p1 = Ponto(x1, y1)
        self.__p2 = Ponto(x2, y2)
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    @property
    def x1(self):
        return self.__x1


    @property
    def y1(self):
        return self.__y1


    @property
    def x2(self):
        return self.__x2


    @property
    def y2(self):
        return self.__y2


    @property
    def p1(self):
        return self.__p1


    @property
    def p2(self):
        return self.__p2


    def calculaM(self):
        if ((self.p2.x - self.p1.x) == 0):
            m = 0
        else:
            m = (self.p2.y - self.p1.y) / (self.p2.x - self.p1.x)
        return m


    def calculaB(self):
        m = self.calculaM();
        b = self.p2.y - (m * self.p2.x)
        return b


    def mostraEquacao(self, m, b):
        print(f'y = {m}x + {b}')

