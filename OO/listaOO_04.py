class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.__nome=nome
        self.__idade=idade
        self.__peso=peso
        self.__altura=altura
        
    def getNome(self):
        return self.__nome
    
    def getIdade(self):
        return self.__idade
    
    def getPeso(self):
        return self.__peso
    
    def getAltura(self):
        return self.__altura
    
    def setNome(self,nome):
        self.__nome=nome
        
    def setIdade(self,idade):
        self.__idade=idade
        
    def setPeso(self,peso):
        self.__peso=peso
        
    def setAltura(self, altura):
        self.__altura=altura
    
    def crescer(self):
        self.setAltura(self.getAltura()+0,05)
        
    def envelhecer(self,anos):
        if self.getIdade()>21:
            self.setIdade(self.getIdade()+anos)
        else:
            diferenca=21-self.getIdade()
            self.setAltura(self.getAltura()+0.05*diferenca)
            self.setIdade(self.getIdade()+anos)
            
    def engordar(self, kg):
        self.setPeso(self.getPeso()+kg)
        
    def emagrecer(self, kg):
        self.setPeso(self.getPeso()+kg)