class ContaFacebook:
    def __init__(self, nome, idade, listaAmigos=[]):
        self.__nome=nome
        self.__idade=idade
        self.__listaAmigos=listaAmigos
        
    def getListaAmigos(self):
        return self.__listaAmigos
        
    def addAmigos(self, amigo):
        self.getListaAmigos().append(amigo)
        
    def conhecePessoa(self, pessoa):
        if pessoa in self.getListaAmigos():
            return 'Sim'
        else:
            return 'Nao'
        
        
vinicius= ContaFacebook('Vinicius',26)
vinicius.addAmigos('Julio')
print(vinicius.conhecePessoa('Julio'))