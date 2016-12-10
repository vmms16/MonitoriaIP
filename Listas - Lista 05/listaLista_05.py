
while True:
    
    nome=input("Nome do atleta: ")
    
    if nome!="":
        print("Atleta: %s"%(nome))
        lista_salto=[]
        lista_salto.append(float(input("Primeiro salto: ")))
        lista_salto.append(float(input("Segundo salto: ")))
        lista_salto.append(float(input("Terceiro salto: ")))
        lista_salto.append(float(input("Quarto salto: ")))
        lista_salto.append(float(input("Quinto salto: ")))
        
        print("")
        
        print("Resultado final")
        
        print("")
        
        print("Atleta: %s"%(nome))
        print("Saltos: %.2f - %.2f - %.2f - %.2f - %.2f"%(lista_salto[0],lista_salto[1],lista_salto[2],lista_salto[3],lista_salto[4]))
        print("Media saltos: %.2f "%(sum(lista_salto)/5))
        
    else:
        break