import random

alunoa = str(input('Digite o nome do 1 aluno: '))
alunoy = str(input('Digite o nome do 2 aluno: '))
alunox = str(input('Digite o nome do 3 aluno: '))
alunob = str(input('Digite o nome do 4 aluno: '))
lista = (alunob,alunoy,alunox,alunoa)
sort = random.sample(lista, 1)
print('O Escolhido Foi o aluno: {}!'.format(sort))