
principal = list()
dados = list()
while True:
    dados.append(str(input('\033[1;31mNome: ')))
    dados.append(float(input('\033[1;32mNota 1: ')))
    dados.append(float(input('\033[1;33mNota 2: ')))
    principal.append(dados[:])
    dados.clear()
    resposta = str(input('\033[1;34mQuer Continuar? [S/N] ')).lower().strip()
    if resposta == 'n':
        break



print('-='*20)
print(f'\033[1;33m{"No.":<8}{"NOME":<10}{"MEDIA":>8}')
print('-'*26)
for c,i in enumerate(principal):
    m = (i[1] + i[2]) / 2
    print(f'{c:<8}{i[0]:<10}{m:>8}')





while True:
    opc = int(input('\033[1;31mMostrar Nota de Qual Aluno? (999 Interrompe) '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(principal) - 1:
        print(f'\033[1;33mNotas de {principal[opc][0]} são {principal[opc][1]} e {principal[opc][2]}')
        print()