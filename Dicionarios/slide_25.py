dic_principal={}
dic_backup={}
ip=0
parada=True

while parada:
    while len(dic_principal)<5:
        
        dado=input("inisira um dado:")
        if dado=='0':
            parada=False
            break
        dic_principal[ip]=dado
        ip+=1
        
        
    dic_backup.update(dic_principal)
    dic_principal.clear()
    
print(dic_principal)
print(dic_backup)