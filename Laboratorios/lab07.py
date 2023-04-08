moddle0=input()
moddle=moddle0.split()
soma=0
for a in moddle:
  soma+=float(a)
media=(soma/(len(moddle)))
print("Media das atividades conceituais: {:.1f}".format(media))

def tupla_float_int(x):
  f=0
  i=0
  x=x[1:-1]     # remove parênteses
  x=x.split(",")  #separa em 2 str
  f=float(x[0])   # trf srt em float
  i=int(x[1])    #2 str em float
  return (f,i)

soma2=0
soma3=0
notas_lab = [tupla_float_int(x) for x in input().split()]
for b in notas_lab:
  soma2+=(b[0]*b[1])
  soma3+=b[1]
media2=(soma2/soma3)
print("Media das tarefas de laboratorio: {:.1f}".format(media2))

prova=[float(y) for y in input().split()]
p1=prova[0]
p2=prova[1]
media3=(p1*2+p2*3)/5
print("Media das provas: {:.1f}".format(media3))

freq=float(input())
if freq>=75:
  if (media2>=5 and media3>=5):
    Me = 0.6 * media3 + 0.3 * media2 + 0.1 * media
    print("Aprovado(a) por nota e frequência.")
    print("Media final: {:.1f}".format(max(5,Me)))
  elif media3<=2.5 or media2<=2.5:
    print("Reprovado(a) por nota.")
    print("Media final: {:.1f}".format(min(media3,media2)))
  else:
    exame=float(input())
    media4=(min(media2,media3)+exame)/2
    print("Nota no exame: {:.1f}".format(exame))
    if media4>=5:
      print("Aprovado(a) por nota e frequência.")
      print("Media final: {:.1f}".format(media4))
    else:
      print("Reprovado(a) por nota.")
      print("Media final: {:.1f}".format(media4))
else:
  print("Reprovado(a) por frequencia.")
  print("Media final: {:.1f}".format(min(media2,media3)))