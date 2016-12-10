lista=[]

for i in range(0,20,1):
    lista.append(int(input("Insira um numero: ")))
    
soma=sum(lista)
media=soma/len(lista)

menores=[]
for i in lista:
    if i < media:
        menores.append(i)
        
print(menores)