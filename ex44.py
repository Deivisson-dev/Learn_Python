preco = float(input('Preço das Compras? '))
print(''' FORMAS DE PAGAMENTO
[ 1 ] á vista dinheiro/cheque
[ 2 ] á vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual a opção desejada? '))

if opcao == 1:
    total = preco - (preco * 10 / 100)
    print('Sua compra de {}R$ vai custar, {}R$ no final da compra'.format(preco, total)) 
elif opcao == 2:
    total = preco - (preco * 5 / 100)
    print('Sua compra de {}R$ vai custar, {}R$ no final da compra'.format(preco, total))
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra sera parcelada em 2x de {}R$'.format(parcela))
    print('Sua compra de {}R$ vai custar, {}R$ no final da compra'.format(preco, total))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totalparc = int(input('Quantas Parcelas? '))
    parcela = total / totalparc
    print('Sua compra sera parcelada em {}x de {:.2f}R$'.format(totalparc, parcela))
    print('Sua compra de {}R$ vai custar, {}R$ no final da compra'.format(preco, total))
else:
    total = 0
    print('\033[1;31mOPÇÂO INVALIDA')