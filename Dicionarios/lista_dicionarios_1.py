agenda={}  
     

while True:
    print("1- Inserir contato")
    print("2- Imprimir maior idade")
    
    opcao=input("Insira uma opcao: ")
    
    if opcao=="1":
    
        cpf=input("Insira o cpf: ")
        nome=input("insira o nome: ")
        idade=int(input("insira a idade: "))
        
        agenda[cpf]={"nome": nome, "idade":idade}
    
    elif opcao=='2':
        maior=0
        cpf=""
        for i in agenda:
            if agenda[i]["idade"]>maior:
                maior=agenda[i]['idade']
                cpf=i
                    
        print("Usuario: %s  Idade:%d"%(agenda[cpf]['nome'],agenda[cpf]['idade']))
        break