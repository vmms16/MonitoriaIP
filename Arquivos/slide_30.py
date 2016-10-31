arqe=open('nomes.txt','r')
lista_nomes=arqe.readlines()
arqe.close()
lista=[]

for i in lista_nomes:
    lista.append(i.strip('\n'))
    
lista.sort()

arqs=open('nomes_saida.txt','w')

for i in lista:
    arqs.write(i+'\n')
arqs.close()