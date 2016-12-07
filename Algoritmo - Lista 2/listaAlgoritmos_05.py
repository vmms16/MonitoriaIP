numero_pessoas=3
maior_altura=0
menor_altura=9999
numero_homens=0
numero_mulheres=0
soma_altura_mulheres=0

for i in range(0,numero_pessoas,1):
    sexo=input("sexo: ")
    altura=float(input("altura: "))
    
    if altura>maior_altura:
        maior_altura=altura
    
    if altura<menor_altura:
        menor_altura=altura
        
    if sexo.upper()=='FEMININO':
        soma_altura_mulheres+=altura
        numero_mulheres+=1
    else:
        numero_homens+=1
        
print("Maior altura: %f"%(maior_altura))
print("Menor altura: %f"%(menor_altura))
print("Media de altura das mulheres: %f"%(soma_altura_mulheres/numero_mulheres))
print("Numero de homens: %d "%(numero_homens))