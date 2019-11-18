from tkinter import *
from tkinter import ttk
from tkinter.colorchooser import askcolor
from time import *
from pontoGr import *
from retaGr import *
from circuloGr import *
from math import *
from xml.dom.minidom import *
from xml.dom.minidom import parse
#from xml.etree import ElementTree

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
historico = []

root = Tk()
root.config(width=STD_LARGURA, height=STD_ALTURA)
root.title("PobroShop")
geo = f'{STD_LARGURA}x{STD_ALTURA}+50+50'
root.geometry(geo)
root.minsize(STD_LARGURA, STD_ALTURA)
#root.maxsize(STD_LARGURA, STD_ALTURA)
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

def toTuplaCor(hashtagCor=COR_SELETA):
   red =   int(f'{hashtagCor[1]}{hashtagCor[2]}',16)
   green = int(f'{hashtagCor[3]}{hashtagCor[4]}',16)
   blue =  int(f'{hashtagCor[5]}{hashtagCor[6]}',16)
   cor = (red,green,blue)
   return cor

def toHashCor(tuplaCor):
   hexOR=f'{hex(tuplaCor[0])}'
   hexOG=f'{hex(tuplaCor[1])}'
   hexOB=f'{hex(tuplaCor[2])}'
   if(tuplaCor[0] > 15):
      r = f'{hexOR[2]}{hexOR[3]}'
   else:
      r = f'0{hexOR[2]}'
   if(tuplaCor[1] > 15):
      g = f'{hexOG[2]}{hexOG[3]}'
   else:
      g = f'0{hexOG[2]}'
   if(tuplaCor[2] > 15):
      b = f'{hexOB[2]}{hexOB[3]}'
   else:
      b = f'0{hexOB[2]}'
   return f'#{r}{g}{b}'

#funcoes pra salvar xml
def toXML(app):
   tipo = app[0]
   cor = toTuplaCor(app[1])
   str = "Erro no toXML."
   if(tipo is 'ponto'):
      #formato do professor:
      #nao tem
      #Formato Historico:
      #['ponto','#cor',esp,x,y]
      str=f'<Ponto>'
      str+=f'<x>{app[3]/desenhoQuadro.winfo_width()}</x><y>{app[4]/desenhoQuadro.winfo_height()}</y>'
      str+=f'<Cor><R>{cor[0]}</R><G>{cor[1]}</G><B>{cor[2]}</B></Cor>'
      #str+=f'<Espessura>{app[2]}</Espessura>\n'
      str+=f'</Ponto>'
      
   elif(tipo is 'reta'):
      #formato do professor:
      '''
      <Reta>
      <Ponto><x>0.2076923076923077</x><y>0.698076923076923</y></Ponto>
      <Ponto><x>0.21153846153846154</x><y>0.6961538461538461</y></Ponto>
      <Cor><R>0</R><G>0</G><B>0</B></Cor>
      </Reta>
      '''
      #Formato Historico:
      #['reta','#cor',esp,x1,y1,x2,y2]
      str=f'<Reta>'
      str+=f'<Ponto><x>{app[3]/desenhoQuadro.winfo_width()}</x><y>{app[4]/desenhoQuadro.winfo_height()}</y></Ponto>'
      str+=f'<Ponto><x>{app[5]/desenhoQuadro.winfo_width()}</x><y>{app[6]/desenhoQuadro.winfo_height()}</y></Ponto>'
      str+=f'<Cor><R>{cor[0]}</R><G>{cor[1]}</G><B>{cor[2]}</B></Cor>'
      #str+=f'<Espessura>{app[2]}</Espessura>\n'
      str+=f'</Reta>'
   elif(tipo is 'circulo'):
      #formato do professor:
      '''
      <Circulo>
      <Ponto><x>0.4403846153846154</x><y>0.17884615384615385</y></Ponto>
      <Raio>0.25566076358233575</Raio>
      <Cor><R>255</R><G>50</G><B>100</B></Cor>
      </Circulo>
      '''
      #Formato Historico:
      #['circulo','#cor',esp,cx,cy,raio]
      str=f'<Circulo>'
      str+=f'<Ponto><x>{app[3]/desenhoQuadro.winfo_width()}</x><y>{app[4]/desenhoQuadro.winfo_height()}</y></Ponto>'
      str+=f'<Raio>{app[5]/desenhoQuadro.winfo_width()}</Raio>'
      str+=f'<Cor><R>{cor[0]}</R><G>{cor[1]}</G><B>{cor[2]}</B></Cor>'
      #str+=f'<Espessura>{app[2]}</Espessura>\n'
      str+=f'</Circulo>'
   elif(tipo is 'retangulo'):
      #formato do professor:
      '''
      <Retangulo>
      <Ponto><x>0.6288461538461538</x><y>0.16538461538461538</y></Ponto>
      <Ponto><x>0.95</x><y>0.4326923076923077</y></Ponto>
      <Cor><R>0</R><G>50</G><B>100</B></Cor>
      </Retangulo>
      '''
      #Formato Historico:
      #['retangulo','#cor',esp,ax,ay,bx,by]
      str=f'<Retangulo>'
      str+=f'<Ponto><x>{app[3]/desenhoQuadro.winfo_width()}</x><y>{app[4]/desenhoQuadro.winfo_height()}</y></Ponto>'
      str+=f'<Ponto><x>{app[5]/desenhoQuadro.winfo_width()}</x><y>{app[6]/desenhoQuadro.winfo_height()}</y></Ponto>'
      str+=f'<Cor><R>{cor[0]}</R><G>{cor[1]}</G><B>{cor[2]}</B></Cor>'
      #str+=f'<Espessura>{app[2]}</Espessura>\n'
      str+=f'</Retangulo>'
   elif(tipo is 'poligono'):
      #formato do professor
      '''
      <Poligono>
      <Ponto><x>0.14615384615384616</x><y>0.12115384615384615</y></Ponto>
      ...
      <Ponto><x>0.06538461538461539</x><y>0.3211538461538462</y></Ponto>
      <Cor><R>0</R><G>50</G><B>100</B></Cor>
      </Poligono>
      '''
      #Formato Historico:
      #['poligono','#cor',esp,ps[]]
      str=f'<Poligono>'
      for ponto in app[3]:
         str+=f'<Ponto><x>{ponto[0]/desenhoQuadro.winfo_width()}</x><y>{ponto[1]/desenhoQuadro.winfo_height()}</y></Ponto>'
      str+=f'<Cor><R>{cor[0]}</R><G>{cor[1]}</G><B>{cor[2]}</B></Cor>'
      #str+=f'<Espessura>{app[2]}</Espessura>\n'
      str+=f'</Poligono>'
   #print(str)
   return str

