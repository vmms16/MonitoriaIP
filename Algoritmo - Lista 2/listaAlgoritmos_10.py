
while True:

    print("1-Somar")
    print("2-Subtrair")
    print("3-Multiplicar")
    print("4-Dividir")
    print("5-Nao fazer operacao")
    
    x=int(input("Insira uma opcao: "))
    
    if x==1:
        numero1=int(input("Insira o primeiro numero: "))
        numero2=int(input("Insira o segundo numero: "))
        print("Soma= %d"%(numero1+numero2))
    elif x==2:
        numero1=int(input("Insira o primeiro numero: "))
        numero2=int(input("Insira o segundo numero: "))
        print("Subtracao= %d"%(numero1-numero2))
    elif x==3:
        numero1=int(input("Insira o primeiro numero: "))
        numero2=int(input("Insira o segundo numero: "))
        print("Multiplicacao= %d"%(numero1*numero2))
    elif x==4:
        numero1=int(input("Insira o primeiro numero: "))
        numero2=int(input("Insira o segundo numero: "))
        print("Divisao= %d"%(numero1/numero2))
    elif x==5:
        break