x=input("Insira uma frase: ")
arqe=open('arquivo.txt','w')
arqe.write(x)
arqe.close()

arqs=open('arquivo.txt','r')
print(arqs.readline())