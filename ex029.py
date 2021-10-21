velocidade = int(input('Digite a velocidade do carro? '))
multa = (velocidade - 80) * 7
if velocidade > 80:
    print('VOCÊ FOI MULTADO!')
    print('E Sua Multa foi de: {}R$'.format(multa))
else:
    print('MUITO BEM!, você está no limite!')