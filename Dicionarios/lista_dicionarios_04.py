lista_A=["09210932","2309520","0934242"]
lista_B=["Vinicius", "Mateus", "Romero"]
dicionario={}

if len(lista_A)==len(lista_B):
    for i in range(0,len(lista_A),1):
        dicionario[lista_A[i]]=lista_B[i]
        
print(dicionario)