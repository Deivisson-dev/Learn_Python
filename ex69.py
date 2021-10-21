from time import sleep
tot18 = 0
tothomen = 0
totmulher20 = 0

while True:
    print('-'*20)
    print('CADASTRAR UMA PESSOA')
    print('-'*20)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    
    if idade >= 18:
        tot18 += 1
    
    if sexo == 'M':
        tothomen += 1
    
    if sexo == 'F' and idade < 20:
        totmulher20 += 1


    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer Continuar? [S/N] ')).upper().strip()[0]

    if resp == 'N':
        break


print('-'*20)
print('FIM DO PROGRAMA')
print('-'*20)
print('Total de Pessoas com mais de 18 anos : {}'.format(tot18))
print('Ao todo temos {} homens cadastrados'.format(tothomen))
print('E temos {} mulheres com menos de 20 anos'.format(totmulher20))
