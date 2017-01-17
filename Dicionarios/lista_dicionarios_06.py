linhas=int(input("Numero de linhas: "))
colunas=int(input("Numero de colunas: "))
matriz={}

for i in range(1,linhas+1,1):
    for j in range(1, colunas+1,1):
        matriz[i,j]=input("Insira um valor: ")
        
for i in range(1,linhas+1,1):
    str_matriz=""
    for j in range(1,colunas+1,1):
        str_matriz+=matriz[i,j]+" "
    print(str_matriz)