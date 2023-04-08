print("BEM VINDO A URNA ELETRÔNICA DE VOTAÇÃO PARA 2018")
print("OS CANDIDATOS, SEU PARTIDO E SEU NÚMERO SÃO:")
print("Alvaro Dias (Podemos): 19")
print("Cabo Daciolo (Patriota): 51")
print("Ciro Gomes (PDT): 12")
print("Eymael (DC): 27")
print("Fernando Haddad (PT): 13")
print("Geraldo Alckmin (PSDB): 45")
print("Guilherme Boulos (PSol): 50")
print("Henrique Meirelles (MDB): 15")
print("Jair Bolsonaro (PSL): 17")
print("João Amoêdo (Novo): 30")
print("João Vicente Goulart (PPL): 54")
print("Marina Silva (Rede): 18")
print("Vera Lúcia (PSTU): 16")
print("Digite o número de seu candidato e aperte ENTER. Para finalizar a votação, digite 0 ")
a=[int(input("Número do meu candidato:"))]
b=[]
while a[0]!=0:
  b=b+a
  a=[int(input("Número do meu candidato:"))]
n=len(b)
print("Número de votos:",n)

ad=0
cd=0
cg=0
ey=0
fh=0
ga=0
gb=0
hm=0
jb=0
ja=0
jg=0
ms=0
vl=0

for i in range(n):
  if b[i]==19:
    ad=ad+1
  elif b[i]==51:
    cd=cd+1
  elif b[i]==12:
    cg=cg+1
  elif b[i]==27:
    ey=ey+1
  elif b[i]==13:
    fh=fh+1
  elif b[i]==45:
    ga=ga+1
  elif b[i]==50:
    gb=gb+1
  elif b[i]==15:
    hm=hm+1
  elif b[i]==17:
    jb=jb+1
  elif b[i]==30:
    ja=ja+1
  elif b[i]==54:
    jg=jg+1
  elif b[i]==18:
    ms=ms+1
  elif b[i]==16:
    vl=vl+1

if ad!=0:
  print("Alvaro tem:", ad, "votos")
if cd!=0:
  print("Cabo daciolo tem:", cd, "votos")
if cg!=0:
  print("Ciro tem:", cg, "votos")
if ey!=0:
  print("Eymael tem:", ey, "votos")
if fh!=0:
  print("Haddad tem:", fh, "votos")
if ga!=0:
  print("Geraldo tem:", ga, "votos")
if gb!=0:
  print("Boulos tem:", gb, "votos")
if hm!=0:
  print("Meirelles tem:", hm, "votos")
if jb!=0:
  print("Bolsonaro tem:", jb, "votos")
if ja!=0:
  print("Amoedo tem:", ja, "votos")
if jg!=0:
  print("Goulart tem:", jg, "votos")
if ms!=0:
  print("Marina tem:", ms, "votos")
if vl!=0:
  print("Vera tem:", vl, "votos")

g=ad
for x in range(1):
  if cd>g:
    g=cd
    print("O novo presidente é: cabo daciolo, com",cd,"votos")
  elif ey>g:
    g=ey
    print("O novo presidente é: eymael, com",ey,"votos")
  elif fh>g:
    g=fh
    print("O novo presidente é: haddad, com",fh,"votos")
  elif ga>g:
    g=ga
    print("O novo presidente é: alckmin, com",ga,"votos")
  elif gb>g:
    g=gb
    print("O novo presidente é: boulous, com",gb,"votos")
  elif hm>g:
    g=hm
    print("O novo presidente é: meirelles, com",hm,"votos")
  elif jb>g:
    g=jb
    print("O novo presidente é: bolsonaro, com",jb,"votos")
  elif ja>g:
    g=ja
    print("O novo presidente é: amoedo, com",ja,"votos")
  elif jg>g:
    g=jg
    print("O novo presidente é: goulart, com",jg,"votos")
  elif ms>g:
    g=ms
    print("O novo presidente é: marina, com",ms,"votos")
  elif vl>g:
    g=vl
    print("O novo presidente é: vera, com",vl,"votos")
  else:
    g=ad
    print("O novo presidente é: alvaro, com",ad,"votos")
 # melhorar programa e comprimilo