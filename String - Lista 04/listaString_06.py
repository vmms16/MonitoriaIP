frase=input("Insira uma frase: ")

palindromo=frase.replace(" ","")

if palindromo==palindromo[::-1]:
    print(" %s e um palindromo"%(frase))