def salvarHistoricoXML(xmlArqOut='output.xml'):
   with open(xmlArqOut, 'w') as file:
      histXml = f'<?xml version="1.0" encoding="UTF-8" standalone="no"?><Figura>'
      for forma in historico:
         histXml+=toXML(forma)
      #print(histXml)
      histXml+=f'</Figura>'
      file.write(histXml)
      file.close()

#funcoes de desenho

def fazReta(ax, ay, bx, by, cor=COR_SELETA, esp=ESPESSURA_SELETA, seQuadro=True, seMapa=True, seHist=True):
   global historico
   global desenhoQuadro
   global desenhoMapa
   global ESPESSURA_SELETA
   global COR_SELETA
   global pilhaGeo
   if(seQuadro is True):
      reta = RetaGr(int(ax), int(ay), int(bx), int(by), cor, esp)
      reta.desenhaLine(desenhoQuadro)
      if(esp >= 4):
         raioM=esp/2
         cx=ax-raioM
         cy=ay+raioM
         lx=ax+raioM
         ly=ay-raioM
         desenhoQuadro.create_oval(cx, cy, lx, ly, tag=('forma','Reta'), outline=cor, fill=cor)
         raioM=esp/2
         cx=bx-raioM
         cy=by+raioM
         lx=bx+raioM
         ly=by-raioM
         desenhoQuadro.create_oval(cx, cy, lx, ly, tag=('forma','Reta'), outline=cor, fill=cor)
         del raioM
         del cx
         del cy
         del lx
         del ly
      del reta
   if(seMapa is True):
      #mapeamento
      propY = desenhoMapa.winfo_height()/desenhoQuadro.winfo_height()
      propX = desenhoMapa.winfo_width()/desenhoQuadro.winfo_width()
      prop = (propY+propX)/2
      #desenho
      reta = RetaGr(float(ax)*propX, float(ay)*propY, float(bx)*propX, float(by)*propY, cor, esp*prop)
      reta.desenhaLine(desenhoMapa)
      del reta
      if(esp >= 4):
         raioM=esp/2
         cx=ax-raioM
         cy=ay+raioM
         lx=ax+raioM
         ly=ay-raioM
         desenhoMapa.create_oval(cx*propX, cy*propY, lx*propX, ly*propY, tag=('forma','Reta'), outline=cor, fill=cor)
         raioM=esp/2
         cx=bx-raioM
         cy=by+raioM
         lx=bx+raioM
         ly=by-raioM
         desenhoMapa.create_oval(cx*propX, cy*propY, lx*propX, ly*propY, tag=('forma','Reta'), outline=cor, fill=cor)
         del raioM
         del cx
         del cy
         del lx
         del ly
   if(seHist is True):
      forma = ['reta', cor, esp, ax, ay, bx, by]
      historico.append(forma)
      del forma

      
def fazCirculo(cx, cy, r, cor=COR_SELETA, esp=ESPESSURA_SELETA, seQuadro=True, seMapa=True, seHist=True):
   global historico
   global desenhoQuadro
   global desenhoMapa
   global ESPESSURA_SELETA
   global COR_SELETA
   global pilhaGeo
   if(seQuadro is True):
      circulo = CirculoGr(cx, cy, r, cor, esp)
      #circulo.desenhaCirculoMidPoint(desenhoQuadro)
      circulo.desenhaCircle(desenhoQuadro)
      del circulo
   if(seMapa is True):
      #mapeamento
      propY = desenhoMapa.winfo_height()/desenhoQuadro.winfo_height()
      propX = desenhoMapa.winfo_width()/desenhoQuadro.winfo_width()
      prop = (propY+propX)/2
      #desenho
      circulo = CirculoGr(float(cx)*propX, float(cy)*propY, r*prop, cor, esp*prop)
      circulo.desenhaCircle(desenhoMapa)
      #circulo.desenhaCirculoMidPoint(desenhoMapa)
      del circulo
   if(seHist is True):
      forma = ['circulo', cor, esp, cx, cy, r]
      historico.append(forma)
      del forma

