print('-='*20)
print('Analisador de Triângulos')
print('-='*20)

r1 = float(input('Primeiro Segmento: '))
r2 = float(input('Segundo Segmento: '))
r3 = float(input('Terceiro Segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('OS SEGMENTOS PODEM FORMAR UM  TRIÂNGULO!')
else:
    print('OS SEGMENTOS NÂO PODEM FORMAR UM TRIÂNGULO:')