from machine import Pin, ADC, I2C
from ssd1306 import SSD1306_I2C
from utime import sleep_ms,sleep
import random

contx=0
conty=0

casillas=0
click=0
posO=[1,2,3,4,5,6,7,8,9]

ancho=128
alto=64
ejex= ADC(Pin(13))
ejex.atten(ADC.ATTN_11DB)
ejex.width(ADC.WIDTH_12BIT)

boton1=Pin(26,Pin.IN,Pin.PULL_UP)

ejey= ADC(Pin(12))
ejey.atten(ADC.ATTN_11DB)
ejey.width(ADC.WIDTH_12BIT)

i2c = I2C(0, scl=Pin(22), sda=Pin(23)) 
oled = SSD1306_I2C(ancho, alto, i2c)

def seleccionar(contx, conty, casillas): #ACA SE MUEVE EL [] PARA SELECCIONAR CASILLAS
    if(contx==0 and conty==0):
        oled.text("[  ]", 5, 5, 10)
        casillas=1
    else:
        oled.text(" ", 5, 5, 10)
    
    if(contx==1 and conty==0):
        oled.text("[  ] ", 48, 5, 10)
        casillas=2
    else:
        oled.text(" ", 48, 5, 10)
        
    if(contx==2 and conty==0):
        oled.text("[  ] ", 93, 5, 10)
        casillas=3
    else:
        oled.text(" ", 93, 5, 10)
    
    if(contx==0 and conty==1):
        oled.text("[  ] ", 5, 27, 10)
        casillas=4
    else:
        oled.text(" ", 5, 27, 10)

    if(contx==1 and conty==1):
        oled.text("[  ] ", 48, 27, 10)
        casillas=5
    else:
        oled.text(" ", 48, 27, 10)
    
    if(contx==2 and conty==1):
        oled.text("[  ] ", 93, 27, 10)
        casillas=6
    else:
        oled.text(" ", 93, 27, 10)
    
    if(contx==0 and conty==2):
        oled.text("[  ] ", 5, 51, 10)
        casillas=7
    else:
        oled.text(" ", 5, 51, 10)
    
    if(contx==1 and conty==2):
        oled.text("[  ] ", 48, 51, 10)
        casillas=8
    else:
        oled.text(" ", 48, 51, 10)
        
    if(contx==2 and conty==2):
        oled.text("[  ] ", 93, 51, 10)
        casillas=9
    else:
        oled.text(" ", 93, 51, 10)

matriz=[[2,2,2],
        [2,2,2],
        [2,2,2],
        ]
matriztxt=[["","",""],
           ["","",""],
           ["","",""]]

def ponerXyO(casillas, click,turno):#PONER LAS Xs Y LAS Os EN LAS CASILLAS
  
  contador= turno

  if(turno==0):
    #UN MONTON DE VARIABLES PORQ NO SUPE HACERLO MAS EFICIENTE A

    #ACA SE PONEN LOS NUMEROS Q CORRESPONDEN A X EN LA MATRIZ
    if(click==1 and matriz[0][0]==2):
        matriz[0][0]=1
        matriztxt[0][0]="x"
        contador=not contador
    if(click==2 and matriz[0][1]==2):
        matriz[0][1]=1
        matriztxt[0][1]="x"
        contador=not contador
    if(click==3 and matriz[0][2]==2):
        matriz[0][2]=1
        matriztxt[0][2]="x"
        contador=not contador
    if(click==4 and matriz[1][0]==2):
        matriz[1][0]=1
        matriztxt[1][0]="x"
        contador=not contador
    if(click==5 and matriz[1][1]==2):
        matriz[1][1]=1
        matriztxt[1][1]="x"
        contador=not contador
    if(click==6 and matriz[1][2]==2):
        matriz[1][2]=1
        matriztxt[1][2]="x"
        contador=not contador
    if(click==7 and matriz[2][0]==2):
        matriz[2][0]=1
        matriztxt[2][0]="x"
        contador=not contador
    if(click==8 and matriz[2][1]==2):
        matriz[2][1]=1
        matriztxt[2][1]="x"
        contador=not contador
    if(click==9 and matriz[2][2]==2):
        matriz[2][2]=1
        matriztxt[2][2]="x"
        contador=not contador
            
                    

  else:
    #ACA SE PONEN LOS NUMEROS Q CORRESPONDEN A LAS Os
    if(click==1 and matriz[0][0]==2):
      matriz[0][0]=0
      matriztxt[0][0]="o"
      contador=not contador
    if(click==2 and matriz[0][1]==2):
      matriz[0][1]=0
      matriztxt[0][1]="o"
      contador=not contador
    if(click==3 and matriz[0][2]==2):
      matriz[0][2]=0
      matriztxt[0][2]="o"
      contador=not contador
    if(click==4 and matriz[1][0]==2):
      matriz[1][0]=0
      matriztxt[1][0]="o"
      contador=not contador
    if(click==5 and matriz[1][1]==2):
      matriz[1][1]=0
      matriztxt[1][1]="o"
      contador=not contador
    if(click==6 and matriz[1][2]==2):
      matriz[1][2]=0
      matriztxt[1][2]="o"
      contador=not contador
    if(click==7 and matriz[2][0]==2):
      matriz[2][0]=0
      matriztxt[2][0]="o"
      contador=not contador
    if(click==8 and matriz[2][1]==2):
      matriz[2][1]=0
      matriztxt[2][1]="o"
      contador=not contador
    if(click==9 and matriz[2][2]==2):
      matriz[2][2]=0
      matriztxt[2][2]="o"
      contador=not contador
            
  #ACA SE IMPRIMEN LOS VALORES 
   
  oled.text(matriztxt[0][0], 15, 5, 1)
  oled.text(matriztxt[0][1], 60, 5, 1)
  oled.text(matriztxt[0][2], 103, 5, 1) 

  oled.text(matriztxt[1][0], 15, 27, 1)
  oled.text(matriztxt[1][1], 60, 27, 1)
  oled.text(matriztxt[1][2], 103, 27, 1)   

  oled.text(matriztxt[2][0], 15, 51, 10)
  oled.text(matriztxt[2][1], 60, 51, 10)
  oled.text(matriztxt[2][2], 103, 51, 10)

  return contador
