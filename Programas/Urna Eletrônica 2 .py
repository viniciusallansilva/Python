print("URNA ELETR�NICA NO BRASIL, ELEI��ES 2018")
print("CANDIDATO/PARTIDO/NUMERO") 
print("Ciro Gomes (PDT): 12") #0
print("Fernando Haddad (PT): 13") #1
print("Jair Bolsonaro (PSL): 17") #2
print("Jo�o Amo�do (Novo): 30")   #3
print("Marina Silva (Rede): 18")  #4
print("DIGITE O N�MERO DE SEU CANDIDATO E CONFIRME") 
print("Para finalizar a vota��o, digite 0:")
l=[[],[],[],[],[]]
a=[int(input("O n�mero de seu candidato �:"))]
b=[]
if a[0]==12:
  c=input("Seu candidato � Ciro Gomes?SIM OU NAO?:")
  if c=="SIM":
    l[0].append(1)
    print("Voc� votou no Ciro Gomes")
elif a[0]==13:
  c=input("Seu candidato � Fernando Haddad?SIM OU NAO?:")
  if c=="SIM":
    l[1].append(1)
    print("Voc� votou no Fernando Haddad")
elif a[0]==17:
  c=input("Seu candidato � Jair Bolsonaro?SIM OU NAO?:")
  if c=="SIM":
    l[2].append(1)
    print("Voc� votou no Jair Bolsonaro")
elif a[0]==30:
  c=input("Seu candidato � Jo�o Amo�do?SIM OU NAO?:")
  if c=="SIM":
    l[3].append(1)
    print("Voc� votou no Jo�o Amo�do")
elif a[0]==18:
  c=input("Seu candidato � Marina Silva?SIM OU NAO?:")
  if c=="SIM":
    l[4].append(1)
    print("Voc� votou no Marina Silva")
while a[0]!=0: 
  b=b+a
  a=[int(input("O n�mero de seu candidato �:"))]
  if a[0]==12:
    c=input("Seu candidato � Ciro Gomes?SIM OU NAO?:")
    if c=="SIM":
      l[0].append(1)
      print("Voc� votou no Ciro Gomes")
  elif a[0]==13:
    c=input("Seu candidato � Fernando Haddad?SIM OU NAO?:")
    if c=="SIM":
      l[1].append(1)
      print("Voc� votou no Fernando Haddad")
  elif a[0]==17:
    c=input("Seu candidato � Jair Bolsonaro?SIM OU NAO?:")
    if c=="SIM":
      l[2].append(1)
      print("Voc� votou no Jair Bolsonaro")
  elif a[0]==30:
    c=input("Seu candidato � Jo�o Amo�do?SIM OU NAO?:")
    if c=="SIM":
      l[3].append(1)
      print("Voc� votou no Jo�o Amo�do")
  elif a[0]==18:
    c=input("Seu candidato � Marina Silva?SIM OU NAO?:")
    if c=="SIM":
      l[4].append(1)
      print("Voc� votou no Marina Silva")
n=len(b)
print("Foram um total de {} votos realizados nessa elei��o!".format(n))
if n==0:
  print("Ningu�m ganhou, pois n�o houve voto, logo, LULA vai implantar o comunismo no bagulho")

def quantidadevotos(l):
  if len(l[0])!=0:
    print("Candidato Ciro Gomes tem {} votos.".format(len(l[0])))
  if len(l[1])!=0:
    print("Candidato Fernando Haddad tem {} votos.".format(len(l[1])))
  if len(l[2])!=0:
    print("Candidato Jair Bolsonaro tem {} votos.".format(len(l[2])))
  if len(l[3])!=0:
    print("Candidato Jo�o Amoedo tem {} votos.".format(len(l[3])))
  if len(l[4])!=0:
    print("Candidato Marina Silva tem {} votos.".format(len(l[4])))
quantidadevotos(l)

n2=len(l)

def ganhador(l,n2):
  g=0
  for k in range(n2):
    if len(l[k])>g:
      g=k
  if g==0 and not len(l[0])==0:
    print("Candidato Ciro Gomes � o novo presidente com {} votos.".format(len(l[0])))
  elif g==1:
    print("Candidato Fernando Haddad � o novo presidente com {} votos.".format(len(l[1])))
  elif g==2:
    print("Candidato Jair Bolsonaro � o novo presidente com {} votos.".format(len(l[2])))
  elif g==3:
    print("Candidato Jo�o Amo�do � o novo presidente com {} votos.".format(len(l[3])))
  elif g==4:
    print("Candidato Marina Silva � a nova presidente com {} votos.".format(len(l[4])))
ganhador(l,n2)