from time import sleep
from random import randint


print('-'*30)
print('\033[34mJOGO DE ADIVINHAÇÃO')
print('-'*30)
print('\033[34mNÚMERO DE 0 A 10')
sorteio = randint(0,10)

sleep(1)
print('\033[32mPROCESSANDO....')
sleep(1.5)
palpites = 0

n = int(input('\033[33mEM QUE NÚMERO ESTOU PENSANDO? '))
palpites += 1
while n != sorteio:
    if n < sorteio:
        print('\033[34mTENTE UM NÚMERO MAIOR')
    elif n > sorteio:
        print('\033[34mTENTE UM NÚMERO MENOR')
    n = int(input('\033[31mERROU TENTE NOVAMENTE? '))
    palpites += 1
print('\033[35mACERTOU COM {} TENTATIVAS'.format(palpites))