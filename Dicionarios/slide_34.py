from random import randint

matriz={}

for i in range(0,4,1):
    for j in range(0,4,1):
        matriz[(i,j)]=randint(0,10)


medias=[]

for i in range(0,4,1):
    soma=0
    for j in range (0,4,1):
        soma+=matriz[(i,j)]
    
    medias.append(soma/4)
    
for i in range(0,4,1):
    print(matriz[(i,0)],matriz[(i,1)],matriz[(i,2)],matriz[(i,3)])

print()

print(medias)
        