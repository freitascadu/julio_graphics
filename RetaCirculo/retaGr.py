"""
Esse modulo implementa a classe RetaGr a partir da classe Reta
para desenhar uma reta gráfica
"""

from reta import Reta
from pontoGr import *

class RetaGr(Reta, PontoGr):

    def __init__(self, x1 = 0, y1 = 0, x2 = 0, y2 = 0, cor = 'black', esp = 2):
        Reta.__init__(self, x1, y1, x2, y2)
        self.__cor = cor
        self.__esp = esp


    @property
    def cor(self):
        return self.__cor


    @property
    def esp(self):
        return self.__esp


    def desenhaReta(self, jan):
        b = self.calculaB()
        m = self.calculaM()
        if (m > 1):
            if (self._Reta__y1 > self._Reta__y2):
                print("Intervalo em Y eh maior")
                if (self._Reta__x1 == self._Reta__x2):
                    ponto = PontoGr(self.p1.x, self.p1.y, self.__cor, self.__esp)
                    ponto.desenhaPonto(jan)
                    for y in range(self._Reta__y2,self._Reta__y1):
                        ponto = PontoGr(self.p1.x, y, self.__cor, self.__esp)
                        ponto.desenhaPonto(jan)
                else:
                    ponto = PontoGr(self.p2.x, self.p2.y, self.__cor, self.__esp)
                    for y in range (self._Reta__y2, self._Reta__y1):
                        ponto = PontoGr(int((y-b)/m), y, self.__cor, self.__esp)
                        ponto.desenhaPonto(jan)
            elif (self._Reta__x1 == self._Reta__x2):
                print("Intervalo em Y eh maior com reta vertical")
                ponto = PontoGr(self.p1.x, self.p1.y, self.__cor, self.__esp)
                ponto.desenhaPonto(jan)
                y = self._Reta__y1
                for y in range (self._Reta__y1,self._Reta__y2):
                    ponto = PontoGr(self.p1.x, y, self.__cor, self.__esp)
                    ponto.desenhaPonto(jan)
            else:
                print("Intervalo em Y eh maior com x1 < x2")
                ponto = PontoGr(self.p1.x, self.p1.y, self.__cor, self.__esp)
                ponto.desenhaPonto(jan)
                y = self._Reta__y1
                for y in range (self._Reta__y1, self._Reta__y2):
                    ponto = PontoGr(int((y-b)/m), y, self.__cor, self.__esp)
                    ponto.desenhaPonto(jan)
        else:
            if(self._Reta__x1>self._Reta__x2):
                print("Intervalo em X eh maior com x1 > x2")
                ponto = PontoGr(self.p2.x, self.p2.y, self.__cor, self.__esp)
                ponto.desenhaPonto(jan)
                x = self._Reta__x2
                for x in range(self._Reta__x2, self._Reta__x1):
                    ponto = PontoGr(x, int(b+m*x), self.__cor, self.__esp)
                    ponto.desenhaPonto(jan)
            elif(self._Reta__x1 == self._Reta__x2):
                print("Intervalo em X eh maior com reta vertical")
                if(self._Reta__y1>self._Reta__y2):
                    ponto = PontoGr(self.p1.x, self.p1.y, self.__cor, self.__esp)
                    ponto.desenhaPonto(jan)
                    for x in range(self._Reta__y1,self._Reta__y2,-1):
                        if (x == self._Reta__y1):
                            ponto = PontoGr(self.p1.x, b, self.__cor, self.__esp)
                            ponto.desenhaPonto(jan)
                        else:
                            ponto = PontoGr(self.p1.x, int(b-(x-self._Reta__y1)), self.__cor, self.__esp)
                            ponto.desenhaPonto(jan)
                else:
                    ponto = PontoGr(self.p2.x, self.p2.y, self.__cor, self.__esp)
                    ponto.desenhaPonto(jan)
                    for x in range(self._Reta__y1, self._Reta__y2):
                        ponto = PontoGr(self.p1.x, int(b - (x-self._Reta__y1)), self.__cor, self.__esp)
                        ponto.desenhaPonto(jan)
            else:
                print("Intervalo em X eh maior com x1 < x2")
                ponto = PontoGr(self.p1.x, self.p1.y, self.__cor, self.__esp)
                ponto.desenhaPonto(jan)
                x = self._Reta__x1
                for x in range(self._Reta__x1,self._Reta__x2):
                    ponto = PontoGr(x, int(b+(m*x)), self.__cor, self.__esp)
                    ponto.desenhaPonto(jan)

r1 = RetaGr(0, 0,0,150,'red',2)
r2 = RetaGr(0, 0,0,-150,'red',2)
r3 = RetaGr(10,10,100,100,'blue',2)
r1.desenhaReta(w)
r2.desenhaReta(w)
r3.desenhaReta(w)
