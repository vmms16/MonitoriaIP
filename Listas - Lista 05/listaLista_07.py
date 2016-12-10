lista1=["a","b","c","d","e"]
lista2=[1,2,3]
lista_intercalada=[]


while True:

    if len(lista2)!=0:
        x=lista2.pop(0)
        lista_intercalada.append(x)
        
    if len(lista1)!=0:
        x=lista1.pop(0)
        lista_intercalada.append(x)
        
    if len(lista1)==0 and len(lista2)==0:
        break
    
print(lista_intercalada)