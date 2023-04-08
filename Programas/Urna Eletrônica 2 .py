print("URNA ELETRÔNICA NO BRASIL, ELEIÇÕES 2018")
print("CANDIDATO/PARTIDO/NUMERO") 
print("Ciro Gomes (PDT): 12") #0
print("Fernando Haddad (PT): 13") #1
print("Jair Bolsonaro (PSL): 17") #2
print("João Amoêdo (Novo): 30")   #3
print("Marina Silva (Rede): 18")  #4
print("DIGITE O NÚMERO DE SEU CANDIDATO E CONFIRME") 
print("Para finalizar a votação, digite 0:")
l=[[],[],[],[],[]]
a=[int(input("O número de seu candidato é:"))]
b=[]
if a[0]==12:
  c=input("Seu candidato é Ciro Gomes?SIM OU NAO?:")
  if c=="SIM":
    l[0].append(1)
    print("Você votou no Ciro Gomes")
elif a[0]==13:
  c=input("Seu candidato é Fernando Haddad?SIM OU NAO?:")
  if c=="SIM":
    l[1].append(1)
    print("Você votou no Fernando Haddad")
elif a[0]==17:
  c=input("Seu candidato é Jair Bolsonaro?SIM OU NAO?:")
  if c=="SIM":
    l[2].append(1)
    print("Você votou no Jair Bolsonaro")
elif a[0]==30:
  c=input("Seu candidato é João Amoêdo?SIM OU NAO?:")
  if c=="SIM":
    l[3].append(1)
    print("Você votou no João Amoêdo")
elif a[0]==18:
  c=input("Seu candidato é Marina Silva?SIM OU NAO?:")
  if c=="SIM":
    l[4].append(1)
    print("Você votou no Marina Silva")
while a[0]!=0: 
  b=b+a
  a=[int(input("O número de seu candidato é:"))]
  if a[0]==12:
    c=input("Seu candidato é Ciro Gomes?SIM OU NAO?:")
    if c=="SIM":
      l[0].append(1)
      print("Você votou no Ciro Gomes")
  elif a[0]==13:
    c=input("Seu candidato é Fernando Haddad?SIM OU NAO?:")
    if c=="SIM":
      l[1].append(1)
      print("Você votou no Fernando Haddad")
  elif a[0]==17:
    c=input("Seu candidato é Jair Bolsonaro?SIM OU NAO?:")
    if c=="SIM":
      l[2].append(1)
      print("Você votou no Jair Bolsonaro")
  elif a[0]==30:
    c=input("Seu candidato é João Amoêdo?SIM OU NAO?:")
    if c=="SIM":
      l[3].append(1)
      print("Você votou no João Amoêdo")
  elif a[0]==18:
    c=input("Seu candidato é Marina Silva?SIM OU NAO?:")
    if c=="SIM":
      l[4].append(1)
      print("Você votou no Marina Silva")
n=len(b)
print("Foram um total de {} votos realizados nessa eleição!".format(n))
if n==0:
  print("Ninguém ganhou, pois não houve voto, logo, LULA vai implantar o comunismo no bagulho")

def quantidadevotos(l):
  if len(l[0])!=0:
    print("Candidato Ciro Gomes tem {} votos.".format(len(l[0])))
  if len(l[1])!=0:
    print("Candidato Fernando Haddad tem {} votos.".format(len(l[1])))
  if len(l[2])!=0:
    print("Candidato Jair Bolsonaro tem {} votos.".format(len(l[2])))
  if len(l[3])!=0:
    print("Candidato João Amoedo tem {} votos.".format(len(l[3])))
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
    print("Candidato Ciro Gomes é o novo presidente com {} votos.".format(len(l[0])))
  elif g==1:
    print("Candidato Fernando Haddad é o novo presidente com {} votos.".format(len(l[1])))
  elif g==2:
    print("Candidato Jair Bolsonaro é o novo presidente com {} votos.".format(len(l[2])))
  elif g==3:
    print("Candidato João Amoêdo é o novo presidente com {} votos.".format(len(l[3])))
  elif g==4:
    print("Candidato Marina Silva é a nova presidente com {} votos.".format(len(l[4])))
ganhador(l,n2)