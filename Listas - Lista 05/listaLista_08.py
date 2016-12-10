numero_linhas=int(input("Numero de linhas: "))
numero_colunas=int(input("Numero de Coluna: "))
matriz=[]
for i in range(0,numero_linhas,1):
    linha=[]
    for j in range(0,numero_colunas,1):
        if i==j:
            linha.append(1)
        else:
            linha.append(0)
            
    matriz.append(linha)
    
for i in matriz:
    print(i)