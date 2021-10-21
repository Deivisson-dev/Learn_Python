principal = list()
dado = list()
tot = 0
maior: 0
menor: 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    if len(principal) == 0:
        maior = menor = dado[1]
    else:
        if dado[1] > maior:
            maior = dado[1]
        if dado[1] < menor:
            menor = dado[1]
    principal.append(dado[:])
    dado.clear()
    tot += 1
    resp = str(input('Quer Continuar? [S/N] ')).strip().lower()
    if resp == 'n':
        break

print('-'*35)
print(f'Ao todo Foram Cadastradas {len(principal)} pessoas')
print(f'O Maior peso foi de {maior}. Peso de ', end=' ')
for p in principal:
    if p[1] == maior:
        print(f'[{p[0]}]', end='')
print()
print(f'O Menor peso foi de {menor}. Peso de ', end='')
for p in principal:
    if p[1] == menor:
        print(f'[{p[0]}]', end='')
print()