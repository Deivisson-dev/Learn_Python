import math
from random import randint
print('-'*25)
print('BANCO BRADESCO')
print('-'*25)
valor = int(input("SAQUE: "))
nota50 = valor / 50
valor %= 50
nota20 = valor / 20
valor %= 20
nota10 = valor / 10
valor %= 10
nota1 = valor / 1
valor %= 1

print('-'*30)
print(f'TOTAL DE CEDULAS DE 50R$: {math.trunc(nota50)}')
print(f'TOTAL DE CEDULAS DE 20R$: {math.trunc(nota20)}')
print(f'TOTAL DE CEDULAS DE 10R$: {math.trunc(nota10)}')
print(f'TOTAL DE CEDULAS DE 1R$: {math.trunc(nota1)}')
print('-'*30)

