o=float(input()) #nota de corte ouro
p=float(input()) #nota de corte prata
b=float(input()) #nota de corte bronze
n=[float(input())] #nota dos alunos
l=[]
while n[0]!=-1:
  l=l+n
  n=[float(input())]
num=len(l) # conta quantas listas tem 
def conta_ouro(num,o): #conta num de ouro
  ouro=0
  for k in range(num):
    if l[k]<=10 and l[k]>=o:
      ouro=ouro+1
  if ouro==0:
    print("Nenhum participante recebeu medalha de ouro!")
  else:
    print("Medalha(s) de ouro:", ouro)
conta_ouro(num,o)
def conta_prata(num,p,o): #conta num de prata
  prata=0
  for k in range(num):
    if l[k]<o and l[k]>=p:
      prata=prata+1
  if prata==0:
    print("Nenhum participante recebeu medalha de prata!")
  else:
    print("Medalha(s) de prata:", prata)
conta_prata(num,p,o)
def conta_bronze(num,b,p): #conta num de bronze
  bronze=0
  for k in range(num):
    if l[k]<p and l[k]>=b:
      bronze=bronze+1
  if bronze==0:
    print("Nenhum participante recebeu medalha de bronze!")
  else:
    print("Medalha(s) de bronze:", bronze)
conta_bronze(num,b,p)
def maior_nota(num):
  win=l[0]
  for k in range(num):
    if l[k]>=win:
      win=l[k]
  print("Maior nota:",win)
maior_nota(num)