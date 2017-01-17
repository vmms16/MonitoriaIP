linhas=int(input("Numero de linhas: "))
colunas=int(input("Numero de colunas: "))
matriz={}

for i in range(1,linhas+1,1):
    for j in range(1, colunas+1,1):
        matriz[i,j]=int(input("Insira um valor: "))
        
for chave,valor in matriz.items():
    if valor%2!=0:
        matriz[chave]=valor*2
        
print(matriz)
    