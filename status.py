from tkinter import * 
#from tkinter import ttl

class Status(Frame):
	STATUS_SIZE = 32
	STATUS_BG = "red"
	STATUS_FG = "white"
	def __init__(self, mestre, msg):
		Frame.__init__(mestre, height=self.STATUS_SIZE, bg=self.STATUS_BG)
		msg = Label(self, text="Text", height=self.STATUS_SIZE, bg=self.STATUS_BG, fg=self.STATUS_FG)


if(__name__ == "__main__"):
	root = Tk()
	root.title("Teste de Status")
	janela = Frame(root, height=500, width=500)
	janela.pack()
	status = Status(janela, "Teste")

'''
Cor
tupla(255,0,255)
string "#ff00ff"
nome "red"
#background: #272822

Cursors
arrow (normal)
watch (carregando do windows)
wait (tb)
no (proibido vermelho)

circle (melhor)
cross (cruz grande com 3 riscos)
dotbox
exchange
fleur (seta de mover)
mouse (de pc)
pirate (caveira)
plus (cruz pequena grossa)
sizing
spraycan
target (circular pqno)
tcross (cruz pequena fina)
crosshair (cruz grande grossa)
hand2 (mao de selecao)


Bitmaps
"error" (proibido)
(os cinzas sao cores de pontos)
"gray75"
"gray50"
"gray25"
"gray12"
"hourglass" (ampola de vidro)
"info" (i de info)
"questhead" (interrogacao na cabeca)
"question" (interrogacao)
"warning" (exclamacao)

Pegar pixel de img - Python Image Library
import Image
im = Image.open("name_of_file.jpg")
list_of_pixels = list(im.getdata())
print list_of_pixels[0]

'''	
'''
#Observe:
#So precisa 

import tkinter as tk
import time

class App():
    def __init__(self):
        self.root = tk.Tk()
        self.label = tk.Label(text="")
        self.label.pack()
        self.update_clock()
        self.root.mainloop()

    def update_clock(self):
        now = time.strftime("%H:%M:%S")
        self.label.configure(text=now)
        self.root.after(1000, self.update_clock)

app=App()

'''

'''
from tkinter import *

class Frame1(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, bg="red")
        self.parent = parent
        self.widgets()

    def widgets(self):
        self.text = Text(self)
        self.text.insert(INSERT, "Hello World\t")
        self.text.insert(END, "This is the first frame")
        self.text.grid(row=0, column=0, padx=20, pady=20) # margins


class MainW(Tk):

    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent
        self.mainWidgets()

    def mainWidgets(self):

        self.label1 = Label(self, text="Main window label", bg="green")
        self.label1.grid(row=0, column=0)

        self.label2 = Label(self, text="Main window label", bg="yellow")
        self.label2.grid(row=1, column=0)

        self.window = Frame1(self)
        self.window.grid(row=0, column=10, rowspan=2)

if __name__=="__main__":
    app = MainW(None)
    app.mainloop()
'''


'''
class Example(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.l1 = tk.Label(self, text="Hover over me")
        self.l2 = tk.Label(self, text="", width=40)
        self.l1.pack(side="top")
        self.l2.pack(side="top", fill="x")

        self.l1.bind("<Enter>", self.on_enter)
        self.l1.bind("<Leave>", self.on_leave)

    def on_enter(self, event):
        self.l2.configure(text="Hello world")

    def on_leave(self, enter):
        self.l2.configure(text="")

if __name__ == "__main__":
    root = tk.Tk()
    Example(root).pack(side="top", fill="both", expand="true")
    root.mainloop()
'''
# http://www.tcl.tk/man/tcl8.6/TkCmd/options.htm
# http://effbot.org/tkinterbook/tkinter-events-and-bindings.htm
# https://tkdocs.com/search.html?q=photoimage
# https://www.tutorialspoint.com/python/python_gui_programming.htm
