
from random import randint

matriz={}

for i in range(0,4,1):
    for j in range(0,4,1):
        matriz[(i,j)]=randint(0,10)
        
        
for i in range(0,4,1):
    print(matriz[(i,0)],matriz[(i,1)],matriz[(i,2)],matriz[(i,3)])
    
for j in range(0,4,1):
    matriz[(1,j)],matriz[(2,j)]=matriz[(2,j)],matriz[(1,j)]
    
for j in range(0,4,1):
    matriz[(0,j)],matriz[(3,j)]=matriz[(3,j)],matriz[(0,j)]

print()
for i in range(0,4,1):
    print(matriz[(i,0)],matriz[(i,1)],matriz[(i,2)],matriz[(i,3)])
 