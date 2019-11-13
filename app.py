from tkinter import *
from tkinter import ttk
from tkinter.colorchooser import askcolor
from time import *
from pontoGr import *
from retaGr import *
from circulo import *
from circuloGr import *
from math import *
from xml.dom.minidom import *
from xml.dom.minidom import parse

STD_ALTURA = 720
STD_LARGURA = 1280

STATUS_SIZE = 32
PROPORCAO_PAINEL = 4
PAINEL_SIZE = STD_LARGURA / PROPORCAO_PAINEL

STD_BG = "#272822"

STATUS_BG = "#ff0000"
STATUS_FG = "#ffffff"

BOTAO_BG = "#272822"
BOTAO_FG = "#ffffff"
BOTAO_BD = 5

COR_BORDA = "#000000"
SIZE_BORDA = 3

COR_SELETA = "#ff0000"
COR_QUADRO = "#ffffff"

ESPESSURA_SELETA = 2
ESPESSURA_MAX = 64
ESPESSURA_MIN = 2

ferramenta = "Mão"

pilhaGeo = []
historicoMapa = []
historicoQuadro = []
historicoXML = []

root = Tk()
root.config(width=STD_LARGURA, height=STD_ALTURA)
root.title("PobroShop")
geo = f'{STD_LARGURA}x{STD_ALTURA}+50+50'
root.geometry(geo)
root.minsize(STD_LARGURA, STD_ALTURA)
root.maxsize(STD_LARGURA, STD_ALTURA)
root.aspect(1,1,1,1)




#ORGANIZACAO DE FRAMES

#frame maior (janela) que engloba todos os outros
janela = Frame(root, width=STD_LARGURA, height=(STD_ALTURA))

#frame app gui (painel+quadro)
app = Frame(janela, bg=STD_BG)

#painel
painel = Frame(app, bg=STD_BG, width=PAINEL_SIZE, height=(STD_ALTURA-STATUS_SIZE))

#print status, serve pra debug
status = Frame(janela, bg=STATUS_BG, height=STATUS_SIZE)
infoStatus = Label(
   status,
   bitmap="warning",
   bg=STATUS_BG,
   fg=STATUS_FG
   )
dockMsg = Frame(
   status,
   bg=infoStatus["background"]
   )
msg = Label(
   dockMsg,
   text="Aqui fica o feedback do programa.",
   bg=infoStatus["background"],
   fg=infoStatus["foreground"]
   )
coordS = Label(
   status,
   text="0,0",
   bg=infoStatus["background"],
   fg=infoStatus["foreground"]
   )
infoStatus.pack(side=LEFT)
dockMsg.pack(side=LEFT)
msg.pack(side=LEFT)
coordS.pack(side=RIGHT)


#quadro de desenho
quadro = Frame(
               app,
               bg="white",
               width=(STD_LARGURA-PAINEL_SIZE),
               height=(STD_ALTURA-STATUS_SIZE)
               )

#mapa de quadro
mapa = Frame(
   painel,
   bg=quadro["background"],
   cursor="circle",
   width=painel['width'],
   height=(STD_ALTURA/PROPORCAO_PAINEL)
   )

#ordem e posicionamento de geometria
janela.pack(expand=True, fill=BOTH)
app.pack(side=TOP, expand=True, fill=BOTH)
status.pack(side=BOTTOM, fill=X)
painel.pack(side=LEFT, fill=Y)
mapa.pack(side=BOTTOM)
quadro.pack(side=LEFT, expand=True, fill=BOTH)

#rolagem do painel
rolagemPainel = Scrollbar(painel)
rolagemPainel.pack(side=RIGHT, fill=Y)

#FUNCOES DE EVENTOS
desenhoQuadro = Canvas(quadro, bg=COR_QUADRO, cursor="hand2")
desenhoMapa = Canvas(mapa, bg=desenhoQuadro["bg"])
desenhoQuadro.pack(side=TOP, expand=True, fill=BOTH)
desenhoMapa.pack(side=TOP)

