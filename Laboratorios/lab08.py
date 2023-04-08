# -*- encoding: utf-8 -*-
#Criador: Vinicius Allan da Silva
#UNICAMP-ENGENHARIA DE CONTROLE E AUTOMAÇÃO
lista=["perfeitamente", "liberdade", "enfermidade","significado", "outono", "chuva", "ilha","infinito", "solidariedade", "ameixa","felicidade", "arte", "paternidade","criatividade", "virtude", "guerra","democracia", "teatro", "saudade", "adeus","paz", "honestidade", "horizonte", "sabedoria","sossego", "maternidade", "esperteza","primavera", "coragem", "igualdade","navio", "montanha", "queijo","gentileza", "tempestade", "joalheria","paralelogramo", "melancolia", "trem","inverno", "amizade", "atriz","computador", "borboleta", "aeroporto","nascimento", "uva", "oceano", "orquestra","melancia"]

cenas_forca = [
"""\n+++++
|   |
|
|
|
+_______""",

"""\n+++++
|   |
|   O
|
|
+_______""",

"""\n+++++
|   |
|   O
|   |
|
+_______""",
"""\n+++++
|   |
|   O
|  /|
|
+_______""",

"""\n+++++
|   |
|   O
|  /|\\
|
+_______""",

"""\n+++++
|   |
|   O
|  /|\\
|  /
+_______""",

"""\n+++++
|   |
|   O
|  /|\\
|  / \\
+_______"""

]

def addletra3(listapalavra,b,palavra,n):
  dici={}
  for s in range(len(palavra)):
    if b==palavra[s]:
      dici[s]=b
      listapalavra[s]=b
  print("Palavra: ",end="")
  for x in range(n):
    if x!=(n-1):
      print(listapalavra[x]," ",end="")
    elif x==(n-1):
      print(listapalavra[x])
  
listapalavra=[]
n=int(input("Escolha um numero entre 0 e 49: "))

if n<0 or n>49:
  print("Numero invalido.")
else:
  palavra=lista[n]
  print(cenas_forca[0])  
  n=len(palavra)
  listapalavra=["_" for s in range(n)]
  print("Palavra: ",end="")
  for x in range(n):
    if x!=(n-1):
      print(listapalavra[x]," ",end="")
    elif x==(n-1):
      print(listapalavra[x])
  
  ln=[]  
  for s in palavra:
    if s not in ln: 
      ln+=s
  nu=len(ln)
  
  z=0
  soma=0
  soma2=0
  lc=[]
  li=[]
  lin=""
  j=0
  while z==0:
    correta=0
    incorreta=0   
    print("Proxima letra: ",end="")
    b=input()
    #b=input("Proxima letra:") 
    for c in palavra:
      if c==b:
        correta+=1
    if correta==0: # nenhuma palavra
      if not b in lc:
        soma+=1
        j=0
      else:
        print("Voce jah escolheu esta letra.")
        print(cenas_forca[soma])
        addletra3(listapalavra,b,palavra,n)
        if lin!="":  
          print("Tentativa(s) incorreta(s):{}".format(lin))
        j=1
    elif correta!=0:# pelo menos 1
      if not b in lc:
        soma2+=1
        j=0
      else:
        print("Voce jah escolheu esta letra.")
        print(cenas_forca[soma])
        addletra3(listapalavra,b,palavra,n)
        if lin!="":  
          print("Tentativa(s) incorreta(s):{}".format(lin))
        j=1
    lc+=[b]
    if correta==0 and j!=1: #condicional p incorreta
      if soma<6:
        li+=[b]
        print(cenas_forca[soma])
        addletra3(listapalavra,b,palavra,n)
        lin+=" "+b
        print("Tentativa(s) incorreta(s):{}".format(lin))
        z=0
      else:
        li+=[b]
        print(cenas_forca[soma])
        addletra3(listapalavra,b,palavra,n)
        lin+=" "+b
        print("Tentativa(s) incorreta(s):{}".format(lin))
        print("Palavra oculta: {}".format(palavra))
        z=1
    elif correta!=0 and j!=1: #condicional p correta
      if soma2<(nu): 
        print(cenas_forca[soma])
        addletra3(listapalavra,b,palavra,n)
        if soma>0:
          print("Tentativa(s) incorreta(s):{}".format(lin))
        z=0
      elif soma2>=(nu): 
        z=1
        print(cenas_forca[soma])
        addletra3(listapalavra,b,palavra,n)
        if soma>0:
          print("Tentativa(s) incorreta(s):{}".format(lin))
        print("Palavra encontrada!")