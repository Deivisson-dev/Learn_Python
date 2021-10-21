from random import randint
from time import sleep
princ = list()
jogos = list()
print('-'*25)
print('JOGOS NA MEGA-SENA')
print('-'*25)
quant = int(input('Quantos Jogos Você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in princ:
            princ.append(num)
            cont += 1
        if cont >= 6:
            break
    princ.sort()
    jogos.append(princ[:])
    princ.clear()
    tot += 1
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)