def cliqueDesenho(event):
   global desenhoQuadro
   global desenhoMapa
   global pilhaGeo
   global historicoQuadro
   global historicoMapa
   global historicoXML
   infoStatus.config(bitmap="warning")
   str_status = f'Ferramenta {ferramenta}: Clique em {event.x},{event.y} do Desenho. '
   msg.config(text=str_status)
   if(ferramenta=="Mão"):
      pass
   elif(ferramenta=="Poligono"):
      print("Desenhar poligono aqui")
      pass
   elif(ferramenta=="Ponto"):
      ponto1 = PontoGr(event.x,event.y, COR_SELETA, ESPESSURA_SELETA)
      ponto1.origem(-1000, -1000)
      ponto1.desenhaPonto(desenhoQuadro)
      historicoQuadro.append(ponto1)
      #temporario, pq tem que re-escalar o canvas, e nao desenhar duas vezes
      #a escala hard 3 ta errada, a usada no programa eh 4 mas nao ta calibrada tb
      ponto2 = PontoGr(event.x/3, event.y/3, COR_SELETA, ESPESSURA_SELETA/3)
      ponto2.origem(-1000, -1000)
      ponto2.desenhaPonto(desenhoMapa)
      historicoMapa.append(ponto2)
      xn = event.x/desenhoQuadro.winfo_width()
      yn = event.y/desenhoQuadro.winfo_height()
      red =   int(f'{COR_SELETA[1]}{COR_SELETA[2]}',16)
      green = int(f'{COR_SELETA[3]}{COR_SELETA[4]}',16)
      blue =  int(f'{COR_SELETA[5]}{COR_SELETA[6]}',16)
      historicoXML.append(f'<Ponto><x>{xn}</x><y>{yn}</y><Cor><R>{red}</R><G>{green}</G><B>{blue}</B></Cor><Espessura>{ESPESSURA_SELETA}</Espessura></Ponto>')
      msg.config(text=str_status+f'Desenhei um ponto! Cor: {COR_SELETA} e Espessura:{ESPESSURA_SELETA}')
   elif(ferramenta=="Reta"):
      #se a pilha ta vazia adiciona
      #se a pilha ja tem um ponto, adiciona outro e plota a reta
      
      if(len(pilhaGeo)==0):
         ponto = PontoGr(event.x,event.y, COR_SELETA, ESPESSURA_SELETA)
         ponto.origem(0, 0)
         pilhaGeo.append(ponto)
         msg.config(text=str_status+f'Guardei um ponto da reta! Cor: {COR_SELETA} e Espessura:{ESPESSURA_SELETA}')
      else:
         ponto = PontoGr(event.x,event.y, COR_SELETA, ESPESSURA_SELETA)
         ponto.origem(0, 0)
         pilhaGeo.append(ponto)
         pA = pilhaGeo.pop()
         pB = pilhaGeo.pop()
         pC = pA
         pD = pB
         reta = RetaGr(int(pA.x), int(pA.y), int(pB.x), int(pB.y), COR_SELETA, ESPESSURA_SELETA)
         reta.desenhaLine(desenhoQuadro)
         #pq nao desenha no mapa?
         reta2 = RetaGr(int(pC.x/3), int(pC.y/3), int(pD.x/3), int(pD.y/3), COR_SELETA, ESPESSURA_SELETA/3)
         reta2.desenhaLine(desenhoMapa)
         historicoQuadro.append(reta)
         historicoMapa.append(reta2)
         xn = pA.x/desenhoQuadro.winfo_width()
         yn = pA.y/desenhoQuadro.winfo_height()
         xn2= pB.x/desenhoQuadro.winfo_width()
         yn2= pB.y/desenhoQuadro.winfo_height()
         red =   int(f'{COR_SELETA[1]}{COR_SELETA[2]}',16)
         green = int(f'{COR_SELETA[3]}{COR_SELETA[4]}',16)
         blue =  int(f'{COR_SELETA[5]}{COR_SELETA[6]}',16)
         historicoXML.append(f'<Reta><Ponto><x>{xn}</x><y>{yn}</y></Ponto><Ponto><x>{xn2}</x><y>{yn2}</y></Ponto><Cor><R>{red}</R><G>{green}</G><B>{blue}</B></Cor><Espessura>{ESPESSURA_SELETA}</Espessura></Reta>')
         
         msg.config(text=str_status+f'Desenhei uma reta! Cor: {COR_SELETA} e Espessura:{ESPESSURA_SELETA}')
         
   elif(ferramenta=="Círculo"):
      #global pilhaGeo
      if(len(pilhaGeo)==0):
         pilhaGeo.append((event.x,event.y))
         msg.config(text=str_status+f'Guardei o centro! Cor: {COR_SELETA} e Espessura:{ESPESSURA_SELETA}')
      else:
         raioP = (event.x,event.y)
         centro = pilhaGeo.pop()
         raio = sqrt((raioP[0]-centro[0])*(raioP[0]-centro[0])+(raioP[1]-centro[1])*(raioP[1]-centro[1]))
         circulo = CirculoGr( centro[0], centro[1], raio, COR_SELETA, ESPESSURA_SELETA)
         circulo.desenhaCirculoMidPoint(desenhoQuadro)
         circulinho = CirculoGr( centro[0]/3, centro[1]/3, raio/3, COR_SELETA, ESPESSURA_SELETA/3)
         circulinho.desenhaCirculoMidPoint(desenhoMapa)
         historicoQuadro.append(circulo)
         historicoMapa.append(circulinho)

         xn = centro[0]/desenhoQuadro.winfo_width()
         yn = centro[1]/desenhoQuadro.winfo_height()
         
         red =   int(f'{COR_SELETA[1]}{COR_SELETA[2]}',16)
         green = int(f'{COR_SELETA[3]}{COR_SELETA[4]}',16)
         blue =  int(f'{COR_SELETA[5]}{COR_SELETA[6]}',16)
         
         historicoXML.append(f'<Circulo><Ponto><x>{xn}</x><y>{yn}</y></Ponto><Raio>{raio}</Raio><Cor><R>{red}</R><G>{green}</G><B>{blue}</B></Cor><Espessura>{ESPESSURA_SELETA}</Espessura></Circulo>')

         msg.config(text=str_status+f'Desenhei Circulo! raio: {round(raio)} e centro: {centro[0]},{centro[1]}')
         
   elif(ferramenta=="Letra"):
      pass
   elif(ferramenta=="Pencil"):
      pass
      #<B1-Motion>
   elif(ferramenta=="Spray"):
      pass


