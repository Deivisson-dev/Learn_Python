valor = float(input('Qual valor da casa? '))
salario = float(input('Qual o valor do seu salário? '))
ano = int(input('Quantos anos você vai pagar? '))
pre = valor / (ano * 12)
min = salario * 30 / 100
print('Para pagar um casa de {:.2f}R$ em {}anos'.format(valor, ano))
print('A prestaçao será de {:.2f}R$'.format(pre))

if pre <= min:
    print('Emprestimo,pode ser concedido')
else:
    print('Emprestimo Negado')

