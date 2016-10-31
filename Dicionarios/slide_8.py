lista=[]

d={'nome':"Vinicius", "telefone":"95209732",'endereco':'Rua do Limoreiro', 'idade':25}

for x in d:
    lista.append(x)
    
lista.sort()

for i in lista:
    print(i+":"+str(d[i]))
    