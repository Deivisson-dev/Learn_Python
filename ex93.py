time = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear()
    jogador["Nome"] = str(input("Nome do Jogador: "))
    tot = int(input(f'Quantas partidas {jogador["Nome"]} jogou: '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'Quantos gols na partida {c+1}: ')))
    jogador["gols"] = partidas[:]
    jogador["total"] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer Continuar? [S/N] ')).upper()[0]
        print('-'*25)
        if resp in 'SN':
            break
        print('Responda Apenas S OU N.')
        print('-'*25)
    if resp == 'N':
        break
print('-='*30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'*30)
for k, v in enumerate(time):
    print(f'{k:>3}  ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*30)
while True:
    busca = int(input('Mostrar dados de qual jogador (999 interrompe: '))
    if busca == 999:
        print("VOLTE SEMPRE!!!")
        break
    if busca >= len(time):
        print(f'ERRO! Não exites jogador com o codigo {5}')
    else:
        print(f' ---- LEVANTAMENTO DO JOGADOR {time[busca]["Nome"]}: ')
        for i, g in enumerate(time[busca]['gols']):
            print(f'     No Jogo {i+1} fez {g} gols')
    print('-'*40)


    