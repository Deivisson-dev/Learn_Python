n = int(input('Digite um número inteiro: '))
print('''Escolha um número, para realizar a conversão:
[ 1 ] converter para BINÀRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
op = int(input('Digite sua opção: '))

if op == 1:
    print('{} convertido para BINARIO é {}'.format(n, bin(n)))
elif op == 2:
    print('{} convertido para OCTAL é {}'.format(n, oct(n)))
elif op == 3:
    print('{} convertido para HEXADECIMAL é {}'.format(n, hex(n)))
else:
    print('OPÇÂO INVÁLIDA')
    