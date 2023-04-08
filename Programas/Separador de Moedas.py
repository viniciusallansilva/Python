#separador de moedas universal
x=int(input())

qtde = x//10000
x=x%10000
print(qtde, "nota(s) de R$ 100,00.")

qtde2 = x//5000
x=x%5000
print(qtde2, "nota(s) de R$ 50,00.")

qtde21 = x//2000
x=x%2000
print(qtde21, "nota(s) de R$ 20,00.")

qtde3 = x//1000
x=x%1000
print(qtde3, "nota(s) de R$ 10,00.")

qtde4 = x//500
x=x%500
print(qtde4, "nota(s) de R$ 5,00.")

qtde41 = x//200
x=x%200
print(qtde41, "nota(s) de R$ 2,00.")

qtde5 = x//100
x=x%100
print(qtde5, "moeda(s) de R$ 1,00.")

qtde6 = x//50
x=x%50
print(qtde6, "moeda(s) de R$ 0,50.")

qtde7 = x//25
x=x%25
print(qtde7, "moeda(s) de R$ 0,25.")

qtde8 = x//10
x=x%10
print(qtde8, "moeda(s) de R$ 0,10.")

qtde9 = x//5
x=x%5
print(qtde9, "moeda(s) de R$ 0,05.")