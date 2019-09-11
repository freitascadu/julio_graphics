"""
Esse modulo especifica a classe Circulo a partir da classe Ponto
"""

from ponto import Ponto
import math

class Circulo(Ponto):

    def __init__(self, centroX=0, centroY=0, raio=0):
        self.__centro = Ponto(centroX, centroY)
        self.__raio = raio


    @property
    def raio(self):
        return self.__raio


    @property
    def centroX(self):
        return self.__centro.x


    @property
    def centroY(self):
        return self.__centro.y


    def calcularCircunferencia(self):
        return (2*math.pi*self.__raio)


    def calcularArea(self):
        return (math.pi * (self.__raio**2))