def riscoDesenho(event):
   global desenhoQuadro
   global desenhoMapa
   global pilhaGeo
   infoStatus.config(bitmap="warning")
   str_status = f'Ferramenta {ferramenta}: Risco em {event.x},{event.y} do Desenho. '
   msg.config(text=str_status)
   if(ferramenta=="Mão"):
      pass
   elif(ferramenta=="Apagar"):
      pass
   elif(ferramenta=="Ponto"):
      pass
   elif(ferramenta=="Reta"):
      pass
   elif(ferramenta=="Círculo"):
      pass
   elif(ferramenta=="Letra"):
      pass
   elif(ferramenta=="Pencil"):
      if(len(pilhaGeo)==0):
         ponto = PontoGr(event.x,event.y, COR_SELETA, ESPESSURA_SELETA)
         ponto.origem(0, 0)
         pilhaGeo.append(ponto)
      else:
         ponto = PontoGr(event.x,event.y, COR_SELETA, ESPESSURA_SELETA)
         ponto.origem(0, 0)
         pilhaGeo.append(ponto)
         pA = pilhaGeo.pop()
         pB = pilhaGeo.pop()
         pC = pA
         pD = pB
         reta = RetaGr(int(pA.x), int(pA.y), int(pB.x), int(pB.y), COR_SELETA, ESPESSURA_SELETA)
         reta.desenhaLine(desenhoQuadro)
         #pq nao desenha no mapa?
         reta2 = RetaGr(int(pC.x/3), int(pC.y/3), int(pD.x/3), int(pD.y/3), COR_SELETA, ESPESSURA_SELETA/3)
         reta2.desenhaLine(desenhoMapa)
         
         msg.config(text=str_status+f'Desenhei uma reta! Cor: {COR_SELETA} e Espessura:{ESPESSURA_SELETA}')
         
   elif(ferramenta=="Spray"):
      px = event.x
      py = event.y
      ponto1 = PontoGr(px,py, COR_SELETA, ESPESSURA_SELETA)
      ponto1.origem(-1000, -1000)
      ponto1.desenhaPonto(desenhoQuadro)
      ponto2 = PontoGr(px/3, py/3, COR_SELETA, ESPESSURA_SELETA/3)
      ponto2.origem(-1000, -1000)
      ponto2.desenhaPonto(desenhoMapa)
      msg.config(text=str_status+f'Risquei um ponto! Cor: {COR_SELETA} e Espessura:{ESPESSURA_SELETA}')
      xn = px/desenhoQuadro.winfo_width()
      yn = py/desenhoQuadro.winfo_height()
      red =   int(f'{COR_SELETA[1]}{COR_SELETA[2]}',16)
      green = int(f'{COR_SELETA[3]}{COR_SELETA[4]}',16)
      blue =  int(f'{COR_SELETA[5]}{COR_SELETA[6]}',16)
      historicoQuadro.append(ponto1)
      historicoMapa.append(ponto2)
      historicoXML.append(f'<Ponto><x>{xn}</x><y>{yn}</y><Cor><R>{red}</R><G>{green}</G><B>{blue}</B></Cor><Espessura>{ESPESSURA_SELETA}</Espessura></Ponto>')
   
#talvez de pra criar so uma classe dessas funcoes ?
def cliqueMapa(event):
   infoStatus.config(bitmap="warning")
   msg.config(text=f'Clique em {event.x},{event.y} do Mapa.')
def hoverMapa(event):
   coordS.config(text=f'({event.x}, {event.y})')
def mudouTam(event):
   infoStatus.config(bitmap="warning")
   msg.config(text=f'Quadro mudou de tamanho: {event.width}x{event.height}')
   


#FRAMES DE ENCAIXE

#msg.pack_forget() #nao apaga, mas tem q dar pack denovo
#msg.destroy() #apaga a instancia!!!!
#uso do .after() pra tempo?

#QUADRO
#declarado antes
desenhoQuadro.bind("<Button-1>", cliqueDesenho)
desenhoQuadro.bind("<Motion>", hoverMapa)
desenhoQuadro.bind("<Configure>", mudouTam)
desenhoQuadro.bind("<B1-Motion>", riscoDesenho)

