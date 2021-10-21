from typing import Counter


num = (int(input('Digite um Número: ')),int(input('Digite Outro Número: ')),int(input('Digite mais outro Número: ')),int(input('Digite novamente outro  Número: ')))
print(f'Os Valores Digitados Foram: {num}')
print(f'O Valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O Valor 3 apareceu na {num.index(3)+1}ª Posição')
else:
    print('O valor 3 não foi digitado.')

print('os Valores pares digitados foram: ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