def fazRetangulo(ax, ay, bx, by, cor=COR_SELETA, esp=ESPESSURA_SELETA, seQuadro=True, seMapa=True, seHist=True):
   global historico
   global desenhoQuadro
   global desenhoMapa
   global ESPESSURA_SELETA
   global COR_SELETA
   global pilhaGeo
   
   if(seQuadro is True):
      desenhoQuadro.create_polygon(ax, ay, bx, ay, bx, by, ax, by, ax, ay, tag=('forma','Retângulo'), width=esp, outline=cor, fill='')
   if(seMapa is True):
      #mapeamento
      propY = desenhoMapa.winfo_height()/desenhoQuadro.winfo_height()
      propX = desenhoMapa.winfo_width()/desenhoQuadro.winfo_width()
      prop = (propY+propX)/2
      #desenho
      #circulo = CirculoGr(float(cx)*propX, float(cy)*propY, r*prop, cor, esp*prop)
      desenhoMapa.create_polygon(ax*propX, ay*propY, bx*propX, ay*propY, bx*propX, by*propY, ax*propX, by*propY, ax*propX, ay*propY, tag=('forma','Retângulo'), width=esp*prop, outline=cor, fill='')
   #fazReta(ax, ay, bx, ay, cor, esp, seQuadro, seMapa, False)
   #fazReta(ax, ay, ax, by, cor, esp, seQuadro, seMapa, False)
   #fazReta(ax, by, bx, by, cor, esp, seQuadro, seMapa, False)
   #fazReta(bx, ay, bx, by, cor, esp, seQuadro, seMapa, False)
   if(seHist is True):
      forma = ['retangulo', cor, esp, ax, ay, bx, by]
      historico.append(forma)
      del forma
      
#movi a ponto pra baixo pra poder economizar tempo fazendo as outras
def fazPonto(x, y, cor=COR_SELETA, esp=ESPESSURA_SELETA, seQuadro=True, seMapa=True, seHist=True):
   global historico
   global desenhoQuadro
   global desenhoMapa
   global ESPESSURA_SELETA
   global COR_SELETA
   global pilhaGeo
   #se o prof nao implementa ponto, faz uma reta de 1 ponto
   #mas a espessura eh sempre a mesma
   temPonto = False
   if(seQuadro is True):
      if(temPonto is True):
         ponto = PontoGr(x,y, cor, esp)
         ponto.origem(-1000, -1000)
         ponto.desenhaPonto(desenhoQuadro)
         del ponto
      else:
         fazCirculo(x, y, 1, cor, esp, True, True, True)
   if(seMapa is True):
      #mapeamento
      propY = desenhoMapa.winfo_height()/desenhoQuadro.winfo_height()
      propX = desenhoMapa.winfo_width()/desenhoQuadro.winfo_width()
      prop = (propY+propX)/2
      xm=round(x*propX)
      ym=round(y*propY)
      espm=round(esp*prop)
      if(temPonto is True):
         #desenho
         ponto = PontoGr(xm,ym, cor, espm)
         ponto.origem(-1000, -1000)
         ponto.desenhaPonto(desenhoMapa)
         del ponto
   if(seHist is True):
      if(temPonto is True):
         forma = ['ponto', cor, esp, x, y]
         historico.append(forma)
         del forma

def fazPoligono(ps, cor=COR_SELETA, esp=ESPESSURA_SELETA, seQuadro=True, seMapa=True, seHist=True):
   global historico
   global desenhoQuadro
   global desenhoMapa
   global ESPESSURA_SELETA
   global COR_SELETA
   global pilhaGeo
   
   if(seQuadro is True):
      desenhoQuadro.create_polygon(ps, tag=('forma','Poligono'), width=esp, outline=cor, fill='')
   if(seMapa is True):
      #mapeamento
      propY = desenhoMapa.winfo_height()/desenhoQuadro.winfo_height()
      propX = desenhoMapa.winfo_width()/desenhoQuadro.winfo_width()
      prop = (propY+propX)/2
      #print(ps)
      listaM = []
      for ponto in ps :
         pontoM = []
         pontoM.append(ponto[0]*propX)
         pontoM.append(ponto[1]*propY)
         listaM.append(pontoM)
      #print(ps)
      listaM.append(listaM[0])
      desenhoMapa.create_polygon(listaM, tag=('forma','Poligono'), width=esp*prop, outline=cor, fill='')
   if(seHist is True):
      forma = ['poligono', cor, esp, ps]
      historico.append(forma)
      del forma
   
   '''
   primeiro = ps[0]
   ultimo = ps[0]
   for pto in ps:
      fazReta(ultimo[0], ultimo[1], pto[0], pto[1], cor, esp, seQuadro, seMapa, False)
      ultimo = pto
   fazReta(ultimo[0], ultimo[1], primeiro[0], primeiro[1], cor, esp, seQuadro, seMapa, False)
   if(seHist is True):
      forma = ['poligono', cor, esp, ps]
      historico.append(forma)
      del forma
   '''

