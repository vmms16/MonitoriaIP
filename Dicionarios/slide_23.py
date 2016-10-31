agenda={}


while True:
    print("1- Inserir contato")
    print("2- Imprimir agenda")
    
    opcao=input("prompt")
    
    if opcao=="1":
    
        cpf=input("Insira o cpf: ")
        nome=input("insira o nome: ")
        idade=input("insira a idade: ")
        telefone=input("insira o telefone: ")
        
        agenda[cpf]={"nome": nome, "idade":idade, "telefone": telefone}
        
    elif opcao=="2":
        
        for i in agenda:
            print("%s : %s - %s - %s "%(i,agenda[i]['nome'],agenda[i]['idade'],agenda[i]['telefone']))
            
        break