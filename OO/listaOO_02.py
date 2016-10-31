class Funcionario:
    def __init__(self, nome, salario):
        self.__nome=nome
        self.__salario=salario
        
    def getNome(self):
        return self.__nome
    
    def getSalario(self):
        return self.__salario
    
    def setNome(self,nome):
        self.__nome=nome
        
    def setSalario(self,salario):
        self.__salario=salario
        
    def retornarDados(self):
        print("Nome: %s    Salario: %f"%(self.getNome(),self.getSalario()))
        
        
        
vinicius=Funcionario('Vinicius', 2500.00)
vinicius.retornarDados()