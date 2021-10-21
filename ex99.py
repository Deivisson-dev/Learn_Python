from time import sleep
def lin():
    print('~'*40)
def maior(*num):
    print('Analisando os Valores Passados...')
    sleep(0.5)
    print(f'{num} foram informados {len(num)} valores ao todo ', flush=True)
    sleep(0.5)
    print(f'O Maior Valor Informado foi {max(num)}.')
    lin()
    sleep(1)


maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior(0)

