principal = list()
for c in range(1,8):
    principal.append(int(input(f'Digite o {c} Valor ')))

print('-'*30)
print('Os Valores pares digitados Foram ', end='')
for p in principal:
    if p % 2 == 0:
        print(f'[{sorted(p)}]',end='')
print()
print('Os Valores Impares digitados foram ', end='')
for p in principal:
    if p % 2 == 1:
        print(f'[{sorted(p)}]', end='')