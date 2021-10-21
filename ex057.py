s = str(input('Qual seu sexo? [M/F] ')).strip().upper()[0]

while s not in 'MmFf':
    s = str(input('Sexo Inválido... Digite Novamente: ')).strip().upper()[0]
print('SEXO {} REGISTRADO COM SUCESSO...'.format(s))