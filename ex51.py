ptermo = int(input('Digite o Primeiro número: '))
razao = int(input('Digite a razão: '))
PA = ptermo + razao*10

for c in range(ptermo,PA,razao):
    print(c,end=' → ')