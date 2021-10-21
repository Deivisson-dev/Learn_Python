from time import sleep

print('\033[34mMENU DE OPÇÕES')

sleep(1.5)
n1 = int(input('\033[34mDIGITE UM VALOR: '))
n2 = int(input('\033[34mDIGITE OUTRO VALOR: '))
lts = [n1,n2]
soma = n1 + n2
multi = n1 * n2
maior = max(lts)
opcao = 0
while opcao != 5:
    print('''\033[34m
    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] SAIR''')
    opcao = int(input('\033[35mQUAL OPÇÃO? '))
    sleep(2)
    if opcao == 1:
            print('\033[33mA SOMA É {} + {} = {}'.format(n1, n2, soma))
            sleep(2)
    elif opcao == 2:
            print('\033[32mA MULTIPLICAÇÃO É {} X {} = {}'.format(n1, n2 , multi))
            sleep(2)
    elif opcao == 3:
                if n1 > n2:
                    maior = n1
                else:
                    maior = n2
                print('Entre {} e {}, o maior valor é {}'.format(n1,n2,maior))        
    elif opcao == 4:
            print('\033[34mINFORME OS NÚMEROS NOVAMENTE: ')
            n1 = int(input('\033[34mDIGITE UM VALOR: '))
            n2 = int(input('\033[34mDIGITE OUTRO VALOR: '))
            sleep(2)
    elif opcao == 5:
            print('\033[33mFINALIZANDO....')