lst = []

for c in range(1,6):
    peso = float(input('\033[31mPeso da {}ª Pessoa: '.format(c)))
    lst += [peso]
print('')
print('\033[34mO Maior peso lido foi {}Kg'.format(max(lst)))
print('\033[34mO Menor peso lido foi {}Kg'.format(min(lst)))