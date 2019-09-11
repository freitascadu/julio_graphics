"""
Esse modulo implementa a classe CirculoGr a partir das classes Circulo e PontoGr
"""

from circulo import Circulo
from pontoGr import *
import math

class CirculoGr(Circulo, PontoGr):

    def __init__(self, centroX = 0, centroY = 0, raio = 0, cor = 'black', esp = 2):
        Circulo.__init__(self, centroX, centroY, raio)
        self.__cor = cor
        self.__esp = esp


    @property
    def cor(self):
        return self.__cor


    @property
    def esp(self):
        return self.__esp


    def desenhaCirculo(self, jan):
        if (self._Circulo__raio != 0):
            x = 0
            y = self._Circulo__raio
            for alfa in range(0, 451, 1):
                alfa = alfa / 10
                x = (self._Circulo__raio * math.cos((alfa*math.pi)/180))
                y = (self._Circulo__raio * math.sin((alfa*math.pi)/180))
                ponto = PontoGr(self._Circulo__centro.x + x, self._Circulo__centro.y + y, self.__cor, self.__esp)
                ponto.desenhaPonto(jan)
                ponto = PontoGr(self._Circulo__centro.x + y, self._Circulo__centro.y + x, self.__cor, self.__esp)
                ponto.desenhaPonto(jan)
                ponto = PontoGr(self._Circulo__centro.x + y, self._Circulo__centro.y - x, self.__cor, self.__esp)
                ponto.desenhaPonto(jan)
                ponto = PontoGr(self._Circulo__centro.x + x, self._Circulo__centro.y - y, self.__cor, self.__esp)
                ponto.desenhaPonto(jan)
                ponto = PontoGr(self._Circulo__centro.x - x, self._Circulo__centro.y - y, self.__cor, self.__esp)
                ponto.desenhaPonto(jan)
                ponto = PontoGr(self._Circulo__centro.x - y, self._Circulo__centro.y - x, self.__cor, self.__esp)
                ponto.desenhaPonto(jan)
                ponto = PontoGr(self._Circulo__centro.x - y, self._Circulo__centro.y + x, self.__cor, self.__esp)
                ponto.desenhaPonto(jan)
                ponto = PontoGr(self._Circulo__centro.x - x, self._Circulo__centro.y + y, self.__cor, self.__esp)
                ponto.desenhaPonto(jan)


    def desenhaCirculoMidPoint(self, jan):
        if (self._Circulo__raio != 0):
            x = 0
            y = float(self._Circulo__raio)
            d = float(5 / 4 - self._Circulo__raio)
            self.desenharPontosMP(x, y, jan)
            while (y > x):
                if (d < 0):
                    d = d + 2 * x + 3
                    x += 1
                else:
                    d = d + 2 * (x - y) + 5
                    x += 1
                    y -= 1
                self.desenharPontosMP(x, y, jan)


    def desenharPontosMP(self, x, y, jan):
        ponto = PontoGr(self._Circulo__centro.x + x, self._Circulo__centro.y + y, self.__cor, self.__esp)
        ponto.desenhaPonto(jan)
        ponto = PontoGr(self._Circulo__centro.x + y, self._Circulo__centro.y + x, self.__cor, self.__esp)
        ponto.desenhaPonto(jan)
        ponto = PontoGr(self._Circulo__centro.x + y, self._Circulo__centro.y - x, self.__cor, self.__esp)
        ponto.desenhaPonto(jan)
        ponto = PontoGr(self._Circulo__centro.x + x, self._Circulo__centro.y - y, self.__cor, self.__esp)
        ponto.desenhaPonto(jan)
        ponto = PontoGr(self._Circulo__centro.x - x, self._Circulo__centro.y - y, self.__cor, self.__esp)
        ponto.desenhaPonto(jan)
        ponto = PontoGr(self._Circulo__centro.x - y, self._Circulo__centro.y - x, self.__cor, self.__esp)
        ponto.desenhaPonto(jan)
        ponto = PontoGr(self._Circulo__centro.x - y, self._Circulo__centro.y + x, self.__cor, self.__esp)
        ponto.desenhaPonto(jan)
        ponto = PontoGr(self._Circulo__centro.x - x, self._Circulo__centro.y + y, self.__cor, self.__esp)
        ponto.desenhaPonto(jan)

        
"""        
c = CirculoGr(0,0,200)
ci = CirculoGr(0,0,100)
ci.desenhaCirculoMidPoint(w)
c.desenhaCirculo(w)
"""
