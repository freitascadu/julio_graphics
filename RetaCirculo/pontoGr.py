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


    def origem(self, wid=1000, hei=1000):
        self._Ponto__x = self._Ponto__x + (wid / 2)
        self._Ponto__y = self._Ponto__y + (hei / 2)


    def desenhaPonto(self, jan):
        self.origem()
        x1 = self._Ponto__x - (self.__esp / 2)
        y1 = self._Ponto__y + (self.__esp / 2)
        x2 = self._Ponto__x + (self.__esp / 2)
        y2 = self._Ponto__y - (self.__esp / 2)
        jan.create_oval(x1, y1, x2, y2, fill = self.__cor, outline = self.__cor)


t = Tk()
wid = 1000
hei = 1000
w = Canvas(t, width=wid, height=hei)
w.pack()
print(f'EU SOU O {__name__}') 