#MAPA
#declarado antes
desenhoMapa.bind("<Button-1>", cliqueMapa)
#posicionado antes


#BARRA DE FERRAMENTAS - ESQ
SIZE_FERR = 55
ferramentasBorda = LabelFrame(
   painel,
   text="Barra de Ferramentas",
   bg=BOTAO_BG,
   fg=BOTAO_FG,
   height=SIZE_FERR,
   width=painel['width']
   )
ferramentasBorda.pack(side=TOP, fill=X)
ferramentasDock = Frame(ferramentasBorda, bg=STD_BG, width=ferramentasBorda['width'])
ferramentasDock.pack(fill=BOTH, expand=True)
ferrDir = Frame(
   ferramentasDock,
   bg=STD_BG,
   width=150)
ferrEsq = Frame(
   ferramentasDock,
   bg=STD_BG
   )
ferrEsq.pack(side=LEFT, fill=BOTH, expand=True)
ferrDir.pack(side=RIGHT, fill=BOTH, expand=True)



#funcoes chamadas pelos botoes
def mao():
   global ferramenta
   ferramenta = "Mão"
   for f in ferram:
      if(f!='mao'):ferram[f].config(state=ACTIVE, relief=RAISED)
   ferram['mao'].config(state=DISABLED, relief=SUNKEN)
   desenhoQuadro.config(cursor="hand2")
   
def poligono():
   global ferramenta
   ferramenta = "Poligono"
   for f in ferram:
      if(f!='poligono'):ferram[f].config(state=ACTIVE, relief=RAISED)
   ferram['poligono'].config(state=DISABLED, relief=SUNKEN)
   desenhoQuadro.config(cursor="tcross")
   
def ponto():
   global ferramenta
   ferramenta = "Ponto"
   for f in ferram:
      if(f!='ponto'):ferram[f].config(state=ACTIVE, relief=RAISED)
   ferram['ponto'].config(state=DISABLED, relief=SUNKEN)
   desenhoQuadro.config(cursor="circle")
   
def reta():
   global ferramenta
   ferramenta = "Reta"
   for f in ferram:
      if(f!='reta'):ferram[f].config(state=ACTIVE, relief=RAISED)
   ferram['reta'].config(state=DISABLED, relief=SUNKEN)
   desenhoQuadro.config(cursor="circle")
   
def circulo():
   global ferramenta
   ferramenta = "Círculo"
   for f in ferram:
      if(f!='circulo'):ferram[f].config(state=ACTIVE, relief=RAISED)
   ferram['circulo'].config(state=DISABLED, relief=SUNKEN)
   desenhoQuadro.config(cursor="circle")
def letra():
   global ferramenta
   ferramenta = "Letra"
   for f in ferram:
      if(f!='letra'):ferram[f].config(state=ACTIVE, relief=RAISED)
   ferram['letra'].config(state=DISABLED, relief=SUNKEN)
   desenhoQuadro.config(cursor="xterm")
   
def lapis():
   global ferramenta
   ferramenta = "Lapis"
   for f in ferram:
      if(f!='lapis'):ferram[f].config(state=ACTIVE, relief=RAISED)
   ferram['lapis'].config(state=DISABLED, relief=SUNKEN)
   desenhoQuadro.config(cursor="pencil")
   
def spray():
   global ferramenta
   ferramenta = "Spray"
   for f in ferram:
      if(f!='spray'):ferram[f].config(state=ACTIVE, relief=RAISED)
   ferram['spray'].config(state=DISABLED, relief=SUNKEN)
   desenhoQuadro.config(cursor="spraycan")

#imagens dos botoes:
bmMao=      BitmapImage(file="icons/mao.xbm", background=BOTAO_BG, foreground=BOTAO_FG)
bmPoligono=     BitmapImage(file="icons/poligono.xbm", background=BOTAO_BG, foreground=BOTAO_FG)
bmPonto=    BitmapImage(file="icons/ponto.xbm", background=BOTAO_BG, foreground=BOTAO_FG)
bmReta=     BitmapImage(file="icons/reta.xbm", background=BOTAO_BG, foreground=BOTAO_FG)
bmCirculo=  BitmapImage(file="icons/circulo.xbm", background=BOTAO_BG, foreground=BOTAO_FG)
bmLetra=    BitmapImage(file="icons/letra.xbm", background=BOTAO_BG, foreground=BOTAO_FG)
bmLapis=    BitmapImage(file="icons/lapis.xbm", background=BOTAO_BG, foreground=BOTAO_FG)
bmSpray=    BitmapImage(file="icons/spray.xbm", background=BOTAO_BG, foreground=BOTAO_FG)

