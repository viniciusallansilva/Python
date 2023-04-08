#JOGO BINGO 2018 LAB09 MC102
#BY: Vinicius Allan da Silva

l1=input() #ENTRADA LINHA 1
L1=l1.split()
l2=input() #ENTRADA LINHA2
L2=l2.split()
l3=input() #ENTRADA LINHA 3
L3=l3.split()
l4=input() #ENTRADA LINHA 4
L4=l4.split()
l5=input() #ENTRADA LINHA 5
L5=l5.split()

n=int(input()) #NUMERO DE NUMEROS SORTEADOS
B=[L1[0],L2[0],L3[0],L4[0],L5[0]]
I=[L1[1],L2[1],L3[1],L4[1],L5[1]]
N=[L1[2],L2[2],L2[2],L4[2],L5[2]]
G=[L1[3],L2[3],L3[3],L4[3],L5[3]]
O=[L1[4],L2[4],L3[4],L4[4],L5[4]]
tabela={"B":B,"I":I,"N":N,"G":G,"O":O} #TABELA COM AS COLUNA

def tabela(B,I,N,G,O): # PRINTA A TABELA ARRUMADA
  print("+----------------+")
  print("| B  I  N  G  O  |")
  print("+================+")
  print("|",B[0],I[0],N[0],G[0],O[0],"|")
  print("|",B[1],I[1],N[1],G[1],O[1],"|")
  print("|",B[2],I[2],"XX",G[2],O[2],"|")
  print("|",B[3],I[3],N[3],G[3],O[3],"|")
  print("|",B[4],I[4],N[4],G[4],O[4],"|")
  print("+----------------+") 
tabela(B,I,N,G,O)

def bingo(B,I,N,G,O): #FUNAÇÃO ANALISA PRA VER SE É BINGO
  #ANALISA COLUNA
  if B[0]=="XX" and B[1]=="XX" and B[2]=="XX" and B[3]=="XX" and B[4]=="XX":
    return 1
  if I[0]=="XX" and I[1]=="XX" and I[2]=="XX" and I[3]=="XX" and I[4]=="XX":
    return 1
  if N[0]=="XX" and N[1]=="XX" and N[3]=="XX" and N[4]=="XX":
    return 1
  if G[0]=="XX" and G[1]=="XX" and G[2]=="XX" and G[3]=="XX" and G[4]=="XX":
    return 1
  if O[0]=="XX" and O[1]=="XX" and O[2]=="XX" and O[3]=="XX" and O[4]=="XX":
    return 1
  #ANALISA LINHA
  if B[0]=="XX" and I[0]=="XX" and N[0]=="XX" and G[0]=="XX" and O[0]=="XX":
    return 1
  if B[1]=="XX" and I[1]=="XX" and N[1]=="XX" and G[1]=="XX" and O[1]=="XX":
    return 1
  if B[2]=="XX" and I[2]=="XX" and G[2]=="XX" and O[2]=="XX":
    return 1
  if B[3]=="XX" and I[3]=="XX" and N[3]=="XX" and G[3]=="XX" and O[3]=="XX":
    return 1
  if B[4]=="XX" and I[4]=="XX" and N[4]=="XX" and G[4]=="XX" and O[4]=="XX":
    return 1
  #ANALISA DIAGONAL
  if B[0]=="XX" and I[1]=="XX" and G[3]=="XX" and O[4]=="XX":
    return 1
  if B[4]=="XX" and I[3]=="XX" and G[1]=="XX" and O[0]=="XX":
    return 1
    print("q lixo")

for z in range(n):
  b=0
  i=0
  n=0
  g=0
  o=0
  s=input() #NUMERO SORTEADO DO MOMENTO
  coluna=s[0]
  numero=s[2:4]
  print(s)
  for x in range(len(B)):
    if B[x]==numero:
      B[x]="XX"
      b=1
  for x in range(len(I)):
    if I[x]==numero:
      I[x]="XX"
      i=1
  for x in range(len(N)):
    if N[x]==numero:
      N[x]="XX"
      n=1
  for x in range(len(G)):
    if G[x]==numero:
      G[x]="XX"
      g=1
  for x in range(len(O)):
    if O[x]==numero:
      O[x]="XX"
      o=1
  if b==1 or i==1 or n==1 or g==1 or o==1:
    tabela(B,I,N,G,O)
  if bingo(B,I,N,G,O)==1:
    print("BINGO!")
    break