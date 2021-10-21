n = s = cont = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s = s + n
    cont += 1
print(f'A Soma dos {cont} valores foi {s}!')