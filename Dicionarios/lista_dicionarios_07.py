cadastro={}

while True:
    
    print("1-Cadastrar Aluno")
    print("2-Alualizar Dados")
    print("3-Sair")
    print("")
    opcao=input("Escolha opcao: ")
    print("")
    
    if opcao=="1":
        aluno={}
        aluno["nome"]=input("Nome do aluno: ").upper()
        aluno["curso"]=input("Curso: ").upper()
        
        endereco={}
        
        print("Endereco:")
        
        endereco["rua"]=input("Nome da rua:").upper()
        endereco["numero"]=input("Numero: ").upper()
        endereco["bairro"]=input("Bairro: ").upper()
        
        aluno["endereco"]=endereco
    
        cadastro[len(cadastro)+1]=aluno
        
        
        
    elif opcao=="2":
        busca=input("Nome do Aluno: ").upper()
        
        for chave, valor in cadastro.items():
            aluno_busca=valor
            
            if aluno_busca["nome"]==busca:
                
                print("O que voce deseja editar: ")
                print("1-Nome")
                print("2-Curso")
                print("3-Endereco")
                print("4-Cancelar")
                
                opcao_edit=input("Insira sua opacoa: ")
                
                if opcao_edit=="1":
                    aluno_busca["nome"]=input("Novo nome:").upper()
                    
                elif opcao_edit=="2":
                    aluno_busca["curso"]=input("Novo Curso: ").upper()
                
                elif opcao_edit=="3":
                    for chave_endereco in aluno_busca["endereco"]:
                        aluno_busca["endereco"][chave_endereco]=input(chave_endereco+":").upper()
                        
                else:
                    break
            
                cadastro[chave]=aluno_busca
                break
            

            
        
    else:
        print(cadastro)
        break
        