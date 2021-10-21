from time import sleep

def lin():
    print('~'*40)
def contagem(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    lin()
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    sleep(2.5)
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += passo
        print('FIM!')
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont} ',end='', flush=True)
            sleep(0.5)
            cont -= passo
        print('FIM!')


contagem(1, 10, 1)
contagem(10, 0, 2)
lin()
print('CONTAGEM PERSONALIZADA')
i = int(input('INICIO: '))
f = int(input('FIM: '))
p = int(input('PASSO: '))
if p == 0:
    print('NÚMERO 0 INEXISTENTE NA CONTAGEM. CONTAREMOS COM O VALOR 1')
contagem(i, f, p)