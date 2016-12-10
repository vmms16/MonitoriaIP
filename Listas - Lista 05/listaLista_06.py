os=["Windows Server", "Unix", "Linux", "Netware", "Mac", "Outro"]
votos=[0,0,0,0,0,0]

while True:
    
    print("----Votacao ----")
    for i in range(0,6,1):
        print("%d - %s"%(i+1,os[i]))
        
    while True:    
        voto=int(input("Insira seu voto: "))
        
        if voto>=0 and voto<=6:
            break
        else:
            print("Voto Invalido")
    
    if voto==1:
        votos[0]+=1
    
    elif voto==2:
        votos[1]+=1
        
    elif voto==3:
        votos[2]+=1
        
    elif voto==4:
        votos[3]+=1
        
    elif voto==5:
        votos[4]+=1
        
    elif voto==6:
        votos[5]+=1
        
    elif voto==0:
        break


total=sum(votos)
    
print("Sistema Operacional-Votos-Porcentagem")
print("--------------------------------------")
for i in range(0,6,1):
        print("%d - %s  - %d  -  %.2f"%(i+1,os[i],votos[i],100*(votos[i]/total)))
        
print("-------------------------------------")
print("Total           %d"%(total))

print("O vencedor foi o sistema %s com %d votos"%(os[max(votos)], max(votos)))