from random import randint

numero_linhas=int(input("Numero de linhas: "))
numero_colunas=int(input("Numero de Coluna: "))
matriz=[]

for i in range(0,numero_linhas,1):
    
    linha=[]
    
    for j in range(0,numero_colunas,1):
        
        linha.append(randint(0,10))
        
            
    matriz.append(linha)


for i in matriz:
    linha=""
    for j in i:
        linha+=str(j)+" "
    print(linha)