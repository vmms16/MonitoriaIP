import random
from random import randint

lista_1=["0","1","2","3","4","5","6","7","8","9"]
lista_2=lista_1[:]
lista_dezenas=[]

random.shuffle(lista_1)
random.shuffle(lista_2)

print(lista_1)
print(lista_2)

for i in range(0,6,1):
    dezena="00"
    while dezena=="00":
        dezena=lista_1[randint(0,len(lista_1)-1)]+lista_2[randint(0,len(lista_2)-1)]
                       
    lista_dezenas.append(dezena)
    
print("Lista das dezenas: ")
print(lista_dezenas)