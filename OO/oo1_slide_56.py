class Carro:
    
    def __init__(self, consumo, tanque):
        self.__consumo=consumo
        self.__tanque=tanque
        self.__nivelTanque=0
        
    def getNivelTanque(self):
        return self.__nivelTanque
    
    def getConsumo(self):
        return self.__consumo
    
    def getTanque(self):
        return self.__tanque
    
    def setNivelTanque(self, litros):
        self.__nivelTanque=litros
        
    def setConsumo(self, litros_km):
        self.__consumo=litros_km
        
    def setTanque(self,litros):
        self.__tanque=litros
        
    def andar(self,km):
        consumo_total=km*self.getConsumo()
        if consumo_total>self.getNivelTanque():
            print('Combustivel Insuficiente')
        else:
            print('Andou %d kilometros'%(km))
            self.setNivelTanque(self.getNivelTanque()-consumo_total)
            
    def adicionarGasolina(self,litros):
        if self.getNivelTanque()+litros>self.getTanque():
            total_abastecido=self.getTanque()-self.getNivelTanque()
            print('Foi abastevido %d litros'%(total_abastecido))
            self.setNivelTanque(self.getTanque())
        else:
            print('Foi abastecido %d litros'%(litros))
            self.setNivelTanque(self.getNivelTanque()+litros)
        
        
    
carro=Carro(1,20)
        
while True:
    print('-------------')
    print('1-Andar')
    print('2-Abastecer')
    print('3-Parar')
    print('-------------')
    
    x=int(input('Escolha a aopcao: '))
    
    if x==1:
        andar=int(input('Km a ser rodado: '))
        carro.andar(andar)
        
    elif x==2:
        abasterce=int(input('Quantida a ser abastecida: '))
        carro.adicionarGasolina(abasterce)
        
    else:
        print('Chegou ao destino!!')
        break