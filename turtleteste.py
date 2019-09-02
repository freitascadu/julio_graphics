from tkinter import *
t = Tk()
wid = 1000
hei = 1000
w = Canvas(t, width=wid, height=hei)
w.pack()


def ponto (x, y, esp, cor):
    x = x + (wid/2)
    y = -y + (hei/2)
    x1 = x - (esp/2)
    y1 = y + (esp/2)
    x2 = x + (esp/2)
    y2 = y - (esp/2)
    w.create_oval(x1,y1,x2,y2,fill=cor)
    

def calculaM(x1, x2, y1, y2):
    if ((x2-x1) == 0):
        m = 0
    else:
        m = (y2-y1)/(x2-x1)
    return m


def calculaB(x1, x2, y1,y2):
    m = calculaM(x1, x2, y1, y2)
    b = y2 - (m * x2)
    return b


def eqReta (x1,y1, x2,y2, esp, cor):
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
            
    
    
#ponto(10,10,5, "red")

#ponto(0,0, 50, "blue")

#reta(10,10,100,100, 5, "red")


eqReta(10,10,100,10, 5, "black")
eqReta(100,10,100,100, 5, "black")
eqReta(100,100,10,100, 5, "black")
eqReta(10,100,10,10, 5, "black")
eqReta(10,10,100,100,5, "black")
eqReta(10,100,100,10,5, "black")
eqReta(10,100,55,155,5, "black")
eqReta(55,155,100,100,5, "black")
eqReta(55,10, 55, 155, 5, "black")

#w.mainloop()
#eqReta(20, 30, 10,50,5, "red")
