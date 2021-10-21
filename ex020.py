import random

a1 = input('Digite um nome: ')
a2 = input('Digite outro: ')
a3 = input('DIgite outro: ')
a4 = input('Digite outro: ')
a = (a1,a2,a3,a4)
sorteio = random.sample(a, 4)
print('A ordem foi: {}'.format(sorteio))