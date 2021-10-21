galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa["nome"] = str(input('Nome: '))
    while True:
        pessoa["sexo"] = str(input('Sexo: [M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor digie apenas M ou F.')
    pessoa["idade"] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer Continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S OU N.')
    if resp == 'N':
        break


media = soma / len(galera)
print('-'*30)
print(f'A) Ao todo temos {len(galera)} pessoas Cadastradas')
print(f'B) A Média de idade de pessoas é {media:.2f} anos')
print(f'C) As Mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}, ',end='')
print()
print(f'D) Lista das Pessoas que estão acima da Média: ')
for p in galera:
    if p['idade'] >= media:
        print('   ')
        for k, v in p.items():
            print(f'{k} = {v}')
        print()
print('ENCERRADO')