linhas_colunas=int(input("Numero de linhas: "))

matriz={}

for i in range(1,linhas_colunas+1,1):
    for j in range(1, linhas_colunas+1,1):
        matriz[i,j]=int(input("Insira um valor: "))
        
produto_diagonal=1

for i in range(1,linhas_colunas+1,1):
    produto_diagonal*=matriz[i,i]
    
    
print("Produto diagonal principal: "+str(produto_diagonal))