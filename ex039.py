from datetime import date

nascimento = int(input('Qual seu ano de nascimento? '))
atual = date.today().year
idade = atual - nascimento
print('Quem nasceu em {}, tem {} anos, em {}'.format(nascimento, idade, atual))

if idade == 18:
    print('Você tem que se alistar, IMEDIATAMENTE')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda Falta {} anos para seu Alistamento'.format(saldo))
elif idade > 18:
    saldo = idade - 18
    print('Você ja deveria ter se alistado há {} anos'.format(saldo))