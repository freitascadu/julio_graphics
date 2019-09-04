from tkinter import *
t = Tk()
wid = 1000
hei = 1000
w = Canvas(t, width=wid, height=hei)
w.pack()


def ponto (x, y, esp, cor):
    #calculo para arrumar os eixos e centralizar a origem
    x = x + (wid/2)
    y = -y + (hei/2)
    #desenho do ponto
    x1 = x - (esp/2)
    y1 = y + (esp/2)
    x2 = x + (esp/2)
    y2 = y - (esp/2)
    w.create_oval(x1,y1,x2,y2,fill=cor,outline=cor)
    
#coefieciente angular da reta
def calculaM(x1, x2, y1, y2):
    if ((x2-x1) == 0):
        m = 0
    else:
        m = (y2-y1)/(x2-x1)
    return m

#coefieciente linear da reta
def calculaB(x1, x2, y1,y2):
    m = calculaM(x1, x2, y1, y2)
    b = y2 - (m * x2)
    return b

#calculo da equacao da reta e desenho da reta atraves de cada ponto da reta
def retaGraf (x1,y1, x2,y2, esp, cor):
    m = calculaM(x1, x2, y1, y2)
    b = calculaB(x1,x2, y1,y2)
    print("y - ",y1," = ",m," * x - ",x1)
    if (m > 1):
        if (y1 > y2):
            print("Intervalo em Y eh maior")
            if (x1 == x2):
                ponto(x1, y1, esp, cor)
                y = y2
                for y in range(y2,y1):
                    ponto(x1, y, esp, cor)
            else:
                ponto(x2, y2, esp, cor)
                y = y2
                for y in range (y2, y1):
                    ponto(((y-b)/m), y, esp, cor)
        elif (x1 == x2):
            print("Intervalo em Y eh maior com reta vertical")
            ponto(x1, y1, esp, cor)
            y = y1
            for y in range (y1,y2):
                ponto(x1, y, esp, cor)
        else:
            print("Intervalo em Y eh maior com x1 < x2")
            ponto (x1, y1, esp, cor)
            y = y1
            for y in range (y1, y2):
                ponto(((y-b)/m), y, esp, cor)
    else:
        if(x1>x2):
            print("Intervalo em X eh maior com x1 > x2")
            ponto(x2, y2, 5, cor)
            x = x2
            for x in range(x2, x1):
                ponto(x, (b+(m*x)), esp, cor)
        elif(x1 == x2):
            print("Intervalo em X eh maior com reta vertical")
            
            if(y1>y2):
                #ponto(x1, y1, 5, "black")
                for x in range(y1,y2,-1):
                    if (x == y1):
                        ponto(x1, b, esp, cor)
                    else:
                        ponto(x1, b-(x-y1), esp,cor)
            else:
                #ponto(x2,y2,5,"black")
                print(b)
                for x in range(y1,y2):
                    ponto(x1, (b-(x-y1)), esp, cor)
        else:
            print("Intervalo em X eh maior com x1 < x2")
            ponto(x1, y1, esp, "black")
            x = x1
            for x in range(x1,x2):
                ponto(x, (b+(m*x)), esp, cor) 

def fractal():
    retaGraf(0,0,0,150,2,"red")
    retaGraf(0,0,0,-150,2,"red")
    retaGraf(0,-150,-150,-75,2,"red")
    retaGraf(-150,-75,-150,75,2,"red")
    retaGraf(-150,75,0,150,2,"red")
    retaGraf(0,150,150,75,2,"red")
    retaGraf(150,75,150,-75,2,"red")
    retaGraf(150,-75,0,-150,2,"red")
    retaGraf(150,75,-150,-75,2,"red")
    retaGraf(-150,75,150,-75,2,"red")
    retaGraf(150,-75,0,150,2,"red")
    retaGraf(0,150,-150,-75,2,"red")
    retaGraf(-150,-75,150,75,2,"red")
    retaGraf(150,75,-150,75,2,"red")
    retaGraf(-150,-75,150,-75,2,"red")
    retaGraf(-150,75,0,-150,2,"red")
    retaGraf(0,-150,150,75,2,"red")
    retaGraf(50,-75,-50,75,2,"red")
    retaGraf(-50,-75,50,75,2,"red")
    ponto(0,150,5,"blue")
    ponto(-150,75,5,"blue")
    ponto(-50,75,5,"blue")
    ponto(50,75,5,"blue")
    ponto(150,75,5,"blue")
    ponto(-100,0,5,"blue")
    ponto(100,0,5,"blue")
    ponto(-150,-75,5,"blue")
    ponto(-50,-75,5,"blue")
    ponto(50,-75,5,"blue")
    ponto(150,-75,5,"blue")
    ponto(0,-150,5,"blue")

fractal()
#w.mainloop()