def cliqueDesenho(event):
   global desenhoQuadro
   global desenhoMapa
   global pilhaGeo
   global historico
   infoStatus.config(bitmap="warning")
   str_status = f'Ferramenta {ferramenta}: Clique em {event.x},{event.y} do Desenho. '
   msg.config(text=str_status)
   if(ferramenta=="Mão"):
      pilhaGeo.clear()
   elif(ferramenta=="Poligono"):
      print("Desenhar poligono aqui")
      
   elif(ferramenta=="Ponto"):
      pilhaGeo.clear()
      fazPonto(event.x,event.y, COR_SELETA, ESPESSURA_SELETA)
      msg.config(text=str_status+f'Desenhei um ponto! Cor: {COR_SELETA} e Espessura:{ESPESSURA_SELETA}')
   elif(ferramenta=="Reta"):
      #se a pilha ta vazia adiciona senao faz o desenho
      if(len(pilhaGeo)==0):
         ponto = (event.x,event.y)
         pilhaGeo.append(ponto)
         msg.config(text=str_status+f'Guardei um ponto da reta! Em {ponto[0]},{ponto[1]}')
         del ponto
      else:
         ponto = (event.x,event.y)
         fazReta(pilhaGeo[0][0],pilhaGeo[0][1],ponto[0],ponto[1], COR_SELETA, ESPESSURA_SELETA)
         pilhaGeo.clear()
         msg.config(text=str_status+f'Desenhei uma reta! Cor: {COR_SELETA} e Espessura:{ESPESSURA_SELETA}')
   elif(ferramenta=="Círculo"):
      #global pilhaGeo
      if(len(pilhaGeo)==0):
         ponto = (event.x,event.y)
         pilhaGeo.append(ponto)
         msg.config(text=str_status+f'Guardei o centro!  Em {ponto[0]},{ponto[1]}')
         del ponto
      else:
         raioP = (event.x,event.y)
         centro = (pilhaGeo[0][0],pilhaGeo[0][1])
         raio = (sqrt((raioP[0]-centro[0])*(raioP[0]-centro[0])+(raioP[1]-centro[1])*(raioP[1]-centro[1])))
         pilhaGeo.clear()
         fazCirculo(centro[0],centro[1],raio, COR_SELETA, ESPESSURA_SELETA)
         msg.config(text=str_status+f'Desenhei Circulo! raio: {round(raio)} e centro: {centro[0]},{centro[1]}')
   elif(ferramenta=="Retângulo"):
      #se a pilha ta vazia adiciona senao faz o desenho
      if(len(pilhaGeo)==0):
         ponto = (event.x,event.y)
         pilhaGeo.append(ponto)
         msg.config(text=str_status+f'Guardei um ponto do retangulo! Em {ponto[0]},{ponto[1]}')
         del ponto
      else:
         ponto = (event.x,event.y)
         fazRetangulo(pilhaGeo[0][0],pilhaGeo[0][1],ponto[0],ponto[1], COR_SELETA, ESPESSURA_SELETA)
         pilhaGeo.clear()
         msg.config(text=str_status+f'Desenhei um retangulo! Cor: {COR_SELETA} e Espessura:{ESPESSURA_SELETA}')
   elif(ferramenta=="Lapis"):
      pilhaGeo.clear()
      #fazPonto(event.x,event.y, COR_SELETA, ESPESSURA_SELETA)
      msg.config(text=str_status+f'Desenhei um ponto! Cor: {COR_SELETA} e Espessura:{ESPESSURA_SELETA}')
   elif(ferramenta=="Spray"):
      pilhaGeo.clear()
      fazPonto(event.x,event.y, COR_SELETA, ESPESSURA_SELETA)
      msg.config(text=str_status+f'Desenhei um ponto! Cor: {COR_SELETA} e Espessura:{ESPESSURA_SELETA}')


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
   elif(ferramenta=="Retângulo"):
      pass
   elif(ferramenta=="Lapis"):
      if(len(pilhaGeo)==0):
         ponto = (event.x, event.y)
         pilhaGeo.append(ponto)
      else:
         ponto = (event.x,event.y)
         
         fazReta(ponto[0], ponto[1], pilhaGeo[0][0], pilhaGeo[0][1], COR_SELETA, ESPESSURA_SELETA)
         '''
         if(ESPESSURA_SELETA >= 4):
            raioM=ESPESSURA_SELETA/2
            tx=ponto[0]-raioM
            ty=ponto[1]+raioM
            ax=ponto[0]+raioM
            ay=ponto[1]-raioM
            desenhoQuadro.create_oval(tx, ty, ax, ay, tag=('forma','Reta'), outline=COR_SELETA, fill=COR_SELETA)
         #'''
         pilhaGeo.clear()
         pilhaGeo.append(ponto)
         msg.config(text=str_status+f'Risquei uma linha! Cor: {COR_SELETA} e Espessura:{ESPESSURA_SELETA}')
   elif(ferramenta=="Spray"):
      fazPonto(event.x,event.y, COR_SELETA, ESPESSURA_SELETA)
      msg.config(text=str_status+f'Pichei um ponto! Cor: {COR_SELETA} e Espessura:{ESPESSURA_SELETA}')

