# -*- encoding: utf-8 -*-
#LAB011-BUSCA BINÁARIA -ATÉ DIA 01/12 OPCIONAL
#BY: Vinicius Allan da Silva

def main(): # FUNÇÃO DE COMANDOS INICIAIS
  n=int(input()) 
  v=(input()).split()
  print("Elemento procurado:",str(n).zfill(3))
  num=len(v)
  for a in range(num):
    b=str(v[a]).zfill(3)
    v[a]=b
  roda=0
  l="e"
  espaco=0
  centro=0
  molduralista(num,v)
  if ordenado2(v,num)==False:  #SE FOR FALSE, PARA PROCESSO
    print("Vetor nao estah ordenado")
  else:
    while roda==0:
      centro=num//2
      if num%2!=0:
        centro=centro+1
      indice=centro
      indice+=espaco
      #print("indice",indice,"num",num,"espaço",espaco,"centro",centro)
      moldura(indice,num,v,l,espaco,centro)
      if int(v[indice-1])==n: #CENTRO SOBRE INDICE
        print("O elemento estah na posicao {}".format(indice-1))
        roda=1
      elif int(v[indice-1])<n: #NUMERO ESTÁ A DIREITA DO CENTRO
        l="d"
        num=(num-centro)
        if num==0:
          print("O elemento nao foi encontrado")
          break
        espaco+=centro
        roda=0
      elif int(v[indice-1])>n: # NUMERO ESTA A ESQUERDA DO CENTRO
        l="e"
        if num%2!=0: #ÍMPAR
          num=(num//2)
        else:        #PAR
          num=(num//2)-1
        if num<=0:
          print("O elemento nao foi encontrado")
          break
        roda=0

def moldura(indice,num,v,l,espaco,centro):
  if l=="e":
    if espaco==0:
      if num%2!=0:
        j=(num//2)+1 
        print("+-----"*(j-1),end="")
      else:
        j=num//2
        print("+-----"*(j-1),end="")
    else:
      print("      "*espaco,end="")
      if num%2!=0:
        j=(num//2)+1 
        print("+-----"*(j-1),end="")
      else:
        j=num//2
        print("+-----"*(j-1),end="")
    print("+=====",end="")
    print("+-----"*(num-j),end="")
    print("+")

    if espaco==0:
      for a in range(num):
        if a!=(indice-1) and a!=(num-1):
          print("|",v[a+espaco],"",end="")
        elif a==(indice-1) and a!=(num-1):
          print("||",end="")
          print(v[a+espaco],end="")
          print("|",end="")
        elif a!=(indice-1) and a==(num-1):
          print("|",v[a+espaco],"|")
        elif a==(indice-1) and a==(num-1) and not num==1:
          print("|",v[a+espaco],"|")
        elif num==1:
          print("||",end="")
          print(v[a+espaco],end="")
          print("||")
    else:
      print("      "*espaco,end="")
      for b in range(num):  
        if b!=(centro-1) and b!=(num-1):
          print("|",v[b+espaco],"",end="")
        elif b==(centro-1) and b!=(num-1):
          print("||",end="")
          print(v[b+espaco],end="")
          print("|",end="")
        elif b!=(centro-1) and b==(num-1) and not num==1:
          print("|",v[b+espaco],"|")
        elif b==(centro-1) and b==(num-1) and not num==1:
          print("|",v[b+espaco],"|")
        elif num==1:
          print("||",end="")
          print(v[b+espaco],end="")
          print("||")
  
    if espaco==0:
      if num%2!=0:
        j=(num//2)+1 
        print("+-----"*(j-1),end="")
      else:
        j=num//2
        print("+-----"*(j-1),end="")
    else:
      print("      "*espaco,end="")
      if num%2!=0:
        j=(num//2)+1 
        print("+-----"*(j-1),end="")
      else:
        j=num//2
        print("+-----"*(j-1),end="")
    print("+=====",end="")
    print("+-----"*(num-j),end="")
    print("+")
  
  elif l=="d":
    print("      "*espaco,end="")
    if num%2!=0:
      j=(num//2)+1 
      print("+-----"*(j-1),end="")
    else:
      j=num//2
      print("+-----"*(j-1),end="")
    print("+=====",end="")
    print("+-----"*(num-j),end="")
    print("+")

    print("      "*espaco,end="")
    for a in range(num):   
      if a!=(j-1) and a!=(num-1):
        print("|",v[a+espaco],"",end="")
      elif a==(j-1) and a!=(num-1):
        print("||",end="")
        print(v[a+espaco],end="")
        print("|",end="")
      elif a!=(j-1) and a==(num-1):
        print("|",v[a+espaco],"|")
      elif a==(j-1) and a==(num-1) and not num==1:
        print("|",v[a+espaco],"|")
      elif num==1:
          print("||",end="")
          print(v[a+espaco],end="")
          print("||")
    
    print("      "*espaco,end="")
    if num%2!=0:
      j=(num//2)+1 
      print("+-----"*(j-1),end="")
    else:
      j=num//2
      print("+-----"*(j-1),end="")
    print("+=====",end="")
    print("+-----"*(num-j),end="")
    print("+")

    

def ordenado2(v,num): # se o vetor estiver desordenado, encerra processo
  for a in range(num):
    if a<(num-1):
      if not v[a]<v[a+1]:
        return False

def molduralista(num,v):
  l=["+-----","+=====","+","|","||"]
  print(l[0]*num,sep="",end="")
  print(l[2])
  for b in range(num):
    if b==(num-1):
      print(l[3],v[b],"|")
    else:
      print(l[3],v[b],"",end="")
  print(l[0]*num,sep="",end="")
  print(l[2])
     
main()