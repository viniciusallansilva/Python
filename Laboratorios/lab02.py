c=float(input())
m=float(input())
p=float(input())
marcos=str(input())
maria=str(input())
marcos13=float(input())
maria13=float(input())
hotel=float(input())
passagem=float(input())
notas=0
if c>=7 and m>=7 and p>=7:
  notas=1
else:
  notas=0

if marcos !='Sim' and maria !='Sim' and notas!=0:
  ferias=0
else:
  ferias=1

if marcos13 > 11 and maria13 > 11 and notas!=0 and ferias!=0:
  libera=0
else:
  libera=1

if (hotel+passagem)>10000.00 and notas!=0 and ferias!=0 and libera!=0:
  valores=0
else:
  valores=1

if notas==1 and ferias==1 and libera==1 and valores==1:
  print('SIM!!!')
elif notas!=1:
  print('NAO. As notas da Carla nao foram suficientes.')
elif notas==1 and ferias!=1:
  print('NAO. O casal nao esta de ferias.')
elif notas==1 and ferias==1 and libera!=1:
  print('NAO. Nenhum 13o salario foi liberado a tempo.')
elif notas==1 and ferias==1 and libera==1 and valores!=1:
  print('NAO. O valor total e muito alto.')