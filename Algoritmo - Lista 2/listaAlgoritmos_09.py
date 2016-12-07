saque=int(input("Insira a quantidade desejada: "))

n100=0
n50=0
n20=0
n10=0
n5=0
n2=0

while saque!=0:
    if saque>=100:
        n100=saque//100
        saque-=100*n100
    elif saque>=50:
        n50=saque//50
        saque-=50*n50
    elif saque>=20:
        n20=saque//20
        saque-=20*n20
    elif saque>=10:
        n10=saque//10
        saque-=10*n10
    elif saque>=5:
        n5=saque//5
        saque-=5*n5
    elif saque>=2:
        n2=saque//2
        saque-=2*n2
        
print("notas de 100: %d"%(n100))
print("notas de 50: %d"%(n50))
print("notas de 20: %d"%(n20))
print("notas de 10: %d"%(n10))
print("notas de 5: %d"%(n5))
print("notas de 2: %d"%(n2))