#setup: command chama a funcao dele, que ja troca o cursor no desenho e levanta e abaixa os botoes
ferram = {
   'mao':      Button(ferrEsq, command = mao, bd=BOTAO_BD, image=bmMao, state=DISABLED, relief=SUNKEN, bg=BOTAO_BG, fg=BOTAO_FG, activeforeground=BOTAO_FG, activebackground=BOTAO_BG),
   'poligono': Button(ferrEsq, command = poligono, bd=BOTAO_BD, image=bmPoligono, state=ACTIVE, relief=RAISED, bg=BOTAO_BG, fg=BOTAO_FG, activeforeground=BOTAO_FG, activebackground=BOTAO_BG),
   'ponto':    Button(ferrEsq, command = ponto, bd=BOTAO_BD, image=bmPonto, state=ACTIVE, relief=RAISED, bg=BOTAO_BG, fg=BOTAO_FG, activeforeground=BOTAO_FG, activebackground=BOTAO_BG),
   'reta':     Button(ferrEsq, command = reta, bd=BOTAO_BD, image=bmReta, state=ACTIVE, relief=RAISED, bg=BOTAO_BG, fg=BOTAO_FG, activeforeground=BOTAO_FG, activebackground=BOTAO_BG),
   'circulo':  Button(ferrEsq, command = circulo, bd=BOTAO_BD, image=bmCirculo, state=ACTIVE, relief=RAISED, bg=BOTAO_BG, fg=BOTAO_FG, activeforeground=BOTAO_FG, activebackground=BOTAO_BG),
   'letra':    Button(ferrEsq, command = letra, bd=BOTAO_BD, image=bmLetra, state=ACTIVE, relief=RAISED, bg=BOTAO_BG, fg=BOTAO_FG, activeforeground=BOTAO_FG, activebackground=BOTAO_BG),
   'lapis':    Button(ferrEsq, command = lapis, bd=BOTAO_BD, image=bmLapis, state=ACTIVE, relief=RAISED, bg=BOTAO_BG, fg=BOTAO_FG, activeforeground=BOTAO_FG, activebackground=BOTAO_BG),
   'spray':    Button(ferrEsq, command = spray, bd=BOTAO_BD, image=bmSpray, state=ACTIVE, relief=RAISED, bg=BOTAO_BG, fg=BOTAO_FG, activeforeground=BOTAO_FG, activebackground=BOTAO_BG)
   }
#posicionamento em grid (uma row)
ferram['mao'].grid(row=0, column=0)
ferram['poligono'].grid(row=0, column=1)
ferram['ponto'].grid(row=0, column=2)
ferram['reta'].grid(row=0, column=3)
ferram['circulo'].grid(row=0, column=4)
ferram['letra'].grid(row=0, column=5)
ferram['lapis'].grid(row=0, column=6)
ferram['spray'].grid(row=0, column=7)


#BARRA DE PARAMETROS DE FERRAMENTAS (cor e espessura) - DIR


#imagens
bmCorConfig = BitmapImage(file="icons/contagotas.xbm", background=COR_SELETA, foreground=BOTAO_FG)
bmEspConfig = BitmapImage(file="icons/espessura.xbm", background=BOTAO_FG, foreground=BOTAO_BG)
#labels
corConfig = Label(ferrDir, image=bmCorConfig, bg=COR_SELETA)
espConfigLabel = Label(ferrDir, image=bmEspConfig, background=BOTAO_BG)
espConfig = Spinbox(
   ferrDir,
   from_=ESPESSURA_MIN,
   to=ESPESSURA_MAX,
   activebackground=BOTAO_BG,
   disabledbackground=BOTAO_BG,
   disabledforeground=BOTAO_FG,
   bg=BOTAO_BG,
   fg=BOTAO_FG,
   width=2
   )
corConfig.pack(side=RIGHT, fill=BOTH, expand=True)
espConfig.pack(side=RIGHT, fill=BOTH, expand=True)
espConfigLabel.pack(side=RIGHT, fill=BOTH, expand=True)

#funcoes
def escolheCor(event):
   global COR_SELETA
   protegeCor = COR_SELETA
   (tuplaCor, protegeCor) = askcolor(COR_SELETA)
   if(protegeCor != None): COR_SELETA = protegeCor
   corConfig.config(background=COR_SELETA)
   bmCorConfig.config(background=COR_SELETA)
corConfig.bind("<Button-1>",escolheCor)

def escolheEspessura():
   global ESPESSURA_SELETA
   ESPESSURA_SELETA=int(espConfig.get())
espConfig.config(command=escolheEspessura)
#movido o command pra nao reclamar que escolhe espessura nao existe


#funcao pra exemplo

def donothing():
   filewin = Toplevel(root) #toplevel eh uma janela que abre inrriba da outra, puxa o foco
   button = Button(filewin, text="Botao faz nada")
   button.pack()
         
def novoQuadro():
   global historico
   historicoXML.clear()
   historicoQuadro.clear()
   historicoMapa.clear()
   desenhoQuadro.delete("all")
   desenhoMapa.delete("all")
   
