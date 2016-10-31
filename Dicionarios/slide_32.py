import random
from random import randint

linhas=int(input("numero de linhas matriz 1: "))
colunas=int(input("numero de colunas matriz 1: "))

linhas2=int(input("numero de linhas matriz 2: "))
colunas2=int(input("numero de colunas matriz 2: "))


matriz1={}
matriz2={}

for i in range(0,linhas,1):
    for j in range(0,colunas,1):
        matriz1[(i,j)]=randint(0,10)

for i in range(0,linhas2,1):
    for j in range(0,colunas2,1):
        matriz2[(i,j)]=randint(0,10)


matriz_resultado={}
if colunas==linhas2:
    for i in range(0,colunas,1):
        for j in range(0,linhas2,1):
            soma=0
            for l in range(0,colunas,1):
                soma+=matriz1[i,l]*matriz2[l,j]
            matriz_resultado[(i,j)]=soma



