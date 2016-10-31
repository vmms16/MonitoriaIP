class BombaCombustivel:
    def __init__(self, tipoCombustivel, valorCombustivel, quantidadeCombustivel):
        self.__tipoCombustivel=tipoCombustivel
        self.__valorCombustivel=valorCombustivel
        self.__quantidadeCombustivel=quantidadeCombustivel
        
    def getTipo(self):
        return self.__tipoCombustivel
    
    def getValorPorLitro(self):
        return self.__valorCombustivel
    
    def getQuantidadeNaBomba(self):
        return self.__quantidadeCombustivel
    
    def setTipo(self, tipo):
        self.__tipoCombustivel=tipo
        
    def setValorPorLitro(self, valor):
        self.__valor=valor
        
    def setQuantidadeNaBomba(self, quantidade):
        self.__quantidadeCombustivel=quantidade
        
    def abastecerPorValor(self, valor):
        litrosAbastecer= self.getValorPorLitro()*valor
        if litrosAbastecer<= self.getQuantidadeNaBomba():
            self.setQuantidadeNaBomba(self.getQuantidadeNaBomba()-litrosAbastecer)
        else:
            print('Quantidade Insuficiente na Bomba')
            
    def abastecerPorLitro(self,litros):
        if litros>self.getQuantidadeNaBomba():
            print('Quantidade Insuficiente na Bomba')
        else:
            totalPagar=litros*self.getValorPorLitro()
            self.setQuantidadeNaBomba(self.getQuantidadeNaBomba()-litros)
            return totalPagar
        
    def alterarValor(self,valor):
        self.setValorPorLitro(valor)
        
    def alterarCombustivel(self,combustivel):
        self.setTipo(combustivel)
        
    def alterarQuantidadeCombustivel(self, quantidade):
        self.setQuantidadeNaBomba(quantidade)
        
        
bomba= BombaCombustivel('Gasolina', 3.14 , 500)
bomba.abastecerPorLitro(600)
print(bomba.abastecerPorLitro(40))
bomba.abastecerPorValor(100)
print(bomba.getTipo())
print(bomba.getQuantidadeNaBomba())
print(bomba.getValorPorLitro())
bomba.alterarCombustivel('Disel')
bomba.alterarQuantidadeCombustivel(1000)
bomba.alterarValor(2.7)
print(bomba.getTipo())
print(bomba.getQuantidadeNaBomba())
print(bomba.getValorPorLitro())