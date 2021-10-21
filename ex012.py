p = int(input('Digite o preço do produto: R$'))

novo = p - (p * 5 / 100)
print('O Produto  que custava {}R$, na promoção, com desconto custa {}R$'.format(p, novo))