#talvez de pra criar so uma classe dessas funcoes ?
def cliqueMapa(event):
   infoStatus.config(bitmap="warning")
   msg.config(text=f'Clique em {event.x},{event.y} do Mapa.')
def hoverMapa(event):
   coordS.config(text=f'({event.x}, {event.y})')
def mudouTam(event):
   infoStatus.config(bitmap="warning")
   #TODO remapeamento
   remap()
   msg.config(text=f'Quadro mudou de tamanho: {event.width}x{event.height}')

def remap():
   desenhaHistorico(False,True)

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
   pilhaGeo.clear()
   
def poligono():
   global ferramenta
   ferramenta = "Poligono"
   for f in ferram:
      if(f!='poligono'):ferram[f].config(state=ACTIVE, relief=RAISED)
   ferram['poligono'].config(state=DISABLED, relief=SUNKEN)
   desenhoQuadro.config(cursor="tcross")
   pilhaGeo.clear()
   
def ponto():
   global ferramenta
   ferramenta = "Ponto"
   for f in ferram:
      if(f!='ponto'):ferram[f].config(state=ACTIVE, relief=RAISED)
   ferram['ponto'].config(state=DISABLED, relief=SUNKEN)
   desenhoQuadro.config(cursor="circle")
   pilhaGeo.clear()
   
def reta():
   global ferramenta
   ferramenta = "Reta"
   for f in ferram:
      if(f!='reta'):ferram[f].config(state=ACTIVE, relief=RAISED)
   ferram['reta'].config(state=DISABLED, relief=SUNKEN)
   desenhoQuadro.config(cursor="circle")
   pilhaGeo.clear()
   
def circulo():
   global ferramenta
   ferramenta = "Círculo"
   for f in ferram:
      if(f!='circulo'):ferram[f].config(state=ACTIVE, relief=RAISED)
   ferram['circulo'].config(state=DISABLED, relief=SUNKEN)
   desenhoQuadro.config(cursor="circle")
   pilhaGeo.clear()
   
def retangulo():
   global ferramenta
   ferramenta = "Retângulo"
   for f in ferram:
      if(f!='retangulo'):ferram[f].config(state=ACTIVE, relief=RAISED)
   ferram['retangulo'].config(state=DISABLED, relief=SUNKEN)
   desenhoQuadro.config(cursor="tcross")
   pilhaGeo.clear()
   
def lapis():
   global ferramenta
   ferramenta = "Lapis"
   for f in ferram:
      if(f!='lapis'):ferram[f].config(state=ACTIVE, relief=RAISED)
   ferram['lapis'].config(state=DISABLED, relief=SUNKEN)
   desenhoQuadro.config(cursor="pencil")
   pilhaGeo.clear()
   
def spray():
   global ferramenta
   ferramenta = "Spray"
   for f in ferram:
      if(f!='spray'):ferram[f].config(state=ACTIVE, relief=RAISED)
   ferram['spray'].config(state=DISABLED, relief=SUNKEN)
   desenhoQuadro.config(cursor="spraycan")
   pilhaGeo.clear()

#imagens dos botoes:
bmMao=      BitmapImage(file="icons/mao.xbm", background=BOTAO_BG, foreground=BOTAO_FG)
bmPoligono= BitmapImage(file="icons/poligono.xbm", background=BOTAO_BG, foreground=BOTAO_FG)
bmPonto=    BitmapImage(file="icons/ponto.xbm", background=BOTAO_BG, foreground=BOTAO_FG)
bmReta=     BitmapImage(file="icons/reta.xbm", background=BOTAO_BG, foreground=BOTAO_FG)
bmCirculo=  BitmapImage(file="icons/circulo.xbm", background=BOTAO_BG, foreground=BOTAO_FG)
bmRetangulo=BitmapImage(file="icons/retangulo.xbm", background=BOTAO_BG, foreground=BOTAO_FG)
bmLapis=    BitmapImage(file="icons/lapis.xbm", background=BOTAO_BG, foreground=BOTAO_FG)
bmSpray=    BitmapImage(file="icons/spray.xbm", background=BOTAO_BG, foreground=BOTAO_FG)

#setup: command chama a funcao dele, que ja troca o cursor no desenho e levanta e abaixa os botoes
ferram = {
   'mao':      Button(ferrEsq, command = mao, bd=BOTAO_BD, image=bmMao, state=DISABLED, relief=SUNKEN, bg=BOTAO_BG, fg=BOTAO_FG, activeforeground=BOTAO_FG, activebackground=BOTAO_BG),
   'poligono': Button(ferrEsq, command = poligono, bd=BOTAO_BD, image=bmPoligono, state=ACTIVE, relief=RAISED, bg=BOTAO_BG, fg=BOTAO_FG, activeforeground=BOTAO_FG, activebackground=BOTAO_BG),
   'ponto':    Button(ferrEsq, command = ponto, bd=BOTAO_BD, image=bmPonto, state=ACTIVE, relief=RAISED, bg=BOTAO_BG, fg=BOTAO_FG, activeforeground=BOTAO_FG, activebackground=BOTAO_BG),
   'reta':     Button(ferrEsq, command = reta, bd=BOTAO_BD, image=bmReta, state=ACTIVE, relief=RAISED, bg=BOTAO_BG, fg=BOTAO_FG, activeforeground=BOTAO_FG, activebackground=BOTAO_BG),
   'circulo':  Button(ferrEsq, command = circulo, bd=BOTAO_BD, image=bmCirculo, state=ACTIVE, relief=RAISED, bg=BOTAO_BG, fg=BOTAO_FG, activeforeground=BOTAO_FG, activebackground=BOTAO_BG),
   'retangulo':Button(ferrEsq, command = retangulo, bd=BOTAO_BD, image=bmRetangulo, state=ACTIVE, relief=RAISED, bg=BOTAO_BG, fg=BOTAO_FG, activeforeground=BOTAO_FG, activebackground=BOTAO_BG),
   'lapis':    Button(ferrEsq, command = lapis, bd=BOTAO_BD, image=bmLapis, state=ACTIVE, relief=RAISED, bg=BOTAO_BG, fg=BOTAO_FG, activeforeground=BOTAO_FG, activebackground=BOTAO_BG),
   'spray':    Button(ferrEsq, command = spray, bd=BOTAO_BD, image=bmSpray, state=ACTIVE, relief=RAISED, bg=BOTAO_BG, fg=BOTAO_FG, activeforeground=BOTAO_FG, activebackground=BOTAO_BG)
   }
