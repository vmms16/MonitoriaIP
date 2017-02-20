class Matriz:
    def __init__(self,n):
        self.n=n
        self.matriz=[]
            
    def somaDiagonalPrincipal(self):
        x=self.matriz.size()
        return x
    
    def gerarMatriz(self):
        self.matriz=[]
        for i in range(0,self.n,1):
            x=[]
            for j in range(0,self.n,1):
                if i==j:
                    x.append(1)
                else:
                    x.append(0)
            self.matriz.append(x)
        
    
    def escreverEmArquivos(self):
        arq=open("arq1.txt","a")
        for i in self.matriz:
            linha=""
            for j in i:
                linha+=str(j)+" "
            linha+="\n"
            
            arq.write(linha)
        arq.write("_______________\n")
        arq.close()
            
m=Matriz(5)
m.gerarMatriz()
m.escreverEmArquivos()