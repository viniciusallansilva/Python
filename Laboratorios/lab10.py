# -*- encoding: utf-8 -*-
#JOGO BINGO2 2018 LAB10 MC102
#BY: Vinicius Allan da Silva
#faça o bagui direito vinicius até 01/12/18

def printatabela(L,n): #PRINTA A TABELA ORGANIZADA
  for z0 in range(n):
    if z0!=(n-1):
      print("+----------------+ ",end="")
    else:
      print("+----------------+")
  for z1 in range(n):
    if z1!=(n-1):  
      print("| B  I  N  G  O  | ",end="")
    else:
      print("| B  I  N  G  O  |")
  for z2 in range(n):
    if z2!=(n-1):
      print("+================+ ",end="")
    else:
      print("+================+")
  for z in range(n):
    if z!=(n-1): 
      print("|",L[z][0][0],L[z][0][1],L[z][0][2],L[z][0][3],L[z][0][4],"| ",end="")
    else:
      print("|",L[z][0][0],L[z][0][1],L[z][0][2],L[z][0][3],L[z][0][4],"|")
  for y in range(n):  
    if y!=(n-1):
      print("|",L[y][1][0],L[y][1][1],L[y][1][2],L[y][1][3],L[y][1][4],"| ",end="")
    else:
      print("|",L[y][1][0],L[y][1][1],L[y][1][2],L[y][1][3],L[y][1][4],"|")
  for x in range(n):
    if x!=(n-1):
      print("|",L[x][2][0],L[x][2][1],L[x][2][2],L[x][2][3],L[x][2][4],"| ",end="")
    else:
      print("|",L[x][2][0],L[x][2][1],L[x][2][2],L[x][2][3],L[x][2][4],"|")
  for u in range(n): 
    if u!=(n-1):
      print("|",L[u][3][0],L[u][3][1],L[u][3][2],L[u][3][3],L[u][3][4],"| ",end="")
    else:
      print("|",L[u][3][0],L[u][3][1],L[u][3][2],L[u][3][3],L[u][3][4],"|")
  for v in range(n):
    if v!=(n-1):
      print("|",L[v][4][0],L[v][4][1],L[v][4][2],L[v][4][3],L[v][4][4],"| ",end="")
    else:
      print("|",L[v][4][0],L[v][4][1],L[v][4][2],L[v][4][3],L[v][4][4],"|")
  for z3 in range(n):
    if z3!=(n-1):  
      print("+----------------+ ",end="")
    else:
      print("+----------------+")

def addletra(L,sorteado,n): #ADICIONA XX NA TABELA
  for a in range(n):
    for b in range(5):
      for c in range(5):
        if sorteado in L[a][b][c]:
          L[a][b][c]="XX"

def bingo(L,n):
  X=0
  for a in range(n): #ANALISA LINHA
    for b in range(5):
      if L[a][b][0]=="XX" and L[a][b][1]=="XX" and L[a][b][2]=="XX" and L[a][b][3]=="XX" and L[a][b][4]=="XX":
        return X
  for c in range(n): #ANALISA COLUNA
    for d in range(n):
      if L[c][0][d]=="XX" and L[c][1][d]=="XX" and L[c][2][d]=="XX" and L[c][3][d]=="XX" and L[c][4][d]=="XX":
        return X
  for e in range(n): #ANALISA DIAGONAL 1
    if L[e][0][0]=="XX" and L[e][1][1]=="XX" and L[e][2][2]=="XX" and L[e][3][3]=="XX" and L[e][4][4]=="XX":
      return X
  for f in range(n): #ANALISA DIAGONAL 2
    if L[f][4][0]=="XX" and L[f][3][1]=="XX" and L[f][2][2]=="XX" and L[f][1][3]=="XX" and L[f][0][4]=="XX":
      return X

n=int(input()) #NUMERO DE CARTELAS NO JOGO

L=[]
for z in range(n):
  l=[]
  l0=(input()).split() #ENTRADA LINHA 1
  l1=(input()).split() #ENTRADA LINHA 2
  l2=(input()).split() #ENTRADA LINHA 3
  l3=(input()).split() #ENTRADA LINHA 4
  l4=(input()).split() #ENTRADA LINHA 5
  l=[l0,l1,l2,l3,l4]
  L=L+[l]

printatabela(L,n)

numero=int(input())
for i in range(numero): #LAÇO DE REPETIÇÕES DA TABELA
  letra=input()
  print(letra)
  letra=letra.split()
  sorteado=letra[0][2:4] #NUMERO A SER PROCURADO
  o=0
  for g in range(n):
    for h in range(5):
      for j in range(5):
        if sorteado in L[g][h][j]:
          o+=1
  if o!=0:
    addletra(L,sorteado,n)
    printatabela(L,n)
  if bingo(L,n)==0:
    print("BINGO!")
    break