def salvaHistorico():
   global historicoXML
   slv = '<?xml version="1.0" encoding="UTF-8" standalone="no"?><Figura>'
   for linha in historicoXML:
      slv += linha
   slv += f'</Figura>'
   with open('output.xml', 'w') as file:
      file.write(slv)
   #return slv

def inputArquivo(nomeArq='output.xml'):
   global historico
   global COR_SELETA
   global ESPESSURA_SELETA
   global desenhoQuadro
   global desenhoMapa
   historicoQuadro.clear()
   historicoMapa.clear()
   desenhoQuadro.delete("all")
   desenhoMapa.delete("all")
   # Open XML document using minidom parser
   DOMTree = xml.dom.minidom.parse(nomeArq)
   figura = DOMTree.documentElement
   print(f'Figura com {len(figura.childNodes)} geometrias')
   for geo in figura.childNodes[:]:
      #print({geo.nodeName})
      if(geo.nodeName == 'Ponto'):
         #print(f'Tem um ponto:')
         try:
            xmlX = float(geo.getElementsByTagName('x')[0].childNodes[0].data)
            xmlY = float(geo.getElementsByTagName('y')[0].childNodes[0].data)
            xmlP = [xmlX, xmlY]
            del xmlX
            del xmlY
            xmlP[0] = int(xmlP[0]*desenhoQuadro.winfo_width())
            xmlP[1] = int(xmlP[1]*desenhoQuadro.winfo_width())
            #print(f'Ponto: Ponto é: {xmlP[0]},{xmlP[1]}')
         except:
            print("Ponto: X e Y nao encontrado")
         try:
            xmlCor = geo.getElementsByTagName('Cor')[0]
            xmlCorR = int(xmlCor.getElementsByTagName('R')[0].childNodes[0].data)
            xmlCorG = int(xmlCor.getElementsByTagName('G')[0].childNodes[0].data)
            xmlCorB = int(xmlCor.getElementsByTagName('B')[0].childNodes[0].data)
            #conversao pra hex com #
            if(xmlCorR > 15):
               xmlCorR = f'{hex(xmlCorR)[2]}{hex(xmlCorR)[3]}'
            else:
               xmlCorR = f'0{hex(xmlCorR)[2]}'
            if(xmlCorG > 15):
               xmlCorG = f'{hex(xmlCorG)[2]}{hex(xmlCorG)[3]}'
            else:
               xmlCorG = f'0{hex(xmlCorG)[2]}'
            if(xmlCorB > 15):
               xmlCorB = f'{hex(xmlCorB)[2]}{hex(xmlCorB)[3]}'
            else:
               xmlCorB = f'0{hex(xmlCorB)[2]}'
            xmlCor = f'#{xmlCorR}{xmlCorG}{xmlCorB}'
            #print(f'Circulo: Cor é: {xmlCor}')
            del xmlCorR
            del xmlCorG
            del xmlCorB
            COR_SELETA = xmlCor
            corConfig.config(background=COR_SELETA)
            bmCorConfig.config(background=COR_SELETA)
         except:
            print("Circulo: Cor nao encontrada")
         try:
            xmlEspessura = int(geo.getElementsByTagName('Espessura')[0].childNodes[0].data)
            #print(f'Circulo: Espessura é: {xmlEspessura}')
            ESPESSURA_SELETA = xmlEspessura
         except:
            print("Circulo: Espessura nao encontrada")
         ponto = PontoGr(xmlP[0],xmlP[1], COR_SELETA, ESPESSURA_SELETA)
         ponto.origem(-1000, -1000)
         historicoQuadro.append(ponto)
         ponto.desenhaPonto(desenhoQuadro)
         ponto = PontoGr(xmlP[0]/3, xmlP[1]/3, COR_SELETA, ESPESSURA_SELETA/3)
         ponto.origem(-1000, -1000)
         ponto.desenhaPonto(desenhoMapa)
         historicoMapa.append(ponto)
         
      
      if(geo.nodeName == 'Reta'):
         #print(f'Tem uma reta:')
         try:
            xmlPA = geo.getElementsByTagName('Ponto')[0]
            xmlX = float(xmlPA.getElementsByTagName('x')[0].childNodes[0].data)
            xmlY = float(xmlPA.getElementsByTagName('y')[0].childNodes[0].data)
            xmlPA = [xmlX, xmlY]
            del xmlX
            del xmlY
            xmlPA[0] = int(xmlPA[0]*desenhoQuadro.winfo_width())
            xmlPA[1] = int(xmlPA[1]*desenhoQuadro.winfo_width())
            #print(f'Reta: Ponto A é: {xmlPA[0]},{xmlPA[1]}')
         except:
            print("Reta: Ponto A nao encontrado")
         try:
            xmlPB = geo.getElementsByTagName('Ponto')[1]
            xmlX = float(xmlPB.getElementsByTagName('x')[0].childNodes[0].data)
            xmlY = float(xmlPB.getElementsByTagName('y')[0].childNodes[0].data)
            xmlPB = [xmlX, xmlY]
            del xmlX
            del xmlY
            xmlPB[0] = int(xmlPB[0]*desenhoQuadro.winfo_width())
            xmlPB[1] = int(xmlPB[1]*desenhoQuadro.winfo_width())
            #print(f'Reta: Ponto B é: {xmlPB[0]},{xmlPB[1]}')
         except:
            print("Reta: Ponto B nao encontrado")
         try:
            xmlCor = geo.getElementsByTagName('Cor')[0]
            xmlCorR = int(xmlCor.getElementsByTagName('R')[0].childNodes[0].data)
            xmlCorG = int(xmlCor.getElementsByTagName('G')[0].childNodes[0].data)
            xmlCorB = int(xmlCor.getElementsByTagName('B')[0].childNodes[0].data)
            #conversao pra hex com #
            if(xmlCorR > 15):
               xmlCorR = f'{hex(xmlCorR)[2]}{hex(xmlCorR)[3]}'
            else:
               xmlCorR = f'0{hex(xmlCorR)[2]}'
            if(xmlCorG > 15):
               xmlCorG = f'{hex(xmlCorG)[2]}{hex(xmlCorG)[3]}'
            else:
               xmlCorG = f'0{hex(xmlCorG)[2]}'
            if(xmlCorB > 15):
               xmlCorB = f'{hex(xmlCorB)[2]}{hex(xmlCorB)[3]}'
            else:
               xmlCorB = f'0{hex(xmlCorB)[2]}'
            xmlCor = f'#{xmlCorR}{xmlCorG}{xmlCorB}'
            #print(f'Circulo: Cor é: {xmlCor}')
            del xmlCorR
            del xmlCorG
            del xmlCorB
            COR_SELETA = xmlCor
            corConfig.config(background=COR_SELETA)
            bmCorConfig.config(background=COR_SELETA)
         except:
            print("Circulo: Cor nao encontrada")
         try:
            xmlEspessura = int(geo.getElementsByTagName('Espessura')[0].childNodes[0].data)
            #print(f'Circulo: Espessura é: {xmlEspessura}')
            ESPESSURA_SELETA = xmlEspessura
         except:
            print("Circulo: Espessura nao encontrada")
         reta = RetaGr(xmlPA[0], xmlPA[1], xmlPB[0], xmlPB[1], COR_SELETA, ESPESSURA_SELETA)
         reta.desenhaLine(desenhoQuadro)
         historicoQuadro.append(reta)
         reta = RetaGr(xmlPA[0]/3, xmlPA[1]/3, xmlPB[0]/3, xmlPB[1]/3, COR_SELETA, ESPESSURA_SELETA/3)
         reta.desenhaLine(desenhoMapa)
         historicoMapa.append(reta)

         
      if(geo.nodeName == 'Circulo'):
         #print(f'Tem um Circulo:')
         try:
            xmlCentro = geo.getElementsByTagName('Ponto')[0]
            xmlX = float(xmlCentro.getElementsByTagName('x')[0].childNodes[0].data)
            xmlY = float(xmlCentro.getElementsByTagName('y')[0].childNodes[0].data)
            xmlCentro = [xmlX, xmlY]
            del xmlX
            del xmlY
            xmlCentro[0] = int(xmlCentro[0]*desenhoQuadro.winfo_width())
            xmlCentro[1] = int(xmlCentro[1]*desenhoQuadro.winfo_width())
            #print(f'Circulo: Centro é: {xmlCentro[0]},{xmlCentro[1]}')
         except:
            print("Circulo: Ponto de centro nao encontrado")
         try:
            xmlRaio = float(geo.getElementsByTagName('Raio')[0].childNodes[0].data)
            #print(f'Circulo: Raio é: {xmlRaio}')
         except:
            print("Circulo: Raio nao encontrado")
         try:
            xmlCor = geo.getElementsByTagName('Cor')[0]
            xmlCorR = int(xmlCor.getElementsByTagName('R')[0].childNodes[0].data)
            xmlCorG = int(xmlCor.getElementsByTagName('G')[0].childNodes[0].data)
            xmlCorB = int(xmlCor.getElementsByTagName('B')[0].childNodes[0].data)
            #conversao pra hex com #
            if(xmlCorR > 15):
               xmlCorR = f'{hex(xmlCorR)[2]}{hex(xmlCorR)[3]}'
            else:
               xmlCorR = f'0{hex(xmlCorR)[2]}'
            if(xmlCorG > 15):
               xmlCorG = f'{hex(xmlCorG)[2]}{hex(xmlCorG)[3]}'
            else:
               xmlCorG = f'0{hex(xmlCorG)[2]}'
            if(xmlCorB > 15):
               xmlCorB = f'{hex(xmlCorB)[2]}{hex(xmlCorB)[3]}'
            else:
               xmlCorB = f'0{hex(xmlCorB)[2]}'
            xmlCor = f'#{xmlCorR}{xmlCorG}{xmlCorB}'
            #print(f'Circulo: Cor é: {xmlCor}')
            del xmlCorR
            del xmlCorG
            del xmlCorB
            COR_SELETA = xmlCor
            corConfig.config(background=COR_SELETA)
            bmCorConfig.config(background=COR_SELETA)
         except:
            print("Circulo: Cor nao encontrada")
         try:
            xmlEspessura = int(geo.getElementsByTagName('Espessura')[0].childNodes[0].data)
            #print(f'Circulo: Espessura é: {xmlEspessura}')
            ESPESSURA_SELETA = xmlEspessura
         except:
            print("Circulo: Espessura nao encontrada")
         circulo = CirculoGr( xmlCentro[0], xmlCentro[1], xmlRaio, COR_SELETA, ESPESSURA_SELETA)
         circulo.desenhaCirculoMidPoint(desenhoQuadro)
         historicoQuadro.append(circulo)
         circulinho = CirculoGr( xmlCentro[0]/3, xmlCentro[1]/3, xmlRaio/3, COR_SELETA, ESPESSURA_SELETA/3)
         circulinho.desenhaCirculoMidPoint(desenhoMapa)
         historicoMapa.append(circulo)


      if(geo.nodeName == 'Poligono'):
         #print(f'Tem um poligono')
         pass
   print(f'Historico com {len(historicoQuadro)} geometrias')

