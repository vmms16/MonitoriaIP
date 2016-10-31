agenda={}  
agendamenos18={}      

while True:
    print("1- Inserir contato")
    print("2- Imprimir agenda")
    
    opcao=input("Insira uma opcao: ")
    
    if opcao=="1":
    
        cpf=input("Insira o cpf: ")
        nome=input("insira o nome: ")
        idade=int(input("insira a idade: "))
        
        agenda[cpf]={"nome": nome, "idade":idade}
        
    elif opcao=="2":
        lista=[]
        for i in agenda:
            if agenda[i]['idade']<18:
                agendamenos18[i]=agenda[i]
                
        for j in agendamenos18:
                agenda.pop(j)
                
        print(agenda)
        print(agendamenos18)
        break