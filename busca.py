matriz=[]
n=1
for i in range (0,3,1):
    linha=[]
    for j in range(0,3,1):
        linha.append(n)
        n+=1
    matriz.append(linha)
    
posicao=9
linha=posicao//3
coluna= posicao%3

    
print(matriz)
if posicao%3==0:
    print(matriz[linha-1][-1])
else:
    print(matriz[linha][coluna-1])