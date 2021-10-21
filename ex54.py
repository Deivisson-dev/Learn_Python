from datetime import date
from time import sleep
atual = date.today().year
maior = 0
meno = 0
for c in range(1,8):
    nasc = int(input('{}ª Ano De Nascimento: '.format(c)))
    sleep(1.5)
    idade = atual - nasc
    if idade >= 21:
        maior = maior + 1
    else:
        meno = meno + 1
print('')
print('{} pessoas são maiores de idade'.format(maior))
print('{} pessoas são menores de idade'.format(meno))