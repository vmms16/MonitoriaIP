while True:
    x=int(input("Insira um numero: "))
    if x!=9999 and (x%3==0 or x<0) :
        print(x)
    elif x==9999:
        break
    
    