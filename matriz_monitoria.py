colunas=int(input("Insira o numero de colunas: "))
linhas=int(input("Insira o numero de linhas: "))

matriz=[]
contador=1

for i in range(0,linhas,1):
    linha=[]
    for j in range(0,colunas,1):
        
        if contador>=10:
            linha.append(str(contador))
        else:
            linha.append("0"+str(contador))
            
        contador+=1
    matriz.append(linha)

print()
    
for x in matriz:
    print(x)