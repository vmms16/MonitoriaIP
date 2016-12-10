import random
from random import randint

lista_pessoas=[]

for i in range(0,10,1):
    lista_pessoas.append(input("Insira um nome: "))
    
while True:
    random.shuffle(lista_pessoas)
    primeira=lista_pessoas[randint(0,len(lista_pessoas)-1)]
    random.shuffle(lista_pessoas)
    segunda=lista_pessoas[randint(0,len(lista_pessoas)-1)]

    if primeira!=segunda:
        break
    
print("A primeira pessoa sorteada foi %s"%(primeira))
print("A segunda pessoa sorteada foi %s"%(segunda))