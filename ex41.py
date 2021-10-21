from datetime import date
atual = date.today().year
ano = int(input('Qual sua Data de Nascimento? '))
idade = atual - ano

if idade > 0 and idade <= 9:
    print('O Aluno tem {} anos'.format(idade))
    print('\033[1;34mMIRIM')
elif idade > 0 and idade <= 14:
    print('O Aluno tem {} anos'.format(idade))
    print('\033[1;34mINFANTIL')
elif idade > 0 and idade <= 19:
    print('O Aluno tem {} anos'.format(idade))
    print('\033[1;34mJUNIOR')
elif idade > 0 and idade <= 25:
    print('O Aluno tem {} anos'.format(idade))
    print('\033[1;34mSÊNIOR')
else:
    print('O Aluno tem {} anos'.format(idade))
    print('\033[1;34mMASTER')