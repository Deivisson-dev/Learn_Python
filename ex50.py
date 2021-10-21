from time import sleep

print('SOMADOR DE PARES!!!')
sleep(0.5)
soma = 0
for c in range(1,7):
    num = int(input('Digite o {} número: '.format(c)))
    if num % 2 == 0:
        soma += num
print('A Soma dos número pares é igual a {}'.format(soma))