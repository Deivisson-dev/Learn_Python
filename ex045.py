from random import randint
from time import sleep
lista = ['Pedra', 'Papel', 'Tesoura']
comp = randint(0, 2)

print('''Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input('\033[1;31mQual opção você escolhe? '))
print('\033[1;31mJO')
sleep(1)
print('\033[1;31mKEN')
sleep(1)
print('\033[1;31mPO!!!')
sleep(1)
print('-=-'*11)
print('\033[1;31mComputador jogou: {}'.format(lista[comp]))
print('\033[1;31mJogador jogou {}'.format(lista[jogador]))
print('-=-'*11)
if comp == 0:#computador jogou pedra
    if jogador == 0:
        print('\033[1;31mEMPATOU!')
    elif jogador == 1:
        print('\033[1;31mJOGADOR VENCEU!')
    elif jogador == 2:
        print('\033[1;31mCOMPUTADOR VENCEU!')
    else:
        print('\033[1;31mOpção Inválida')

elif comp == 1: #computador jogou papel
    if jogador == 0:
        print('\033[1;31mCOMPUTADOR VENCEU')
    elif jogador == 1:
        print('\033[1;31mEMPATOU!')
    elif jogador == 2:
        print('\033[1;31mJOGADOR VENCEU')
    else:
        print('\033[1;31mOpção Inválida')
elif comp == 2:#computaador jogou tesoura
    if jogador == 0:
        print('\033[1;31mJOGADOR VENCEU')
    elif jogador == 1:
        print('\033[1;31mCOMPUTADOR VENCEU')
    elif jogador == 2:
        print('\033[1;31mEMAPATOU')
    else:
        print('\033[1;31mOpção Inválida')
    