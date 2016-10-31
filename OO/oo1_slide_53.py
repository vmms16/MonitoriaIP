class Funcionario:
    def __init__(self, nome, salario):
        self.__nome=nome
        self.__salario=salario
        
    def setSalario(self, salario):
        self.__salario=salario
        
    def setNome(self,nome):
        self.__nome=nome
        
    def getSalario(self):
        return self.__salario
    
    def getNome(self):
        return self.__nome
    
    def aumentarSalario(self, porcentagem):
        self.setSalario(self.getSalario()*(1+porcentagem/100))
        

vinicius=Funcionario('Vinicius',3000)
vinicius.aumentarSalario(10)
print(vinicius.getSalario())