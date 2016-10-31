class Aluno:
    
    def __init__(self, nome, curso, tempoSemDormir=0):
        self.__nome=nome
        self.__curso=curso
        self.__tempoSemDormir= tempoSemDormir
        
    def setNome(self, nome):
        self.__nome=nome
        
    def setCurso(self,curso):
        self.__curso=curso
        
    def setTempoSemDormir(self,tempoSemDormir):
        self.__tempoSemDormir=tempoSemDormir
        
    def getNome(self):
        return self.__nome
    
    def getCurso(self):
        return self.__curso
    
    def getTempoSemDormir(self):
        return self.__tempoSemDormir
    
    def estudar(self,horas):
        self.setTempoSemDormir(self.getTempoSemDormir()+horas)
        
    def dormir(self,horas):
        self.setTempoSemDormir(self.getTempoSemDormir()-horas)
        
        
# Programa Teste

aluno=Aluno('Vinicius','Sistema de Informacao')

for i in range(1,8,1):
    print('%d da Semana'%(i) )
    x=float(input('Horas de estudo: '))
    y=float(input('Horas de sono: '))
    aluno.estudar(x)
    aluno.dormir(y)
    
print('Horas sem dormir: '+str(aluno.getTempoSemDormir()))