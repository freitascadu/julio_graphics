"""
Esse modulo especifica a classe PontoGr a partir da classe Ponto
"""

from ponto import Ponto
from tkinter import *

class PontoGr(Ponto):

    def __init__(self, x = 0, y = 0, cor = 'black', esp = 2):
        Ponto.__init__(self, x, y)
        self.__cor = cor
        self.__esp = esp


    @property
    def cor(self):
        return self.__cor


    @property
    def esp(self):
        return self.__esp


    def origem(self, ponto, wid=1000, hei=1000):
        self._Ponto__x = ponto.x + (wid / 2)
        self._Ponto__y = ponto.y + (hei / 2)


    def desenhaPonto(self, ponto, jan):
        self.origem(ponto)
        x1 = ponto.x - (ponto.esp / 2)
        y1 = ponto.y + (ponto.esp / 2)
        x2 = ponto.x + (ponto.esp / 2)
        y2 = ponto.y - (ponto.esp / 2)
        jan.create_oval(x1, y1, x2, y2, fill = ponto.cor, outline = ponto.cor)


t = Tk()
wid = 1000
hei = 1000
w = Canvas(t, width=wid, height=hei)
w.pack()



