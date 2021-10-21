frase = input('Digite Uma Frase: ').replace(' ', '').upper()

if frase == frase[::-1]:
    print('O Inverso de {} é {}'.format(frase, frase[::-1]))
    print('É UM PALINDROMO')
else:
    print('O Inverso de {} é {}'.format(frase, frase[::-1]))
    print('NÂO É UM PALINDROMO')