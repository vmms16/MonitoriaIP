
while True:
    
    n=int(input("Insira um numero: "))
    
    for i in range(1,n+1,1):
        if n%i==0:
            print(i)
            
    
    decisao=input("Deseja informar outro numero? ")
    
    if decisao.upper()!="SIM":
        break
    else:
        print("Ate logo")