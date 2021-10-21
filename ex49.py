n = int(input('Digite Um Número: '))

for c in range(1,11):
    d = n * c
    print('\033[1;31m{}x{} = {}'.format(n,c,d))