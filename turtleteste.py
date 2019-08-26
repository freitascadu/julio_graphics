from turtle import *
t=Turtle()
t.hideturtle()

def ponto (x, y, esp, cor):
    t.penup()
    t.setpos(x,y)
    t.dot(esp, cor)

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
                ponto(x1, y1, 5, "yellow")
                y = y2
                for y in range(y2,y1):
                    ponto(x1, y, 5, "black")
            else:
                ponto(x2, y2, 5, "purple")
                y = y2
                for y in range (y2, y1):
                    ponto(((y-b)/m), y, 5, "black")
        elif (x1 == x2):
            print("Intervalo em Y eh maior com reta vertical")
            ponto(x1, y1, 5, "pink")
            y = y1
            for y in range (y1,y2):
                ponto(x1, y, 5, "pink")
        else:
            print("Intervalo em Y eh maior com x1 < x2")
            ponto (x1, y1, 5, "cyan")
            y = y1
            for y in range (y1, y2):
                ponto(((y-b)/m), y, 5, "black")
    else:
        if(x1>x2):
            print("Intervalo em X eh maior com x1 > x2")
            ponto(x2, y2, 5, "black")
            x = x2
            for x in range(x2, x1):
                ponto(x, (b+(m*x)), 5, "red")
        elif(x1 == x2):
            print("Intervalo em X eh maior com reta vertical")
            
            if(y1>y2):
                ponto(x1, y1, 5, "black")
                for x in range(y2,y1):
                    ponto(x1, (b+(m*x)), 5, "blue")
            else:
                ponto(x2,y2,5,"black")
                print(b)
                for x in range(y1,y2):
                    ponto(x1, (b+(m*x)), 5, "blue")
        else:
            print("Intervalo em X eh maior com x1 < x2")
            ponto(x1, y1, 5, "black")
            x = x1
            for x in range(x1,x2):
                ponto(x, (b+(m*x)), 5, "green") 
            
    
    

    
ponto(10,10,5, "red")

ponto(0,0, 5, "blue")

#reta(10,10,100,100, 5, "red")

eqReta(10,10,100,10, 5, "black")
eqReta(100,10,100,100, 5, "black")
eqReta(100,100,10,100, 5, "black")
eqReta(10,100,10,10, 5, "black")
