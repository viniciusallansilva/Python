a=int(input())
b=[]
l=0
n=0
h=0
e=0
for k in range(a):
  c=[str(input())]
  b=b+c
for i in range(a):
  if b[i].isalpha()==True:
    l=l+1
    print(b[i])
  elif (b[i][0]=="-" and b[i][1:].isdigit()==True) or b[i].isdigit()==True:
    n=n+1
    print(b[i])
  elif b[i][0]=="#" and b[i][1:].isalpha()==True:
    h=h+1
  else:
    e=e+1
if h==1:
  print(h,"hashtag foi removida.")
elif h!=0 and h!=1:
  print(h,"hashtags foram removidas.")

if e==1:
  print(e,"emoticon foi removido.")
if e!=0 and e!=1:
  print(e,"emoticons foram removidos.")