def desenhaHistorico():
   for geo in historicoQuadro:
      try:
         geo.desenhaLine(desenhoQuadro)
         #geo.desenhaLine(desenhoMapa)
         print("eh linha")
      except:
         pass
      try:
         geo.desenhaCirculoMidPoint(desenhoQuadro)
         #geo.desenhaCirculoMidPoint(desenhoMapa)
         print("eh circulo")
      except:
         pass
      try:
         geo.desenhaPonto(desenhoQuadro)
         #geo.desenhaPonto(desenhoMapa)
         print("eh ponto")
      except:
         pass
   for geo in historicoMapa:
      try:
         geo.desenhaLine(desenhoMapa)
         #geo.desenhaLine(desenhoMapa)
         print("eh linha")
      except:
         pass
      try:
         geo.desenhaCirculoMidPoint(desenhoMapa)
         #geo.desenhaCirculoMidPoint(desenhoMapa)
         print("eh circulo")
      except:
         pass
      try:
         geo.desenhaPonto(desenhoMapa)
         #geo.desenhaPonto(desenhoMapa)
         print("eh ponto")
      except:
         pass
         
def sobre():
   #nem funciona, mas pq?
   #ta faltando o geometry tb
   sobre = Toplevel(root, bg=STD_BG, height=500, width=350)
   #toplevel eh uma janela que abre inrriba da outra, puxa o foco
   junto = Frame(sobre, bg=sobre['bg'])
   junto.pack(expand=True, fill=BOTH)
   
   sImg = PhotoImage(file='icons/Pepeg.gif')
   pepeg = Label(junto, image=sImg, bg=sobre['bg'])
   pepeg.grid(row=0, column=0)

   sobreTexto = f'Feito por:\nEmerson B Grisi\nCarlos Eduardo Freitas\nCaio Furtado\nGabriel França\n'
   anuncio = Label(junto, text=sobreTexto, bg=sobre['bg'], fg=BOTAO_FG)
   #anuncio.grid(row=1, column=0)
 
