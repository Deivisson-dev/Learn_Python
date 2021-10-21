somaidade = 0
mediaidade = 0
maioridadehomen = 0
nomevelho = ''
mulher20 = 0

for p in range(1,5):
    print('-------{}ª Pessoa-------'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomen = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomen:
        maioridadehomen = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        mulher20 += 1
print('')
mediaidade = somaidade / 4
print('A Média de Idade do Grupo é: {} anos'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomen, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(mulher20))