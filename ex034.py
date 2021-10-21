s = float(input('Informe o seu Salário: '))

su = s + (s * 10 / 100)
si = s + (s * 15 / 100)

if s > 1250:
    print('O seu aumento vai ser R${}'.format(su))
else:
    print('o seu aumento vai ser R${}'.format(si))
