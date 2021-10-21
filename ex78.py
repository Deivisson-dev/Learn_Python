from time import sleep
valores = []
for c,cont in enumerate(range(0,5)):
    valores.append(int(input(f'Digite um Valor para a posição {c}: ')))
sleep(2)
print('-'*40)
print(f'Voce digitou os valores {valores}')
print(f'O Maior valor digitado foi {max(valores)} na posição {valores.index(max(valores))}')
print(f'O Menor valor digitado foi {min(valores)} na posição {valores.index(min(valores))}')
