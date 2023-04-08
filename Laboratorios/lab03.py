tipo=str(input()) #tipo objeto
car=str(input()) #caractere 
lado=10 
largura=10 
altura=10  
O=10 

def quadrado(car, lado): # função quadrado 
    interno=(lado-2)*" " 
    for a in range(lado): 
        if a==0 or a==(lado-1): 
            print((lado) * car) 
        else: 
            print(car,car,sep=interno)

def retangulo(car, largura, altura): # função rentangulo 
    interno=(largura-2)*" " 
    for b in range(altura): 
        if b==0 or b==(altura-1): 
            print((largura)*car) 
        else: 
            print(car, car, sep=interno)

def paralelogramo(car, largura, altura): #função paralelogramo 
    interno=(largura-2)*" "
    for c in range(altura): 
        if c==0: 
            print(largura*car) 
        elif c==(altura-1): 
            c2=c-1
            print(c2*" ", largura*car)
        else:           
            print(c*" ", end="")
            print(car, car, sep=interno)   
 
def losango(car, lado): #função losango
    for d in range((lado*2)-1):
        if d==0 or d==((lado*2)-2):
            print((lado-1)*" ", end="")
            print(car)
        elif d<=(lado-1) and (d!=0 or d!=((lado*2)-2)):
            print(((lado-1)-d)*" ", end="")
            print(car, car, sep=(((d*2)-1)*" "))
        elif d>(lado-1) and (d!=0 or d!=((lado*2)-2)):                        
            print(((d-lado)+1)*" ", end="")           
            print(car, car, sep=((((lado+1)-((d-lado)+1)+(lado-d)+(lado-5))*" ")))

def cruz(car, lado):    
    interno=((lado-2)*" ")
    for e in range((lado*2)+(lado-2)):
        if e==0 or e==((lado*2)+(lado-2)-1):
            print((lado-1)*" ",lado*car)
        elif e==(lado-1) or e==((lado*2)-2):
            print(lado*car*3)
        elif (e<(lado-1) and e>0) or (e>((lado*2)-2) and e<((lado*2)+(lado-2)-1)):
            print((lado)*" ",end="")
            print(car,car,sep=interno)
        else:
            print(car,car,sep=interno,end="")
            print(car,car,sep=interno,end="")
            print(car,car,sep=interno)

if tipo=="Q" or tipo=="L" or tipo=="C": 
    lado=int(input()) 
elif tipo=="P" or tipo=="R": 
    largura=int(input()) 
    altura=int(input())
elif tipo!="Q" and tipo!="L" and tipo!="C" and tipo!="P" and tipo!="R" :       
    nada=int(input())

if tipo!="Q" and tipo!="L" and tipo!="C" and tipo!="P" and tipo!="R":
    print("Objeto incorreto.")
    o=0
else:
    o=10
    

if lado<3 or largura<3 or altura<3 and o==10: # identificador de dimensoes incorretas 
    print('Dimensao incorreta.') 
elif tipo=="Q":
    quadrado(car, lado)
elif tipo=="R":
    retangulo(car, largura, altura)
elif tipo=="P":
    paralelogramo(car, largura, altura)
elif tipo=="L":
    losango(car, lado)
elif tipo=="C":
    cruz(car, lado)
