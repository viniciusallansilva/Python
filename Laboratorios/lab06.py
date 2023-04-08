a=int(input())
time={}
pt={}
vit={}
saldo={}
gpro={}
gsofridos={}
for b in range(a*(a-1)):
  c=input()
  d=c.split()
  d[1]=int(d[1])
  d[4]=int(d[4])
  casa=d[0]
  golscasa=d[1]
  visitante=d[3]
  golsvisitante=d[4]
  if not casa in time:
    time[casa]=0
    pt[casa]=0
    vit[casa]=0
    saldo[casa]=0
    gpro[casa]=0
    gsofridos[casa]=0 
  if not visitante in time:
    time[visitante]=0
    pt[visitante]=0
    vit[visitante]=0
    saldo[visitante]=0
    gpro[visitante]=0
    gsofridos[visitante]=0 
  
  gpro[casa] += d[1]
  gsofridos[casa] += d[4]
  saldo[casa] = gpro[casa] - gsofridos[casa]  
  
  gpro[visitante] += d[4]
  gsofridos[visitante] += d[1]
  saldo[visitante] = gpro[visitante] - gsofridos[visitante]
  
  if golscasa>golsvisitante:
    vit[casa] += 1
    pt[casa] += 3
  elif golscasa==golsvisitante:
    pt[casa] += 1
    pt[visitante] += 1
  else:
    vit[visitante] += 1
    pt[visitante] += 3
for t in sorted(pt):
  print(t,pt[t],vit[t],saldo[t],gpro[t])

e=0
f=0
g=0
h=0
vencedor=0
for v in pt:
  if pt[v]==(max(pt.values())):
    e=e+1
    vencedor=v
if e<2:
  print("Vencedor: {}".format(vencedor))
elif e>=2:
  for u in vit:
    if vit[u]==(max(vit.values())):
      f=f+1
      vencedor=u
  if f<2:
    print("Vencedor: {}".format(vencedor))
  elif f>=2:
    for x in saldo:      
      if saldo[x]==(max(saldo.values())):
        g=g+1
        vencedor=x
    if g<2:
      print("Vencedor: {}".format(vencedor))
    elif g>=2:
      for w in gpro:
        if gpro[w]==(max(gpro.values())):
          vencedor=w
          print("Vencedor: {}".format(vencedor))
