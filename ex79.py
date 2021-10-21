from time import sleep
valores = []
while True:
    n = int(input('Digite um valor: '))
    if n not in valores:
        valores.append(n)
        print('Valor adicionado com sucesso....')
    else:
        print('Valor duplicado! não vou adicionar...')
    resp = str(input('Quer Continuar? [S/N] ')).lower().strip()
    if resp == 'n':
        print('-'*35)
        print(f'Você digitou os valores {valores}')
        break