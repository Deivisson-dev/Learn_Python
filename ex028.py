import random
import time

print('-' * 30)
n = int(input('Digite um número de 0 a 5: '))
print('-' * 30)
sort = random.randint(0, 5)

print('PROCESSANDO...')
time.sleep(3)


if sort == n:
    print('PARABENS, Você Ganhou da Maquina')
else:
    print('PERDEU, o número correto era: {}'.format(sort))