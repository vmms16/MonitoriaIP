class ValeEletronico:
    def __init__(self, usuario, cpf, saldo=0):
        self.__usuario=usuario
        self.__cpf=cpf
        self.__saldo=saldo
        
    def setUsuario(self, usuario):
        self.__usuario=usuario
        
    def setCpf(self, cpf):
        self.__cpf=cpf
        
    def setSaldo(self, saldo):
        self.__saldo=saldo
        
    def getUsuario(self):
        return self.__usuario
    
    def getCpf(self):
        return self.__cpf
    
    def getSaldo(self):
        return self.__saldo
    
    def carregar(self,valor):
        self.setSaldo(self.getSaldo()+valor)
        
    def verificarSaldo(self):
        print(self.getSaldo())
        
class VemEstudante(ValeEletronico):
    def __init__(self,usuario, cpf, saldo, instituicaoEnsino):
        ValeEletronico.__init__(self, usuario, cpf, saldo)
        self.__instiruicaoEnsino=instituicaoEnsino
        
    def usarPassagem(self, precoPassagem):
        if self.getSaldo()-precoPassagem/2<0:
            return 'Saldor insuciente'
        else:
            self.setSaldo(self.getSaldo()-precoPassagem/2)
            
    
class VemTrabalhador(ValeEletronico):
    
    def __init__(self, usuario, cpf, saldo, empresa):
        ValeEletronico.__init__(self, usuario, cpf, saldo)
        self.__empresa=empresa
        
    def usarPassagem(self, precoPassagem):
        if self.getSaldo()-precoPassagem<0:
            return 'Saldor insuciente'
        else:
            self.setSaldo(self.getSaldo()-precoPassagem)
            
        
            
        

vale= ValeEletronico('Vinicius', '094284392')
vale.verificarSaldo()
vale.carregar(120)
vale.verificarSaldo()

estudante= VemEstudante('Joao','123456789', 0, 'UFRPE')
estudante.carregar(100)
estudante.usarPassagem(2)
estudante.verificarSaldo()

trabalhador= VemTrabalhador('Joao','123456789', 0, 'UFRPE')
trabalhador.carregar(100)
trabalhador.usarPassagem(2)
trabalhador.verificarSaldo()