#posicionamento em grid (uma row)
ferram['mao'].grid(row=0, column=0)
ferram['poligono'].grid(row=0, column=1)
ferram['ponto'].grid(row=0, column=2)
ferram['reta'].grid(row=0, column=3)
ferram['circulo'].grid(row=0, column=4)
ferram['retangulo'].grid(row=0, column=5)
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
   historico.clear()
   desenhoQuadro.delete("all")
   desenhoMapa.delete("all")
   
def inputArquivo(nomeArq='input.xml'):
   global historico
   global COR_SELETA
   global ESPESSURA_SELETA
   global desenhoQuadro
   global desenhoMapa
   
   historico.clear()
   desenhoQuadro.delete("all")
   desenhoMapa.delete("all")
   
   # Try and Open XML document using minidom parser
   try:
      DOMTree = xml.dom.minidom.parse(nomeArq)
   except:
      print(f'falha ao abrir o {nomeArq}, criando um novo')
      with open(nomeArq, 'w') as file:
         file.write('<?xml version="1.0" encoding="UTF-8" standalone="no"?><Figura></Figura>')
      DOMTree = xml.dom.minidom.parse(nomeArq)
   
   figura = DOMTree.documentElement
   print(f'Figura XML com {len(figura.childNodes)} formas')
   for geo in figura.childNodes[:]:
      if(geo.nodeName == 'Ponto'):
         #print(f'Tem um ponto:')
         try:
            xmlX = float(geo.getElementsByTagName('x')[0].childNodes[0].data)
            xmlY = float(geo.getElementsByTagName('y')[0].childNodes[0].data)
            xmlP = [xmlX, xmlY]
            del xmlX
            del xmlY
            xmlP[0] = round(xmlP[0]*desenhoQuadro.winfo_width())
            xmlP[1] = round(xmlP[1]*desenhoQuadro.winfo_width())
            #print(f'Ponto: Ponto é: {xmlP[0]},{xmlP[1]}')
         except:
            print("Ponto: X e Y nao encontrado")
         try:
            xmlCor = geo.getElementsByTagName('Cor')[0]
            xmlCor = (int(xmlCor.getElementsByTagName('R')[0].childNodes[0].data),
                      int(xmlCor.getElementsByTagName('G')[0].childNodes[0].data),
                      int(xmlCor.getElementsByTagName('B')[0].childNodes[0].data))
            COR_SELETA = toHashCor(xmlCor)
            corConfig.config(background=COR_SELETA)
            bmCorConfig.config(background=COR_SELETA)
         except:
            print("Ponto: Cor nao encontrada")
         try:
            xmlEspessura = int(geo.getElementsByTagName('Espessura')[0].childNodes[0].data)
            #print(f'Ponto: Espessura é: {xmlEspessura}')
            ESPESSURA_SELETA = xmlEspessura
         except:
            pass
            #print("Ponto: Espessura nao encontrada")
         fazPonto(xmlP[0],xmlP[1], COR_SELETA, ESPESSURA_SELETA)
      
      elif(geo.nodeName == 'Reta'):
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
            xmlCor = (int(xmlCor.getElementsByTagName('R')[0].childNodes[0].data),
                      int(xmlCor.getElementsByTagName('G')[0].childNodes[0].data),
                      int(xmlCor.getElementsByTagName('B')[0].childNodes[0].data))
            COR_SELETA = toHashCor(xmlCor)
            corConfig.config(background=COR_SELETA)
            bmCorConfig.config(background=COR_SELETA)
         except:
            print("Reta: Cor nao encontrada")
         try:
            xmlEspessura = int(geo.getElementsByTagName('Espessura')[0].childNodes[0].data)
            #print(f'Reta: Espessura é: {xmlEspessura}')
            ESPESSURA_SELETA = xmlEspessura
         except:
            pass
            #print("Reta: Espessura nao encontrada")
         fazReta(xmlPA[0], xmlPA[1], xmlPB[0], xmlPB[1], COR_SELETA, ESPESSURA_SELETA)
         
      elif(geo.nodeName == 'Circulo'):
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
            xmlRaio = float(geo.getElementsByTagName('Raio')[0].childNodes[0].data)*desenhoQuadro.winfo_width()
            #print(f'Circulo: Raio é: {xmlRaio}')
         except:
            print("Circulo: Raio nao encontrado")
         try:
            xmlCor = geo.getElementsByTagName('Cor')[0]
            xmlCor = (int(xmlCor.getElementsByTagName('R')[0].childNodes[0].data),
                      int(xmlCor.getElementsByTagName('G')[0].childNodes[0].data),
                      int(xmlCor.getElementsByTagName('B')[0].childNodes[0].data))
            COR_SELETA = toHashCor(xmlCor)
            corConfig.config(background=COR_SELETA)
            bmCorConfig.config(background=COR_SELETA)
         except:
            print("Circulo: Cor nao encontrada")
         try:
            xmlEspessura = int(geo.getElementsByTagName('Espessura')[0].childNodes[0].data)
            #print(f'Circulo: Espessura é: {xmlEspessura}')
            ESPESSURA_SELETA = xmlEspessura
         except:
            pass
            #print("Circulo: Espessura nao encontrada")
         #verificar se o raio esta desnormalizado!
         fazCirculo(xmlCentro[0], xmlCentro[1], xmlRaio, COR_SELETA, ESPESSURA_SELETA)
         
      elif(geo.nodeName == 'Retangulo'):
         #print(f'Tem um retangulo:')
         try:
            xmlPA = geo.getElementsByTagName('Ponto')[0]
            xmlX = float(xmlPA.getElementsByTagName('x')[0].childNodes[0].data)
            xmlY = float(xmlPA.getElementsByTagName('y')[0].childNodes[0].data)
            xmlPA = [xmlX, xmlY]
            del xmlX
            del xmlY
            xmlPA[0] = int(xmlPA[0]*desenhoQuadro.winfo_width())
            xmlPA[1] = int(xmlPA[1]*desenhoQuadro.winfo_width())
            #print(f'Retangulo: Ponto A é: {xmlPA[0]},{xmlPA[1]}')
         except:
            print("Retangulo: Ponto A nao encontrado")
         try:
            xmlPB = geo.getElementsByTagName('Ponto')[1]
            xmlX = float(xmlPB.getElementsByTagName('x')[0].childNodes[0].data)
            xmlY = float(xmlPB.getElementsByTagName('y')[0].childNodes[0].data)
            xmlPB = [xmlX, xmlY]
            del xmlX
            del xmlY
            xmlPB[0] = int(xmlPB[0]*desenhoQuadro.winfo_width())
            xmlPB[1] = int(xmlPB[1]*desenhoQuadro.winfo_width())
            #print(f'Retangulo: Ponto B é: {xmlPB[0]},{xmlPB[1]}')
         except:
            print("Retangulo: Ponto B nao encontrado")
         try:
            xmlCor = geo.getElementsByTagName('Cor')[0]
            xmlCor = (int(xmlCor.getElementsByTagName('R')[0].childNodes[0].data),
                      int(xmlCor.getElementsByTagName('G')[0].childNodes[0].data),
                      int(xmlCor.getElementsByTagName('B')[0].childNodes[0].data))
            COR_SELETA = toHashCor(xmlCor)
            corConfig.config(background=COR_SELETA)
            bmCorConfig.config(background=COR_SELETA)
         except:
            print("Retangulo: Cor nao encontrada")
         try:
            xmlEspessura = int(geo.getElementsByTagName('Espessura')[0].childNodes[0].data)
            #print(f'Reta: Espessura é: {xmlEspessura}')
            ESPESSURA_SELETA = xmlEspessura
         except:
            pass
            #print("Retangulo: Espessura nao encontrada")
         fazRetangulo(xmlPA[0], xmlPA[1], xmlPB[0], xmlPB[1], COR_SELETA, ESPESSURA_SELETA)

      elif(geo.nodeName == 'Poligono'):
         #print(f'Tem um poligono')
         poligono = []
         try:
            for ponto in geo.getElementsByTagName('Ponto'):
               xmlX = int(float(ponto.getElementsByTagName('x')[0].childNodes[0].data)*desenhoQuadro.winfo_width())
               xmlY = int(float(ponto.getElementsByTagName('y')[0].childNodes[0].data)*desenhoQuadro.winfo_width())
               ponto = [xmlX, xmlY]
               del xmlX
               del xmlY
               poligono.append(ponto)
               #print(f'Poligono: Ponto é: {ponto[0]},{ponto[1]}')
         except:
            print("Poligono: Ponto nao encontrado")
         try:
            xmlCor = geo.getElementsByTagName('Cor')[0]
            xmlCor = (int(xmlCor.getElementsByTagName('R')[0].childNodes[0].data),
                      int(xmlCor.getElementsByTagName('G')[0].childNodes[0].data),
                      int(xmlCor.getElementsByTagName('B')[0].childNodes[0].data))
            COR_SELETA = toHashCor(xmlCor)
            corConfig.config(background=COR_SELETA)
            bmCorConfig.config(background=COR_SELETA)
         except:
            print("Poligono: Cor nao encontrada")
         try:
            xmlEspessura = int(geo.getElementsByTagName('Espessura')[0].childNodes[0].data)
            #print(f'Reta: Espessura é: {xmlEspessura}')
            ESPESSURA_SELETA = xmlEspessura
         except:
            #print("Poligono: Espessura nao encontrada")
            pass
         #print(poligono)
         fazPoligono(poligono, COR_SELETA, ESPESSURA_SELETA)
   print(f'Historico com {len(historico)} formas')