def refrescar (oled):
   
    seleccionar(contx, conty, casillas)


    oled.show()

def Comprobar_partida():

  victoria=False

  for i in range(len(matriz)):
    if matriz[i][0]!=2 and matriz[i][1]!=2 and matriz[i][2]!=2 and (matriz[i][0]==matriz[i][1] and matriz[i][1]==matriz[i][2]):
      if matriz[i][0]==0:
        return 0
      else:
        return 1
        victoria=True
  for i in range(len(matriz[0])):
    if matriz[0][i]!=2 and matriz[1][i]!=2 and matriz[2][i]!=2 and (matriz[0][i]==matriz[1][i] and matriz[1][i]==matriz[2][i]):
      if matriz[0][i]==0:
        return 0
        victoria=True
      else:
        return 1
        victoria=True
  if matriz[1][1]!=2 and ((matriz[0][0]==matriz[1][1] and matriz[1][1]==matriz[2][2]) or (matriz[0][2]==matriz[1][1] and matriz[1][1]==matriz[2][0])):
    if matriz[1][1]==0:
      return 0
      victoria=True
    else:
      return 1
      victoria=True

  empate=True
  
  for i in range(len(matriz)):
    for j in range(len(matriz[0])):
      if matriz[i][j]==2:
        empate=False
  
  if empate==True and victoria==False:
    return 2

  return 3
def vaciar_matrices():
  for i in range(len(matriz)):
    for j in range(len(matriz[i])):
      matriz[i][j]=2
      matriztxt[i][j]=""

contador=0
end=False

while True:

  estado=Comprobar_partida()

  if estado==0:
    click=0
    oled.fill(0)
    vaciar_matrices()
    oled.text("Gana O", 37, 27, 1)
    oled.show()
    sleep(3)
  if estado==1:
    click=0
    oled.fill(0)
    vaciar_matrices()
    oled.text("Gana X", 37, 27, 1)
    oled.show()
    sleep(3)
  if estado==2:
    click=0
    oled.fill(0)
    vaciar_matrices()
    oled.text("Empate!", 37, 27, 1)
    oled.show()
    sleep(3)
  
  oled.line(42,0,42,64,1)
  oled.line(84,0,84,64,1)
  oled.line(128,20,0,20,1)
  oled.line(128,43,0,43,1)
  
  tempx=ejex.read()
  tempy=ejey.read()
  
  if(tempx==4095 and contx!=2):
      contx=contx+1
      sleep_ms(200)
  if(tempx==0 and contx!=0):
      contx=contx-1
      sleep_ms(200)
  if(tempy==4095 and conty!=2):
      conty=conty+1
      sleep_ms(200)
  if(tempy==0 and conty!=0):
      conty=conty-1
      sleep_ms(200)

  if(contx==0 and conty==0):
      casillas=1
  if(contx==1 and conty==0):
      casillas=2
  if(contx==2 and conty==0):
      casillas=3
  if(contx==0 and conty==1):
      casillas=4
  if(contx==1 and conty==1):
      casillas=5
  if(contx==2 and conty==1):
      casillas=6
  if(contx==0 and conty==2):
      casillas=7
  if(contx==1 and conty==2):
      casillas=8
  if(contx==2 and conty==2):
      casillas=9
  
  if(not boton1.value()):
      click=casillas
      sleep_ms(200)

  contador=ponerXyO(casillas, click, contador)
  refrescar(oled)

  oled.show()
  oled.fill(0)
