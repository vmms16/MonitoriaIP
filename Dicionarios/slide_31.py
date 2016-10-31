matriz={}
tamanho=3


for i in range(0,tamanho,1):
    for j in range(0,tamanho,1):
        matriz[(i,j)]=int(input("insira posicao (%d,%d): "%(i,j)))
        
print("------Matriz-------")
print()
for i in range(0,tamanho,1):
        print(matriz[(i,0)],matriz[(i,1)],matriz[(i,2)])
        
soma_impar=0
soma_par=0

for i in range(0,tamanho,1):
    for j in range(0,tamanho,1):
        if matriz[(i,j)]%2==0:
            soma_par+=matriz[(i,j)]
        else:
            soma_impar+=matriz[(i,j)]

print()            
print("Soma dos impares= "+str(soma_impar))
print("Soma dos pares= "+str(soma_par))

