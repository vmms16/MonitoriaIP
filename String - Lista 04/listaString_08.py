
from random import randint

fita1=input("Insira a sequencia de bases 1:")
fita2=input("Insira a sequencia de bases 2:")

ponto_cross=randint(1,len(fita1))

nova_fita1= fita1[:ponto_cross]+fita2[ponto_cross:]
nova_fita2= fita2[:ponto_cross]+fita1[ponto_cross:]

print("Novas fitas a partir do ponto %d"%(ponto_cross))
print("Nova fita 1: "+nova_fita1)
print("Nova fita 2: "+nova_fita2)