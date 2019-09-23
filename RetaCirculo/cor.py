
#ver: https://www.tcl.tk/man/tcl/TkLib/GetColor.htm
#ver: csv de cores

class Cor:

    def __init__(self, **kwargs):
        #achar um jeito de converter
        if(tupla!=None):
            pass
        elif(nome!=None):
            pass
        elif(hex!=None):
            self.__valor = hex #como chama o valor do dict do kwargs msm?
        #implamentacao de tranparencia futura
        if(alpha!=None):
            pass

    
    @property
    def valor(self):
        return self.__valor

    #como chama o setter no init?
    #valor interno 
    @valor.setter
    def valor(self, new_valor):
        self.__valor = new_valor

    #Deve retornar a cor conforme o tk entende:
    #tupla, string com o nome ou string com # na frente do hex
    def pinta(self):
        return self.__valor

    #So pra testar, essa funcao deve fazer o negativo da cor
    #vai dar mto trabalho pra negativar de hex
    def pintaNegativo(self):
        pass
        
        




    
