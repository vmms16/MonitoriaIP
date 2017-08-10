class Assento:
    def __init__(self, numero , preco=20.00, disponivel=True):
        self.__numero=numero
        self.__preco=preco
        self.__disponivel=disponivel

    def getNumero(self):
        return self.__numero

    def getPreco(self):
        return self.__preco

    def getDisponivel(self):
        return self.__disponivel

    def setNumero(self, numero):
        self.__numero=numero

    def setPreco(self, preco):
        self.__preco=preco

    def setDisponivel(self, disponivel):
        self.__disponivel = disponivel


class ControladorAssento:
    def __init__(self):
        self.__matrizAssentos=[]

    def gerarMatriz(self, linhas , colunas):
        contador=0
        for l in range(0,linhas,1):
            linhaTemp=[]
            for c in range(0,colunas,1):
                assentoTemp=Assento(contador, 20 - l)
                linhaTemp.append(assentoTemp)
                contador+=1
            self.__matrizAssentos.append(linhaTemp)

    def printMatrizAssentoNumero(self):
        for l in self.__matrizAssentos:
            linha=""
            for assento in l:
                linha+=str(assento.getNumero())+" "
            print(linha)

    def printMatrizAssentoDisponivel(self):
        for l in self.__matrizAssentos:
            linha=""
            for assento in l:
                linha+=str(assento.getDisponivel())+" "
            print(linha)

    def printMatrizAssentoPreco(self):
        for l in self.__matrizAssentos:
            linha=""
            for assento in l:
                linha+=str(assento.getPreco())+" "
            print(linha)
        

    def comprarAssento(self, numero):
        for l in range(0, len(self.__matrizAssentos)):
            for c in range(0, len(self.__matrizAssentos[0])):
                if numero == self.__matrizAssentos[l][c].getNumero():
                    if self.__matrizAssentos[l][c].getDisponivel():
                        self.__matrizAssentos[l][c].setDisponivel(False)
                        self.registroDeOperacoes(self.__matrizAssentos[l][c])
                        print("Assento comprado")
                        return True
                    else:
                        return False
                        print("Assento Indisponivel")

    def devolverAssento(self, numero):
        for l in range(0, len(self.__matrizAssentos)):
            for c in range(0, len(self.__matrizAssentos[0])):
                if numero == self.__matrizAssentos[l][c].getNumero():
                    if not self.__matrizAssentos[l][c].getDisponivel():
                        self.__matrizAssentos[l][c].setDisponivel(True)
                        self.registroDeOperacoes(self.__matrizAssentos[l][c])
                        print("Assento devolvido com sucesso")
                        break
                    else:
                        print("Erro: Assento ja estava disponivel")

    def comprarAssentos(self, *numeroAssentos):
        for i in numeroAssentos:
            print (i)
            if self.comprarAssento(i):
                continue
            else:
                print("Compra do assento %s cancelada"%(i))

    def registroDeOperacoes(self, assento):
        arquivo=open("resitro.txt","a")
        string="%d: %f :%s \n"%(assento.getNumero(), assento.getPreco(), str(assento.getDisponivel()))
        arquivo.write(string)
        
            
        
        



controlador=ControladorAssento()
controlador.gerarMatriz(3,3)
controlador.comprarAssentos(0,1)
controlador.devolverAssento(0)
