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


    def desenhaReta(self, reta, jan):
        b = self.calculaB()
        m = self.calculaM()
        if (m > 1):
            if (reta.y1 > reta.y2):
                print("Intervalo em Y eh maior")
                if (reta.x1 == reta.x2):
                    ponto = PontoGr(self.p1.x, self.p1.y, reta.cor, reta.esp)
                    ponto.desenhaPonto(ponto, jan)
                    for y in range(reta.y2,reta.y1):
                        ponto = PontoGr(self.p1.x, y, reta.cor, reta.esp)
                        ponto.desenhaPonto(ponto, jan)
                else:
                    ponto = PontoGr(self.p2.x, self.p2.y, reta.cor, reta.esp)
                    for y in range (reta.y2, reta.y1):
                        ponto = PontoGr(int((y-b)/m), y, reta.cor, reta.esp)
                        ponto.desenhaPonto(ponto, jan)
            elif (reta.x1 == reta.x2):
                print("Intervalo em Y eh maior com reta vertical")
                ponto = PontoGr(self.p1.x, self.p1.y, reta.cor, reta.esp)
                ponto.desenhaPonto(ponto, jan)
                y = reta.y1
                for y in range (reta.y1,reta.y2):
                    ponto = PontoGr(self.p1.x, y, reta.cor, reta.esp)
                    ponto.desenhaPonto(ponto,jan)
            else:
                print("Intervalo em Y eh maior com x1 < x2")
                ponto = PontoGr(self.p1.x, self.p1.y, reta.cor, reta.esp)
                ponto.desenhaPonto(ponto, jan)
                y = reta.y1
                for y in range (reta.y1, reta.y2):
                    ponto = PontoGr(int((y-b)/m), y, reta.cor, reta.esp)
                    ponto.desenhaPonto(ponto, jan)
        else:
            if(reta.x1>reta.x2):
                print("Intervalo em X eh maior com x1 > x2")
                ponto = PontoGr(self.p2.x, self.p2.y, reta.cor, reta.esp)
                ponto.desenhaPonto(ponto, jan)
                x = reta.x2
                for x in range(reta.x2, reta.x1):
                    ponto = PontoGr(x, int(b+m*x), reta.cor, reta.esp)
                    ponto.desenhaPonto(ponto, jan)
            elif(reta.x1 == reta.x2):
                print("Intervalo em X eh maior com reta vertical")
                if(reta.y1>reta.y2):
                    ponto = PontoGr(self.p1.x, self.p1.y, reta.cor, reta.esp)
                    ponto.desenhaPonto(ponto, jan)
                    for x in range(reta.y1,reta.y2,-1):
                        if (reta.x == reta.y1):
                            ponto = PontoGr(self.p1.x, b, reta.cor, reta.esp)
                            ponto.desenhaPonto(ponto, jan)
                        else:
                            ponto = PontoGr(self.p1.x, int(b-(x-reta.y1)), reta.cor, reta.esp)
                            ponto.desenhaPonto(ponto, jan)
                else:
                    ponto = PontoGr(self.p2.x, self.p2.y, reta.cor, reta.esp)
                    ponto.desenhaPonto(ponto, jan)
                    for x in range(reta.y1, reta.y2):
                        ponto = PontoGr(self.p1.x, int(b - (x-reta.y1)), reta.cor, reta.esp)
                        ponto.desenhaPonto(ponto, jan)
            else:
                print("Intervalo em X eh maior com x1 < x2")
                ponto = PontoGr(self.p1.x, self.p1.y, reta.cor, reta.esp)
                ponto.desenhaPonto(ponto, jan)
                x = reta.x1
                for x in range(reta.x1,reta.x2):
                    ponto = PontoGr(x, int(b+(m*x)), reta.cor, reta.esp)
                    ponto.desenhaPonto(ponto, jan)

r = RetaGr(10,10,10,100,'black',2)

r.desenhaReta(r, w)