def desenhaHistorico(seQuadro=True, seMapa=True):
   global historico
   if(seQuadro is True):desenhoQuadro.delete("all")
   if(seMapa is True):desenhoMapa.delete("all")
   for forma in historico:
      #print(forma)
      if(forma[0] is 'ponto'):
         #['ponto', '#ff0000', 2, 178, 259]
         #fazPonto(x, y, cor=COR_SELETA, esp=ESPESSURA_SELETA, seQuadro=True, seMapa=True, seHist=True)
         fazPonto(forma[3], forma[4], forma[1], forma[2], seQuadro, seMapa, False)
      elif(forma[0] is 'reta'):
         #['reta', '#ff0000', 2, 212, 240, 376, 403]
         #fazReta(ax, ay, bx, by, cor=COR_SELETA, esp=ESPESSURA_SELETA, seQuadro=True, seMapa=True, seHist=True)
         fazReta(forma[3], forma[4], forma[5], forma[6], forma[1], forma[2], seQuadro, seMapa, False)
      elif(forma[0] is 'circulo'):
         #['circulo', '#ff0000', 2, 141, 173, 223.27113561766106]
         #fazCirculo(cx, cy, r, cor=COR_SELETA, esp=ESPESSURA_SELETA, seQuadro=True, seMapa=True, seHist=True)
         fazCirculo(forma[3], forma[4], forma[5], forma[1], forma[2], seQuadro, seMapa, False)
      elif(forma[0] is 'retangulo'):
         #['retangulo', '#ff0000', 2, 506, 431, 735, 554]
         #fazRetangulo(ax, ay, bx, by, cor=COR_SELETA, esp=ESPESSURA_SELETA, seQuadro=True, seMapa=True, seHist=True)
         fazRetangulo(forma[3], forma[4], forma[5], forma[6], forma[1], forma[2], seQuadro, seMapa, False)
      elif(forma[0] is 'poligono'):
         #['poligono', '#ff0000', 2, ps]
         #fazPoligono(ps, cor=COR_SELETA, esp=ESPESSURA_SELETA, seQuadro=True, seMapa=True, seHist=True)
         fazPoligono(forma[3],forma[1],forma[2], seQuadro, seMapa, False)

