arqe=open('ip.txt','r')
lista_ip=arqe.readlines()

for i in lista_ip:
    ip=i.strip('\n').split('.')
    n=0
    for j in ip:
        if int(j)>254:
            n+=1
    
    if n==0:
        print(i.strip('\n')+" e valido")
    else:
        print(i.strip('\n')+" e invalido")