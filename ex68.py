from random import randint
from time import sleep

while True:
    computador = randint(0,10)
    jogador = int(input('\033[34mDIGITE UM NÚMERO: '))
    sleep(1.5)
    total = computador + jogador
    print('''\033[33mÍMPAR OU PAR?
    [ 1 ] PAR
    [ 2 ] ÍMPAR''')
    opcao = int(input('\033[33mQUAL VOCE ESCOLHE? '))
    if opcao != 1 and opcao != 2:
        break
    sleep(1.5)
    print(f'\033[32mO JOGADOR JOGOU {jogador} E O COMPUTADOR JOGOU {computador}. O TOTAL FOI {total}')
    print('\033[32mDEU PAR' if total % 2 == 0 else '\033[32mDEU ÍMPAR')
    
    if opcao == 1:
        if total % 2 == 0:
            print('\033[31mVOCÊ GANHOU!')
        else:
            print('\033[31mVOCÊ PERDEU!')
            break
    elif opcao == 2:
        if total % 2 == 1:
            print('\033[34mVOCÊ GANHOU!')
        else:
            print('\033[34mVOCÊ PERDEU!')
            break
    print('\033[33mVAMOS JOGAR DENOVO...')