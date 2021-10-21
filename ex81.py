lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    resp = str(input('Quer Continuar? [S/N] ')).lower().strip()
    if resp in 'n':
        break
print('-'*40)
print(f'Você digitou {len(lista)} elementos')
lista.sort(reverse=True)
print(f'Os Valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O Valor 5 faz parte da lista!')
else:
    print('O Valor 5 não faz parte da lista!')