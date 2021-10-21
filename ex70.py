from time import sleep
total = 0
totmaismil = 0
cont = 0
menor = 0
barato = ''
while True:
    print('-'*25)
    print('FEIRA DA TROCA')
    print('-'*25)
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$'))
    cont += 1
    total += preco
    

    if preco > 1000:
        totmaismil += 1

    if cont == 1:
        menor = preco
        barato = produto
    else:
        if preco < menor:
            menor = preco
            barato = produto





    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer Continuar? [S/N] ')).strip().upper()[0]

    if resp == 'N':
        break

print('-'*30)
print('FIM DO PROGRAMA')
print('-'*30)
print(f'O Total Gasto Na Compra Foi {total}')
print(f'{totmaismil} Produtos Custam Mais de 1000R$')
print(f'O Produto Mais barato foi a {barato} que custa {menor}R$')
