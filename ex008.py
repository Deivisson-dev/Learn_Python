n = int(input('Digite um valor em metros: '))
cm = n * 100
mi = n * 1000
print('\033[1;31m{} em centimetros é {}cm e em milimetros é {}mm'.format(n,cm, mi))