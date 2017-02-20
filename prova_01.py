class Aluno():
    def __init__(self, cpf, nota, nome):
        self.__cpf=cpf
        self.__nome=nome
        self.__nota=nota
        
    def getCpf(self):
        return self.__cpf
    
    def getNome(self):
        return self.__nome
    
    def getNota(self):
        return self.__nota
    
    def setCpf(self,cpf):
        self.__cpf=cpf
        
    def setNome(self,nome):
        self.__nome=nome
        
    def setNota(self, nota):
        self.__nota=nota
        
    def dadosAlunos(self):
        print("Nome: "+ self.getNome())
        print("Cpf: "+ self.getCpf())
        print("Nota: "+ str(self.getNome())) 
        
class Monitor(Aluno):
    def __init__(self, cpf,nota ,nome, listaAlunos=[]):
        Aluno.__init__(self, cpf, nota, nome)
        self.__listaAlunos=listaAlunos
        
    def addAluno(self,aluno):
        for i in self.__listaAlunos:
            if aluno.getCpf() == i.getCpf():
                print("Aluno nao pode ser add")
                break
        else:
            self.__listaAlunos.append(aluno)
            
    
    def printDados(self):
        self.dadosAlunos()
        print("Monitorandos: ")
        for i in self.__listaAlunos:
            print(i.getNome())
        
    def salvarArquivo(self, nomeDoArquivo):
        arqNome=nomeDoArquivo+".txt"
        arquivo= open(arqNome,"w")
        arquivo.write(self.getNome()+"\n")
        arquivo.write(self.getCpf()+"\n")
        arquivo.write(str(self.getNota())+"\n")
        for i in self.__listaAlunos:
            arquivo.write(i.getNome+"\n")
        arquivo.close()
        
monitor= Monitor("23746239", 8, "Vinicius")
monitor.salvarArquivo("monitoria")
    
        
        
        
    
        
        