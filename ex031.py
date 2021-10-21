d = float(input('Qual a distância da sua viagem? '))
preco = d * 0.50
p2 = d * 0.45

if d <= 200:
    print('A Passagem é: R${}'.format(preco))
else:
    print('A Passagem é: R${}'.format(p2))