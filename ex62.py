ptermo = int(input('DIGITE O PRIMEIRO TERMO: ')) 
razao = int(input('DIGITE A RAZÃO: ')) 
termo = ptermo
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} → '.format(termo), end='')
        termo = termo + razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos vc quer mostrar a mais? '))
print('FIM')