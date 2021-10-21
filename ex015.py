dias = int(input('Digite os dias que vai ficar alugado: '))
km = float(input('Digite os KM rodado: '))
pago = (dias * 60) + (km * 0.15)
print('Você tem que pagar {}R$'.format(pago))
