linhas=int(input("Numero de linhas: "))
colunas=int(input("Numero de colunas: "))
matriz={}

for i in range(1,linhas+1,1):
    for j in range(1, colunas+1,1):
        matriz[i,j]=input("Insira um valor: ")
        
matriz_transposta={}

for i in range(1,linhas+1,1):
    for j in range(1, colunas+1,1):
        matriz_transposta[j,i]=matriz[i,j]
        
for i in range(1,colunas+1,1):
    str_matriz=""
    for j in range(1,linhas+1,1):
        str_matriz+=matriz_transposta[i,j]+" "
    print(str_matriz)
