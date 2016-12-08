nome=input("Insira seu nome: ")

primeiro_nome=nome[:nome.find(" "):1]
reverso=nome[::-1]
ultimo_nome=reverso[:reverso.find(" "):1]
ultimo_nome=ultimo_nome[::-1]


print("%s, %s"%(ultimo_nome,primeiro_nome))