resp = 'S'
media = 0
soma = 0
quant = 0
while resp in 'Ss':
        num = int(input('Digite um Valor: '))
        soma = soma + num
        quant += 1
        if quant == 1:
            maior = menor = num
        elif num > maior:
            maior = num
        elif num < menor:
            menor = num
        resp = str(input('Quer Continuar? [S/N] '))  
media = soma / quant
print('{} Valores digitados'.format(quant))
print('A Media Foi {:.2f}'.format(media))
print(' O Maior Valor é {} e o Menor é {}'.format(maior, menor))
