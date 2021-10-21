n1 = float(input('Qual foi a sua Primeira nota? '))
n2 = float(input('Qual foi a sua Segunda nota? '))
m = (n1 + n2) / 2

if m < 5:
    print('\033[1;31mA Sua Media Foi {}'.format(m))
    print('\033[1;31mREPROVADO')
elif m >= 5 and m <= 6.9:
    print('\033[1;31mA Sua media foi {}'.format(m))
    print('\033[1;33mRECUPERAÇAO')
elif m >= 7:
    print('\033[1;31mA Sua Média Foi {}'.format(m))
    print('\033[1;32mAPROVADO')