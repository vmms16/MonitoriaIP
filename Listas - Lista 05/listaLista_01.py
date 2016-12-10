lista=[]

for i in range(0,8,1):
    lista.append(int(input("Insira um numero: ")))
    

maior=max(lista)
posicao=lista.index(maior)

print("O maior numero e %d na posicao %d"%(maior,posicao))