def ctrlZ(event=None):
   global historico
   global desenhoQuadro
   global desenhoMapa
   if(historico is not None):
      try:
         del historico[-1]
      except:
         print('ctrlZ falhou')
   desenhoQuadro.delete("all")
   desenhoMapa.delete("all")
   desenhaHistorico()

#bogosity
#X_cursor

def sobre():
   sobre = Toplevel(root, bg='black')
   #toplevel eh uma janela que abre inrriba da outra, puxa o foco
   junto = Frame(sobre, bg=sobre['bg'], height=500, width=450)
   junto.pack(expand=True, fill=BOTH, side=TOP)
   sImg = PhotoImage(file='icons/Pepeg.gif')
   pepeg = Label(junto, image=sImg, bg=sobre['bg'])
   pepeg.grid(row=0, column=0)
   sobreTexto = f'Feito por:\nEmerson B Grisi\nCarlos Eduardo Freitas\nCaio Furtado\nGabriel França\n'
   anuncio = Label(junto, text=sobreTexto, bg=sobre['bg'], fg='#ff0000')
   anuncio.grid(row=1, column=0)
   sobre.geometry('140x200+500+500')
 
#ORGANIZACOES DE MENU
#menu arquivo
menuBarra = Menu(root)
menuArquivo = Menu(menuBarra, tearoff=0)
menuArquivo.add_command(label="Novo", command=novoQuadro)
menuArquivo.add_command(label="Abrir", command=inputArquivo)
menuArquivo.add_command(label="Salvar", command=salvarHistoricoXML)
menuArquivo.add_command(label="Salvar como...", command=donothing)
menuArquivo.add_command(label="Fechar", command=donothing)
menuArquivo.add_separator()
menuArquivo.add_command(label="Sair", command=root.quit)
menuBarra.add_cascade(label="Arquivo", menu=menuArquivo)

#menu editar
menuEditar = Menu(menuBarra, tearoff=0)
menuEditar.add_command(label="Desfazer", command=ctrlZ)
menuEditar.add_separator()
menuEditar.add_command(label="Recortar", command=donothing)
menuEditar.add_command(label="Copiar", command=donothing)
menuEditar.add_command(label="Colar", command=donothing)
menuEditar.add_command(label="Apagar", command=donothing)
menuBarra.add_cascade(label="Editar", menu=menuEditar)

#menu ajuda
menuAjuda = Menu(menuBarra, tearoff=0)
menuAjuda.add_command(label="Sobre...", command=sobre)
menuBarra.add_cascade(label="Ajuda", menu=menuAjuda)

#aplica o menu
root.config(menu=menuBarra)
root.bind("<Control-z>",ctrlZ)

janela.mainloop()
