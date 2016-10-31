import os
os.chdir('C:\\Users\\Vinicius\\Desktop\\Vinicius\\UFRPE\\Projetos - Eclipse')

arqe=open('exercicios2.txt','r')
dic={}
x=arqe.readlines()
arqe.close()

for i in x:
    y=i.strip('\n').split(' ')
    dic[y[0]]=y[1]    

print(dic)