f = 1 
n = 1
s = 1
lts = []
nome = []
while f != 0 and n != '' and s != 'MF':
    n = str(input('Digite Seu nome: '))
    f = int(input('Digite Sua idade: '))
    s = str(input('Qual seu sexo? [M/F] ' )).upper()
    lts += [f]
    nome += [n]
print('')
print('O Nome do Mais Velho é {}, e tem {} anos'.format(max(nome), max(lts)))
