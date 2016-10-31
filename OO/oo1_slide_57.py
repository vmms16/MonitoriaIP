class Aluno:
    
    def __init__ (self, nome, cpf):
        self.__nome=nome
        self.__cpf=cpf
        
    def setNome(self,nome):
        self.__nome=nome
        
    def setCpf(self, cpf):
        self.__cpf=cpf
        
    def getNome(self):
        return self.__nome
    
    def getCpf(self):
        return self.__cpf
    

class Equipe:
    def __init__(self,projeto,lista):
        self.__projeto=projeto
        self.__lista=lista
        
    def getLista(self):
        return self.__lista
    
    def setLista(self,lista):
        self.__lista=lista
        
class GerenciadorDeEquipes:
    def __init__(self,listaEquipes):
        self.__listaEquipes=listaEquipes
        
    def inLista