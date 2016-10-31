class Livro:
    def __init__(self, nome, autor, qtdpag, preco):
        self.__nome=nome
        self.__autor=autor
        self.__qtdpag=qtdpag
        self.__preco=preco
        
    def getPreco(self):
        return self.__preco
    
    def setPreco(self, preco):
        self.__preco=preco
        
        
livro=Livro('Introducao ao Py','Vinicius', 50, 25)
livro.setPreco(30)
print(livro.getPreco())