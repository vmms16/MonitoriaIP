class Aluno:
    def __init__(self, nome, cpf):
        self.__nome=nome
        self.__cpf=cpf
        
    def getNome(self):
        return self.__nome
    
    def getCpf(self):
        return self.__cpf
    
    def setNome(self,novoNome):
        self.__nome=novoNome
        
    def setCpf(self,novoCpf):
        self.__cpf=novoCpf
        

class Equipe:
    
    def __init__(self, listaParticipantes, nomeProjeto):
        self.__listaAlunos=listaParticipantes
        self.__projeto=nomeProjeto
        
    def getListaAlunos(self):
        return self.__listaAlunos
    
    def getProjeto(self):
        return self.__projeto
    
    def setListaAlunos(self,lista):
        self.__listaAlunos=lista
        
    def setProjeto(self, projeto):
        self.__projeto=projeto
    
    def inEquipe(self,aluno):
        for i in self.getListaAlunos():
            if aluno.getCpf()==i.getCpf():
                return True
        return False


class GerenciadorEquipes:
    
    def __init__(self):
        self.__listaEquipes=[]

    def getListaEquipes(self):
        return self.__listaEquipes
    
    
    def criarEquipe(self, equipe):
        criar=True
        for i in self.getListaEquipes():
            if equipe.getProjeto()==i.getProjeto():
                for aluno in equipe.getListaAlunos():
                    if i.inEquipe(aluno):
                        criar=False
                        print ("Equipe noo pode ser criada")
                        break
            if not(criar):
                break
        else:
            self.getListaEquipes().append(equipe)
            

    def listarEquipes(self):
        for i in self.getListaEquipes():
            print('Equipe')
            for j in i.getListaAlunos():
                print(j.getNome())



ge=GerenciadorEquipes()

aluno1=Aluno('Vinicius','291479')
aluno2=Aluno('Romero','666')
aluno3=Aluno('Vinicius','291479')
aluno4=Aluno('Vinicius','2914790')
aluno5=Aluno('Joao','49835')

listaComAlunos=[aluno1,aluno2,aluno4]

equipe=Equipe(listaComAlunos,'Monitoria')
equipe2=Equipe([aluno1],'teste')
ge.criarEquipe(equipe)
ge.criarEquipe(equipe)
ge.criarEquipe(equipe2)
ge.listarEquipes()