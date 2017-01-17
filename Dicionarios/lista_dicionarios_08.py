from lista_dicionarios_1 import nome
dicionario={}

for i in range(0,6,1):
    nome=input("Nome: ")
    idade=int(input("Idade"))
    dicionario[nome]=idade
    
listaMaior=[]
listaMenor=[]

for nome, idade in dicionario.items():
    if idade>30:
        listaMaior.append(nome)
    else:
        listaMenor.append(nome)
        
print("Maior que 30: ")
print(listaMaior)
print("Menor que 30: ")
print(listaMenor)