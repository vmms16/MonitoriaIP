a=""
e=""
i=""
o=""
u=""


frase=input("Inisira uma frase: ")

for x in frase:
    j=x.lower()
    if j=="a":
        a+="*"
    elif j=="e":
        e+="*"
    elif j=="i":
        i+="*"
    elif j=="o":
        o+="*"
    elif j=="u":
        u+="*" 
        
print("a= %s"%(a))
print("e= %s"%(e))
print("i= %s"%(i))
print("o= %s"%(o))
print("u= %s"%(u))