#ORGANIZACOES DE MENU
#menu arquivo
menuBarra = Menu(root)
menuArquivo = Menu(menuBarra, tearoff=0)
menuArquivo.add_command(label="Novo", command=novoQuadro)
menuArquivo.add_command(label="Abrir", command=inputArquivo)
menuArquivo.add_command(label="Salvar", command=salvaHistorico)
menuArquivo.add_command(label="Salvar como...", command=donothing)
menuArquivo.add_command(label="Fechar", command=donothing)
menuArquivo.add_separator()
menuArquivo.add_command(label="Sair", command=root.quit)
menuBarra.add_cascade(label="Arquivo", menu=menuArquivo)

#menu editar
menuEditar = Menu(menuBarra, tearoff=0)
menuEditar.add_command(label="Desfazer", command=donothing)
menuEditar.add_separator()
menuEditar.add_command(label="Recortar", command=donothing)
menuEditar.add_command(label="Copiar", command=donothing)
menuEditar.add_command(label="Colar", command=donothing)
menuEditar.add_command(label="Apagar", command=donothing)
menuEditar.add_command(label="Selecionar Tudo", command=donothing)
menuBarra.add_cascade(label="Editar", menu=menuEditar)

#menu ajuda
menuAjuda = Menu(menuBarra, tearoff=0)
menuAjuda.add_command(label="Documentação", command=donothing)
menuAjuda.add_command(label="Sobre...", command=sobre)
menuBarra.add_cascade(label="Ajuda", menu=menuAjuda)

#aplica o menu
root.config(menu=menuBarra)

#janela.mainloop()