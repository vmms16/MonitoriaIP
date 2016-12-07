numero_aluno=3
soma_notas=0
maior_nota=0
aluno=""

for i in range(0,numero_aluno,1):
    nome=input("Nome do Aluno: ")
    nota=int(input("Nota do aluno: "))
    soma_notas+=nota
    if nota>maior_nota:
        maior_nota=nota 
        aluno=nome
        
        
print("Media da turma: %f"%(soma_notas/numero_aluno))
print("Aluno com maior nota %s:"%(aluno))